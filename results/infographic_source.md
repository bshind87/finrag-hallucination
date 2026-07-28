# Infographic source — all results in one place

Paste this into NotebookLM (or any infographic tool) to generate a one-image summary for
the poster/PPT. Every number here is verified against the report's tables.

## Rules for the tool (read first)
- **Use ONLY the numbers in this file. Do not invent, estimate, or pull figures from any
  other source.** (A prior run fabricated a "150/150 answered, 78% accuracy" row — that is
  wrong; no configuration answered 150/150.)
- The **~22% mis-scored** result is a *callout*, NOT a data row with its own accuracy/answered numbers.
- The hallucination-type chart must have **exactly four slices that sum to 100%**:
  Numerical 46%, Entity 31%, Unsupported 15%, Reasoning 8%. **No "Other" slice, no fifth slice.**
- Keep faithfulness consistent: the tables below use **answered-only** faithfulness (Faith(ans)).
  The "0.59 vs 0.21" figure is *overall* faithfulness and appears only as a labeled callout.

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
  GPT-3.5 (**0.59 vs 0.21** overall) and ~2× more numerically accurate (EM 0.37 vs 0.21), but
  more conservative (answers 69 vs 87 of 150). Abstention behavior, not model scale, drives grounding.

## Big-number callouts (feature these)
- **43% → 69%** correct-filing retrieval (BM25 → Enhanced)
- **0.59 vs 0.21** faithfulness — Mistral vs GPT-3.5, same context (overall)
- **46%** of hallucinations are numerical
- **~22%** of flagged "failures" were actually correct
- **100%** oracle retrieval, yet only **96/150** answered

## Block 1 — Retrieval ladder (RQ1, GPT-3.5)
| Config | Retr@k | Faith(ans) | Ctx.Prec | Answered | EM(num) |
|---|---|---|---|---|---|
| Baseline (BM25) | 43% | 0.408 | 0.240 | 47/150 | 0.120 |
| Dense (512, top-3) | 64% | 0.352 | 0.417 | 82/150 | 0.180 |
| Enhanced (rewrite) | 69% | 0.353 | 0.462 | 87/150 | 0.207 |
| Single-doc (oracle) | 100% | 0.572 | 0.435 | 96/150 | 0.267 |

## Block 2 — Ablations (Dense, GPT-3.5)
- **Retrieval depth:** top-5 beats top-3 — retrieval 64→73%, answered 82→97/150, EM 0.18→0.22.
- **Chunk size:** 512 beats 256 tokens — retrieval 64 vs 59%, answered 82 vs 70/150;
  smaller chunks split a financial figure from its label.

## Block 3 — Generator on identical Enhanced context (RQ3)
| Generator | Faith(ans) | Answered | EM(num) |
|---|---|---|---|
| GPT-3.5-turbo | 0.353 | 87/150 | 0.207 |
| Mistral-7B | 0.631 | 69/150 | 0.373 |

## Hallucination taxonomy — donut/bar, EXACTLY these 4 slices (sum = 100%)
| Type | Share | Count | Meaning |
|---|---|---|---|
| Numerical | 46% | 18 | right item, wrong value/calculation |
| Entity | 31% | 12 | wrong company/segment (often wrong-filing retrieval) |
| Unsupported | 15% | 6 | fabricated, not in any retrieved chunk |
| Reasoning | 8% | 3 | right inputs, wrong inference |

*(Do NOT add an "Other" slice. The 11 "other" cases were the mis-scored-correct ones — they
are excluded from this 39-case taxonomy and reported separately as the ~22% callout.)*

## Optional — automatic detector (RoBERTa on RAGTruth, proof-of-concept)
Zero-shot transfer to our labels: F1 **0.81** (recall 0.85) but low specificity (clears only
1 of 11 grounded) — a high-recall **over-flagger**, not a precise judge.

## Copy/wording fixes for the current draft image
- Rename the broken heading "Mistral achieved AI Models" → **"Open Model, Higher Faithfulness."**
- Fix typo **"invoive" → "involve."**
- Replace the donut's **"Other (8%)"** with **"Reasoning (8%)"** and remove any extra slice.
- The chunk-illustration cell text is decorative gibberish (373 / 202 / lc95 / TAX); fine for a
  poster, but real labels (e.g. "Revenue 1,577") would look cleaner.
