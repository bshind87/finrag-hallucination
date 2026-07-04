# Preliminary Paper

**Analyzing Hallucination Patterns in RAG-Based Financial Question Answering** —
CS6120 NLP preliminary report (M2, due 2026-07-03).

## Files
- `main.docx` — **Word version of the paper** (ACL 2023 Word template styles, citations
  resolved, Figure 1 embedded). Generated from `main.md`. Open/edit/submit directly.
- `main.md` — Markdown source for the Word build (edit this, then regenerate `main.docx`).
- `main.tex` — the paper (ACL 2023 LaTeX template, ~4-page body + refs + appendix).
- `references.bib` — 24 references, grouped by theme (RAG methods / hallucination
  detection / financial NLP). Verify author lists + pages before final submit.
- `results_table.tex` — auto-generated baseline results table (from
  `src/build_results_table.py`); `\input` by `main.tex`.
- `fig_eda_overview.png` — Figure 1 (from `notebooks/01_eda.ipynb`).
- `acl2023.sty`, `acl_natbib.bst` — the provided ACL 2023 template files (also in
  `templates/acl2023/`), copied here so the folder compiles standalone.
- `litreview_notes/` — per-member study notes feeding the related-work section.
- `templates/` — the instructor-provided ACL 2023 template (LaTeX + Word).

## Build (Word — recommended if LaTeX is giving trouble)
Regenerate `main.docx` from `main.md` with the ACL Word template applied:
```bash
pandoc main.md --citeproc --bibliography=references.bib \
  --reference-doc=templates/acl2023.docx -o main.docx
```
Then open `main.docx` in Word, adjust to two-column / final formatting as needed, and submit.

## Build (LaTeX)
Compiles cleanly with the provided template (verified locally, 5 pages total:
~4-page body + references + a short appendix, within the "4 pages excluding
references/appendices" limit). On Overleaf, create a project from the ACL 2023
template and add `main.tex` + `references.bib` + `results_table.tex` +
`fig_eda_overview.png`; or locally:

```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

## Before submitting — checklist
- [ ] Fill in Member 3 / Member 4 names + emails (author block + contributions footnote).
- [ ] Members 3/4 add their assigned related-work paper summaries (5–6 papers each).
- [ ] Full-group proofread; confirm ≤4-page body.
- [ ] Confirm this ACL 2023 template is the one the instructor requires (a Word
      version is in `templates/acl2023.docx` if Word is required instead).
- [ ] Submit per course instructions before 2026-07-03.
