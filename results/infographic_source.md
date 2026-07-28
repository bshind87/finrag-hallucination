# Infographic source — all results in one place

Paste this into NotebookLM (or any infographic tool) to generate a one-image summary for
the poster/PPT. Every number here is verified against the report's tables — tell the tool
**not to invent numbers**, and spot-check the rendered image against this file before using it.

**Title:** Analyzing Hallucination Patterns in RAG-based Financial Question Answering
**Dataset:** FinanceBench open subset — 150 questions over 84 SEC filings (32 companies)
**Setup:** One RAG pipeline; we change **one component at a time** so each result maps to one
research question. Generator = GPT-3.5-turbo (temp 0) unless noted; RAGAS judge = GPT-4o-mini.
Retr@k = % of questions whose top-k retrieval reached the correct filing; Faith(ans) =
faithfulness over answered questions; EM(num) = numeric-tolerant exact match.

## Headline findings
- **RQ1 — Retrieval is the dominant lever.** As retrieval improves (BM25 → Dense → query
  rewrite), the correct filing is reached **43% → 64% → 69%** of the time, and coverage,
  faithfulness, and accuracy rise together. An oracle that always retrieves the right filing
  hits 100% retrieval but still leaves a third of questions unanswered.
- **RQ2 — Numerical errors dominate** hallucinations (**46%**), then entity errors (31%).
  **~22%** of automatically flagged "failures" were actually correct answers mis-scored.
- **RQ3 — Given the SAME retrieved context, the open Mistral-7B is far more faithful** than
  GPT-3.5 (**0.59 vs 0.21**) and ~2× more numerically accurate (EM 0.37 vs 0.21), but more
  conservative (answers 69 vs 87 of 150). Abstention behavior, not model scale, drives grounding.

## Big-number callouts (feature these)
- **43% → 69%** correct-filing retrieval (BM25 → Enhanced)
- **0.59 vs 0.21** faithfulness (Mistral vs GPT-3.5, same context)
- **46%** of hallucinations are numerical
- **~22%** of flagged "failures" were actually correct
- **100%** oracle retrieval, yet only **96/150** answered

## Master results table (all configurations, 150 questions)
| Group | Config | Retr@k | Faith(ans) | Ctx.Prec | Answered | F1 | EM(num) |
|---|---|---|---|---|---|---|---|
| Retrieval | Baseline (BM25) | 43% | 0.408 | 0.240 | 47/150 | 0.083 | 0.120 |
| Retrieval | Dense (512, top-3) | 64% | 0.352 | 0.417 | 82/150 | 0.116 | 0.180 |
| Retrieval | Enhanced (rewrite) | 69% | 0.353 | 0.462 | 87/150 | 0.121 | 0.207 |
| Retrieval | Single-doc (oracle) | 100% | 0.572 | 0.435 | 96/150 | 0.139 | 0.267 |
| Ablation | Dense, top-5 | 73% | 0.397 | 0.388 | 97/150 | 0.126 | 0.220 |
| Ablation | Dense, 256-token | 59% | 0.462 | 0.288 | 70/150 | 0.095 | 0.160 |
| Generator | Enhanced + Mistral-7B | 69% | 0.631 | 0.411 | 69/150 | 0.128 | 0.373 |

## Hallucination taxonomy (39 genuine cases, from 50 answered-but-wrong)
| Type | Share | Count | Meaning |
|---|---|---|---|
| Numerical | 46% | 18 | right item, wrong value/calculation |
| Entity | 31% | 12 | wrong company/segment (often wrong-filing retrieval) |
| Unsupported | 15% | 6 | fabricated, not in any retrieved chunk |
| Reasoning | 8% | 3 | right inputs, wrong inference |

*Plus 11 of 50 flagged cases were actually correct — a caution for automatic metrics.*

## Ablations (one-liners)
- **Retrieval depth:** top-5 beats top-3 (retrieval 64→73%, answered 82→97).
- **Chunk size:** 512 beats 256 tokens (smaller chunks split a figure from its label).

## Optional — automatic detector (RoBERTa on RAGTruth, proof-of-concept)
Zero-shot transfer to our labels: F1 **0.81** (recall 0.85) but low specificity (clears only
1 of 11 grounded) — a high-recall **over-flagger**, not a precise judge.
