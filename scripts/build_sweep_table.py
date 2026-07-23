"""Build the T16 hyperparameter-sweep comparison table + figure.

Reads per-row CSVs from evaluate.py (RAGAS) and qa_metrics.py (QA) for each of
the 4 sweep configs, aggregates means, writes a comparison table
(CSV + markdown + LaTeX) and a grouped bar chart. Files prefixed t16_ for easy
identification. No existing code is touched.
Run from repo root:  python scripts/build_sweep_table.py
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW = REPO_ROOT / "results" / "raw_outputs"
RESULTS = REPO_ROOT / "results"

CONFIGS = [
    ("A", 256, 3, "dense_256tok_top3"),
    ("B", 256, 5, "dense_256tok_top5"),
    ("C", 512, 3, "dense_512tok_top3"),
    ("D", 512, 5, "dense_512tok_top5"),
]


def load_config_metrics(stem: str) -> dict:
    ragas = pd.read_csv(RAW / f"{stem}_ragas_perrow.csv")
    qa = pd.read_csv(RAW / f"{stem}_qa_perrow.csv")
    out = {}
    for m in ("faithfulness", "answer_relevancy", "context_precision"):
        out[m] = round(float(ragas[m].dropna().mean()), 4) if m in ragas else None
    out["f1"] = round(float(qa["f1"].mean()), 4)
    out["em_numeric"] = round(float(qa["em_numeric"].mean()), 4)
    out["n_answered"] = int(len(qa[~qa["abstained"]]))
    return out


def make_chart(df: pd.DataFrame, path: Path) -> None:
    labels = [f"{r.config}\n{r.chunk_tokens}tok\ntop-{r.top_k}" for r in df.itertuples()]
    x = range(len(df))
    width = 0.38
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar([i - width / 2 for i in x], df["faithfulness"], width,
           label="Faithfulness", color="#3b6ea5")
    ax.bar([i + width / 2 for i in x], df["answer_relevancy"], width,
           label="Answer relevancy", color="#c26b3e")
    ax.set_ylabel("Score (0-1)")
    ax.set_title("T16 sweep: RAGAS metrics by config (dense pipeline, GPT-3.5)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_ylim(0, max(df["answer_relevancy"].max(), df["faithfulness"].max()) * 1.25)
    for i, v in enumerate(df["faithfulness"]):
        ax.text(i - width / 2, v + 0.01, f"{v:.2f}", ha="center", fontsize=8)
    for i, v in enumerate(df["answer_relevancy"]):
        ax.text(i + width / 2, v + 0.01, f"{v:.2f}", ha="center", fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main() -> int:
    rows = []
    for label, tok, k, stem in CONFIGS:
        m = load_config_metrics(stem)
        rows.append({
            "config": label, "chunk_tokens": tok, "top_k": k,
            "faithfulness": m["faithfulness"], "answer_relevancy": m["answer_relevancy"],
            "context_precision": m["context_precision"], "f1": m["f1"],
            "em_numeric": m["em_numeric"], "n_answered": m["n_answered"],
        })
    df = pd.DataFrame(rows)
    best_idx = df["faithfulness"].idxmax()
    best = df.loc[best_idx]

    df.to_csv(RESULTS / "t16_sweep_results.csv", index=False)

    md = ["# T16 Hyperparameter Sweep Results\n",
          "Dense (FAISS + MiniLM) pipeline, GPT-3.5-turbo generator, temperature 0.0, "
          "full 150-question FinanceBench set. RAGAS judge: GPT-3.5-turbo; embeddings: "
          "local MiniLM.\n",
          "| Config | Chunk (tok) | Top-k | Faithfulness | Answer Rel. | Ctx. Prec. | F1 | Numeric-EM | Answered |",
          "|--------|-------------|-------|--------------|-------------|-----------|-----|-----------|----------|"]
    for _, r in df.iterrows():
        md.append(f"| {r['config']} | {r['chunk_tokens']} | {r['top_k']} | "
                  f"{r['faithfulness']:.4f} | {r['answer_relevancy']:.4f} | "
                  f"{r['context_precision']:.4f} | {r['f1']:.4f} | "
                  f"{r['em_numeric']:.4f} | {r['n_answered']} |")
    md.append("")
    md.append(f"**Best config (by faithfulness):** Config {best['config']} "
              f"— {int(best['chunk_tokens'])}-token chunks, top-{int(best['top_k'])} "
              f"(faithfulness {best['faithfulness']:.4f}, F1 {best['f1']:.4f}, "
              f"answered {int(best['n_answered'])}/150).\n")
    md.append("![T16 sweep chart](t16_sweep_chart.png)\n")
    md.append("_Note: top-k = 5 outperforms top-k = 3 on faithfulness and answer "
              "relevancy across configs. The two top-5 configs (B and D) are close on "
              "faithfulness; the 256- vs 512-token choice is the main open decision and "
              "is worth confirming with the team before carrying one config into T17._")
    (RESULTS / "t16_sweep_results.md").write_text("\n".join(md), encoding="utf-8")

    tex = ["\\begin{table}[t]", "\\centering",
           "\\caption{Hyperparameter sweep: dense pipeline (GPT-3.5-turbo, "
           "150 questions). Best faithfulness in \\textbf{bold}.}", "\\label{tab:t16sweep}",
           "\\begin{tabular}{llrrrrrr}", "\\toprule",
           "Cfg & Chunk & $k$ & Faith. & Ans.Rel. & Ctx.Prec. & F1 & Num-EM \\\\", "\\midrule"]
    for _, r in df.iterrows():
        faith = (f"\\textbf{{{r['faithfulness']:.3f}}}" if r.name == best_idx
                 else f"{r['faithfulness']:.3f}")
        tex.append(f"{r['config']} & {r['chunk_tokens']} & {r['top_k']} & "
                   f"{faith} & {r['answer_relevancy']:.3f} & {r['context_precision']:.3f} & "
                   f"{r['f1']:.3f} & {r['em_numeric']:.3f} \\\\")
    tex += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    (RESULTS / "t16_sweep_table.tex").write_text("\n".join(tex), encoding="utf-8")

    make_chart(df, RESULTS / "t16_sweep_chart.png")

    print(df.to_string(index=False))
    print(f"\nBest config by faithfulness: {best['config']} "
          f"({int(best['chunk_tokens'])} tok, top-{int(best['top_k'])})")
    print("\nwrote: results/t16_sweep_results.csv")
    print("wrote: results/t16_sweep_results.md")
    print("wrote: results/t16_sweep_table.tex")
    print("wrote: results/t16_sweep_chart.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
