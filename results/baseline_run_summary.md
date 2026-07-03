# Baseline run summary (T06)

Pipeline 1: full-corpus BM25 retrieval + a local generator, answering from context only. This is the curated summary; the full per-question predictions live in `results/raw_outputs/baseline_bm25.jsonl` (gitignored, regenerate with `python src/pipeline_baseline.py`).

## Run config

| setting | value |
|---|---|
| pipeline | baseline_bm25 |
| model | ollama:llama3.2 |
| retrieval | bm25 |
| chunk_strategy | fixed_512 |
| top_k | 3 |
| temperature | 0.0 |
| n_examples | 150 |

## What came out

- Questions answered: **150** (all of FinanceBench open-source).
- Retrieval reached the correct filing (top-3): **63/150 = 42%**.
- Model abstained ("I don't know"): **121/150 = 81%**.
- Model gave an answer: **29/150 = 19%**.
- Answered *and* the right filing was never retrieved: **4/150**. These are the prime hallucination suspects for the error analysis (T19-T23): the model committed to an answer with no supporting document in context.

## Abstention by question type

| question_type | total | abstained | abstain rate |
|---|---|---|---|
| metrics-generated | 50 | 50 | 100% |
| domain-relevant | 50 | 41 | 82% |
| novel-generated | 50 | 30 | 60% |

## Reading it

The naive BM25 retriever only surfaces the correct filing about two times in five, and with the wrong context in front of it the model mostly refuses to answer. So the baseline trades away coverage for safety: few outright fabrications, but it leaves most questions on the table. That gap is what the dense and query-rewrite pipelines (T14, T15) are meant to close, and the small set of answered-but-unsupported cases is where we expect to find the clearest hallucinations.
