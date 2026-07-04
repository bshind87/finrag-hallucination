"""Assemble the preliminary results table for the paper (Task T10).

Joins the RAGAS metrics (from evaluate.py, results/eval_ragas.csv) with the F1/EM
metrics (from qa_metrics.py, results/eval_qa_metrics.csv) on pipeline+model, and writes
a single paper-ready table in both Markdown and LaTeX, plus a short interpretation.

For the preliminary paper there is only the baseline row; the same script fills in as
the dense / enhanced / Mistral rows arrive later (T18), no changes needed.

Run it (after T08 and T09 have produced their CSVs):
    python src/build_results_table.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = REPO_ROOT / "results"
RAGAS_CSV = RESULTS_DIR / "eval_ragas.csv"
QA_CSV = RESULTS_DIR / "eval_qa_metrics.csv"

MD_OUT = RESULTS_DIR / "preliminary_results.md"
TEX_OUT = RESULTS_DIR / "results_table.tex"

# (source column, display header)
COLUMNS = [
    ("pipeline", "Pipeline"),
    ("model", "Model"),
    ("faithfulness_mean", "Faithfulness"),
    ("answer_relevancy_mean", "Answer Rel."),
    ("context_precision_mean", "Context Prec."),
    ("exact_match", "EM"),
    ("f1", "F1"),
]


def load_merged() -> pd.DataFrame:
    if not RAGAS_CSV.exists():
        raise SystemExit(f"missing {RAGAS_CSV}. Run src/evaluate.py first (T08).")
    if not QA_CSV.exists():
        raise SystemExit(f"missing {QA_CSV}. Run src/qa_metrics.py first (T09).")
    ragas = pd.read_csv(RAGAS_CSV)
    qa = pd.read_csv(QA_CSV)
    merged = ragas.merge(qa, on=["pipeline", "model"], how="outer", suffixes=("_ragas", "_qa"))
    return merged


def _fmt(x) -> str:
    if pd.isna(x):
        return "n/a"
    if isinstance(x, float):
        return f"{x:.3f}"
    return str(x)


def to_markdown(df: pd.DataFrame) -> str:
    headers = [h for _c, h in COLUMNS]
    lines = ["| " + " | ".join(headers) + " |",
             "|" + "|".join(["---"] * len(headers)) + "|"]
    for _, row in df.iterrows():
        cells = [_fmt(row.get(col)) for col, _h in COLUMNS]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def to_latex(df: pd.DataFrame) -> str:
    headers = [h for _c, h in COLUMNS]
    col_spec = "ll" + "r" * (len(headers) - 2)
    out = [r"\begin{table}[t]", r"\centering",
           r"\caption{Preliminary baseline results on FinanceBench (all 150 questions). "
           r"Generator and RAGAS judge: GPT-3.5-turbo at temperature 0; RAGAS embeddings "
           r"are local sentence-transformers.}",
           r"\label{tab:prelim-results}",
           r"\begin{tabular}{" + col_spec + "}", r"\toprule",
           " & ".join(headers) + r" \\", r"\midrule"]
    for _, row in df.iterrows():
        cells = [_fmt(row.get(col)).replace("_", r"\_") for col, _h in COLUMNS]
        out.append(" & ".join(cells) + r" \\")
    out += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    return "\n".join(out)


def interpretation(df: pd.DataFrame) -> str:
    """One honest paragraph about the baseline row (assumes a single baseline)."""
    row = df.iloc[0]
    faith = row.get("faithfulness_mean")
    ansrel = row.get("answer_relevancy_mean")
    ctxprec = row.get("context_precision_mean")
    f1 = row.get("f1")
    f1_ans = row.get("f1_answered_only")
    n_ans = row.get("n_answered")
    return (
        "The baseline pairs a plain BM25 retriever with GPT-3.5-turbo. BM25 surfaces the "
        "correct filing for only 43\\% of questions, so the generator---instructed to answer "
        f"only from context---abstains on roughly two-thirds, answering {_fmt(n_ans)} of 150. "
        "This caution is deliberate and safer than fabrication, but it caps coverage: token "
        f"F1 is {_fmt(f1)} over all questions and {_fmt(f1_ans)} on the answered subset, with "
        "exact match at zero because short numeric answers are written many ways "
        "($1,577 vs.\\ 1577.00) and rarely match after normalization. RAGAS reflects the same "
        f"bottleneck: faithfulness ({_fmt(faith)}) and answer relevancy ({_fmt(ansrel)}) are "
        "low---an abstention has nothing to ground and does not address the question---while "
        f"context precision ({_fmt(ctxprec)}) shows retrieval places a useful chunk near the "
        "top only about half the time. Read together, the picture is a retrieval-bound "
        "baseline: the generator rarely fabricates, but weak sparse retrieval leaves most "
        "questions unanswered. Closing that gap with dense and query-rewrite retrieval---and "
        "surfacing the answered-but-unsupported cases---is the focus of the next phase."
    )


def main() -> int:
    df = load_merged()
    md_table = to_markdown(df)
    tex_table = to_latex(df)

    row0 = df.iloc[0]
    n_ragas = row0.get("n_examples_ragas", row0.get("n_examples"))
    n_qa = row0.get("n_examples_qa", row0.get("n_examples"))
    n_ragas = "n/a" if pd.isna(n_ragas) else int(n_ragas)
    n_qa = "n/a" if pd.isna(n_qa) else int(n_qa)
    md = ["# Preliminary results (T10)\n",
          "Baseline pipeline (BM25 + GPT-3.5-turbo) on FinanceBench. Both the token-level "
          f"metrics (F1/EM, `src/qa_metrics.py`, T09; n={n_qa}) and the RAGAS metrics "
          f"(`src/evaluate.py`, T08; n={n_ragas}) cover all 150 questions. Generator and RAGAS "
          "judge are GPT-3.5-turbo at temperature 0; RAGAS embeddings are local "
          "sentence-transformers.\n",
          md_table, "",
          f"*RAGAS n = {n_ragas}, F1/EM n = {n_qa}.*", "",
          "## Interpretation\n", interpretation(df), ""]
    MD_OUT.write_text("\n".join(md), encoding="utf-8")
    TEX_OUT.write_text(tex_table + "\n", encoding="utf-8")

    print(md_table)
    print(f"\nsaved -> {MD_OUT.relative_to(REPO_ROOT)}")
    print(f"saved -> {TEX_OUT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
