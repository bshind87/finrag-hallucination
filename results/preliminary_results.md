# Preliminary results (T10)

Baseline pipeline on FinanceBench. F1 and Exact Match (from `src/qa_metrics.py`, T09) cover all 150 questions. The RAGAS metrics (from `src/evaluate.py`, T08) were run on a balanced 50-question subset for the preliminary paper, since the local judge is slow; we will score the full set for the final paper. All runs use temperature 0.

| Pipeline | Model | Faithfulness | Answer Rel. | Context Prec. | EM | F1 |
|---|---|---|---|---|---|---|
| baseline_bm25 | ollama:llama3.2 | 0.361 | 0.197 | 0.842 | 0.000 | 0.111 |

*RAGAS n = 50, F1/EM n = 150.*

## Interpretation

The baseline pairs a plain BM25 retriever with a small local generator, and the numbers show why finance QA is hard for this setup. Token F1 sits at 0.111 and exact match at zero: even when the model answers, it rarely reproduces the gold figure exactly, partly because the same number gets written many ways ($1,577 vs 1577.00). Context precision is the bright spot at 0.842, meaning that when a relevant chunk is retrieved it tends to rank near the top, but recall is the problem: BM25 only reaches the right filing 42% of the time, so the model abstains on most questions. That abstention is why faithfulness (0.361) and answer relevancy (0.197) come out low, an abstention has nothing to ground and does not address the question, so RAGAS scores it near zero. Read together, the baseline is cautious rather than reckless: it answers only 29 of 150, and on that answered subset F1 climbs to 0.269. Closing the retrieval gap with dense and query-rewrite retrieval is the obvious next step, and it should also surface more of the hallucinations we want to study.
