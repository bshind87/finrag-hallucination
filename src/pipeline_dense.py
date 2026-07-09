"""Pipeline 2: Dense RAG with FAISS + MiniLM embeddings (Task T14).

Semantic retrieval variant of the baseline. Instead of BM25 term matching, we embed
every chunk with ``sentence-transformers/all-MiniLM-L6-v2`` and retrieve the top-k by
cosine similarity from a FAISS index built over the whole corpus (all 84 filings).
The generator, prompt template, temperature, and output schema are identical to the
BM25 baseline (T06), so the only thing that changes is *retrieval* -- that is the
controlled comparison for RQ1.

Chunk embeddings are cached to disk (data/processed/) so the enhanced pipeline (T15)
reuses them without re-encoding.

Run it:
    python src/pipeline_dense.py                  # all 150, top-3, GPT-3.5
    python src/pipeline_dense.py --limit 3        # quick smoke test
    python src/pipeline_dense.py --backend ollama # local generator
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
from dotenv import load_dotenv
from tqdm import tqdm

from llm import LOCAL_EMBEDDING_MODEL, get_backend, make_client
from pipeline_baseline import PROMPT_TEMPLATE, _chat, load_questions
from preprocess import load_chunks
from schema import RunConfig, validate_row, write_predictions

REPO_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = REPO_ROOT / "data" / "processed"
DEFAULT_OUT = REPO_ROOT / "results" / "raw_outputs" / "dense_faiss.jsonl"


class DenseRetriever:
    """MiniLM + FAISS cosine retriever over the full chunk corpus.

    Embeddings are L2-normalized and indexed with inner product, so inner product
    equals cosine similarity. Chunk embeddings are cached per (strategy, model).
    """

    def __init__(self, chunks_df, model_name: str = LOCAL_EMBEDDING_MODEL,
                 strategy: str = "fixed_512"):
        import faiss
        from sentence_transformers import SentenceTransformer

        self.ids = chunks_df["chunk_id"].tolist()
        self.texts = chunks_df["text"].tolist()
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

        cache = PROCESSED_DIR / f"emb_{strategy}_{model_name.split('/')[-1]}.npy"
        if cache.exists():
            print(f"loading cached chunk embeddings <- {cache.name}")
            emb = np.load(cache)
        else:
            print(f"embedding {len(self.texts)} chunks with {model_name} ...")
            emb = self.model.encode(self.texts, batch_size=64, show_progress_bar=True,
                                    convert_to_numpy=True, normalize_embeddings=True)
            np.save(cache, emb)
            print(f"cached chunk embeddings -> {cache.name}")
        emb = emb.astype("float32")

        self.index = faiss.IndexFlatIP(emb.shape[1])
        self.index.add(emb)

    def top_k(self, query: str, k: int) -> list[tuple[str, str]]:
        q = self.model.encode([query], convert_to_numpy=True,
                              normalize_embeddings=True).astype("float32")
        _scores, idx = self.index.search(q, k)
        return [(self.ids[i], self.texts[i]) for i in idx[0]]


def run(backend_name, chunk_strategy, top_k, model, temperature, limit, out_path,
        embedding_model=LOCAL_EMBEDDING_MODEL):
    out_path = Path(out_path).resolve()
    load_dotenv(REPO_ROOT / ".env")
    backend = get_backend(backend_name)
    model = model or backend.default_model
    client = make_client(backend)
    print(f"generator: {backend.name} / {model} (temp {temperature})")

    chunks_df = load_chunks(chunk_strategy)
    retriever = DenseRetriever(chunks_df, embedding_model, chunk_strategy)
    questions = load_questions(limit)

    rows = []
    for q in tqdm(questions, desc="dense RAG"):
        retrieved = retriever.top_k(q["question"], top_k)
        contexts = [t for _c, t in retrieved]
        chunk_ids = [c for c, _t in retrieved]
        prompt = PROMPT_TEMPLATE.format(context="\n\n---\n\n".join(contexts),
                                        question=q["question"])
        answer = _chat(client, model, prompt, temperature)
        row = {
            "financebench_id": q["financebench_id"], "question": q["question"],
            "contexts": contexts, "retrieved_chunk_ids": chunk_ids,
            "generated_answer": answer, "gold_answer": q["answer"],
            "doc_name": q["doc_name"], "question_type": q["question_type"],
        }
        validate_row(row)
        rows.append(row)

    cfg = RunConfig(pipeline="dense_faiss", model=f"{backend.name}:{model}",
                    retrieval="dense", chunk_strategy=chunk_strategy, top_k=top_k,
                    temperature=temperature, embedding_model=embedding_model,
                    notes="FAISS cosine over MiniLM chunk embeddings; same prompt as baseline.")
    path = write_predictions(rows, cfg, out_path)
    print(f"wrote {len(rows)} predictions -> {path.relative_to(REPO_ROOT)}")

    hit = sum(1 for r in rows if any(cid.split("::")[0] == r["doc_name"]
                                     for cid in r["retrieved_chunk_ids"]))
    print(f"retrieval reached the correct filing for {hit}/{len(rows)} "
          f"({hit / len(rows):.1%})")
    return path


def main() -> int:
    p = argparse.ArgumentParser(description="Dense FAISS RAG pipeline (Task T14).")
    p.add_argument("--backend", choices=("ollama", "openai"), default=None)
    p.add_argument("--chunk-strategy", choices=("fixed_512", "sentence"), default="fixed_512")
    p.add_argument("--top-k", type=int, default=3)
    p.add_argument("--model", default=None)
    p.add_argument("--temperature", type=float, default=0.0)
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--out", type=Path, default=DEFAULT_OUT)
    a = p.parse_args()
    run(a.backend, a.chunk_strategy, a.top_k, a.model, a.temperature, a.limit, a.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
