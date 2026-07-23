# T16 Hyperparameter Sweep Results

Dense (FAISS + MiniLM) pipeline, GPT-3.5-turbo generator, temperature 0.0, full 150-question FinanceBench set. RAGAS judge: GPT-3.5-turbo; embeddings: local MiniLM.

| Config | Chunk (tok) | Top-k | Faithfulness | Answer Rel. | Ctx. Prec. | F1 | Numeric-EM | Answered |
|--------|-------------|-------|--------------|-------------|-----------|-----|-----------|----------|
| A | 256 | 3 | 0.1618 | 0.3210 | 0.7594 | 0.0919 | 0.1667 | 66 |
| B | 256 | 5 | 0.2359 | 0.3860 | 0.7420 | 0.1308 | 0.2200 | 89 |
| C | 512 | 3 | 0.2025 | 0.3903 | 0.7850 | 0.1166 | 0.2133 | 88 |
| D | 512 | 5 | 0.2321 | 0.4615 | 0.7796 | 0.1276 | 0.2333 | 98 |

**Chosen config for T17: Config D — 512-token chunks, top-5.** Both top-5 configs lead the top-3 ones. B and D are effectively tied on faithfulness (0.236 vs 0.232, within noise), but D is stronger across answer relevancy (0.462 vs 0.386), context precision (0.780 vs 0.742), numeric-EM (0.233 vs 0.220), and answers more questions (98 vs 89). We therefore carry D into the Mistral comparison (T17).

![T16 sweep chart](t16_sweep_chart.png)

_Overall finding: top-k = 5 clearly outperforms top-k = 3 on faithfulness and answer relevancy; chunk size matters less at top-5._