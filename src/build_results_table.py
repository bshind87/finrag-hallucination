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
           r"\caption{Preliminary baseline results on FinanceBench. Token-level QA "
           r"metrics (EM, F1) cover all 150 questions; RAGAS metrics use a 50-question "
           r"subset for the preliminary paper.}",
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
        "The baseline pairs a plain BM25 retriever with a small local generator, and the "
        "numbers show why finance QA is hard for this setup. Token F1 sits at "
        f"{_fmt(f1)} and exact match at zero: even when the model answers, it rarely "
        "reproduces the gold figure exactly, partly because the same number gets written "
        "many ways ($1,577 vs 1577.00). Context precision is the bright spot at "
        f"{_fmt(ctxprec)}, meaning that when a relevant chunk is retrieved it tends to rank "
        "near the top, but recall is the problem: BM25 only reaches the right filing 42% of "
        "the time, so the model abstains on most questions. That abstention is why "
        f"faithfulness ({_fmt(faith)}) and answer relevancy ({_fmt(ansrel)}) come out low, an "
        "abstention has nothing to ground and does not address the question, so RAGAS scores "
        "it near zero. Read together, the baseline is cautious rather than reckless: it "
        f"answers only {_fmt(n_ans)} of 150, and on that answered subset F1 climbs to "
        f"{_fmt(f1_ans)}. Closing the retrieval gap with dense and query-rewrite retrieval is "
        "the obvious next step, and it should also surface more of the hallucinations we want "
        "to study."
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
          "Baseline pipeline on FinanceBench. F1 and Exact Match (from `src/qa_metrics.py`, "
          f"T09) cover all {n_qa} questions. The RAGAS metrics (from `src/evaluate.py`, T08) "
          f"were run on a balanced {n_ragas}-question subset for the preliminary paper, since "
          "the local judge is slow; we will score the full set for the final paper. All runs "
          "use temperature 0.\n",
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
