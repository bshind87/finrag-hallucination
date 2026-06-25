# Project Plan & Task Board — RAG Hallucination in Financial QA

**Course:** CS6120 NLP (Northeastern University) · **Group size:** 4
**Project:** Analyzing Hallucination Patterns in RAG-Based Financial Question Answering
**Plan owner doc:** keep this file updated as the single source of truth.

> **How to use this document**
> - This is a **task board**, not a role assignment. Tasks are written so any member can **pick up one task at a time**, top to bottom.
> - Before starting a task, set its **Status → In Progress** and put your name in **Owner**. When done, set **Status → Done** and tick the acceptance criteria.
> - **Respect dependencies.** A task is only "pickable" once everything in its *Dependencies* line is Done.
> - Each task has: number, title, description, subtasks, dependencies, acceptance criteria, and an estimate.
> - Status legend: `TODO` · `IN PROGRESS` · `BLOCKED` · `DONE`

---

## 1. Timeline & Milestones

| Milestone | Deadline | Status | Gating tasks (must be DONE) |
|-----------|----------|--------|-----------------------------|
| M0 — Group registration | 2026-06-05 | ✅ Done | — |
| M1 — Project proposal | 2026-06-16 | ✅ Done | — |
| **M2 — Preliminary Paper (4 pages)** | **2026-07-03** | ⏳ ~2 weeks left | T01–T13 |
| **M3 — Final Paper (8 pages)** | **2026-07-31** | ⏳ | T14–T28 |
| **M4 — Presentation + Poster** | **2026-08-04** | ⏳ | T29–T33 |

### Suggested internal cadence (buffer before each hard deadline)
| Window | Focus | Target by end of window |
|--------|-------|--------------------------|
| 6/19 – 6/22 | Setup & data (Phase 1) | T01–T05 done |
| 6/23 – 6/27 | Baseline pipeline + eval harness (Phase 2/3 subset) | T06–T10 done |
| 6/28 – 7/01 | Lit review + draft prelim paper | T11–T13 in progress |
| **7/02** | **Internal freeze for prelim paper** | T13 done, 1 day buffer |
| 7/04 – 7/12 | Dense + Enhanced RAG, Mistral, full eval | T14–T19 |
| 7/13 – 7/20 | Error analysis + taxonomy + (optional) classifier | T20–T24 |
| 7/21 – 7/28 | Full results, figures, write final paper | T25–T28 |
| **7/30** | **Internal freeze for final paper** | T28 done, 1 day buffer |
| 8/01 – 8/03 | Poster + video | T29–T32 |
| **8/04** | Submit / present | T33 |

> **Reality check on dates:** Today is 6/19. The proposal timeline assumed setup happened in Week 2 (6/13–6/19). If setup hasn't started yet, prioritize T01–T06 immediately — the preliminary paper depends on a working baseline pipeline.

---

## 1.5 Progress Tracker (single source of truth for reviews)

**Repo:** https://github.com/bshind87/finrag-hallucination (private)

> 🔎 **The professor reviews progress every alternate week.** This table is the at-a-glance
> view for those reviews. **Keep it current** — update your task's row the moment you start,
> finish, or get blocked. The detailed task blocks below hold the full description + acceptance
> criteria; this table holds who/what/when.

**Rules that make attribution clean:**
1. **Commit under your own GitHub account** — `git`/PR history is the audit trail of who did what. Don't push someone else's work under your name.
2. **One task → one branch → one PR**, named `feature/<task-id>-short-name` (e.g. `feature/T06-baseline-rag`). The merged PR link is the proof a task is done.
3. When you **start**: set Status → `IN PROGRESS`, put your name in Owner, fill **Started**.
4. When you **finish**: set Status → `DONE`, fill **PR #** and **Done date**, tick the task's acceptance criteria below.
5. If **blocked**, set Status → `BLOCKED` and note what's blocking in the row.

| Task | Title | Owner | Status | Branch / PR # | Started | Done |
|------|-------|-------|--------|---------------|---------|------|
| **M2 — Preliminary Paper (due 2026-07-03)** | | | | | | |
| T01 | Shared repo & structure | Bhalchandra | IN PROGRESS | repo live (`bshind87/finrag-hallucination`, private), structure + .gitignore + README + branch/PR convention done (`5314fa7`); **pending: add 3 teammates as collaborators (need usernames)** | 2026-06-19 | |
| T02 | Python env & dependencies | Bhalchandra | DONE | clean install verified on Python 3.12 (`requirements.txt`, all imports OK); SETUP.md + check_setup.py + Colab template committed. Per-member key: each runs `check_setup.py` (own key). | 2026-06-19 | 2026-06-23 |
| T03 | Load & explore FinanceBench | Bhalchandra | DONE | ran `src/download_data.py`: 150 QA records + 84 PDFs (161 MB, 0 failed); QA↔doc-info merge → 150 rows verified; schema note in `data/README.md` | 2026-06-19 | 2026-06-23 |
| T04 | Exploratory Data Analysis | Bhalchandra | DONE | `notebooks/01_eda.ipynb` (10-part EDA) + 22 figures + `results/eda_summary.md` | 2026-06-23 | 2026-06-24 |
| T05 | Preprocessing & chunking | _____ | TODO | | | |
| T06 | Pipeline 1: Baseline RAG (BM25) | _____ | TODO | | | |
| T07 | Freeze output schema + run config | _____ | TODO | | | |
| T08 | RAGAS eval harness (baseline) | _____ | TODO | | | |
| T09 | QA metrics (F1 + EM) | _____ | TODO | | | |
| T10 | Preliminary results table | _____ | TODO | | | |
| T11 | Expand related work (20–24 papers) | _____ | TODO | | | |
| T12 | Paper template & scaffold | _____ | TODO | | | |
| T13 | Write & submit prelim paper | _____ | TODO | | | |
| **M3 — Final Paper (due 2026-07-31)** | | | | | | |
| T14 | Pipeline 2: Dense RAG (FAISS) | _____ | TODO | | | |
| T15 | Pipeline 3: Enhanced RAG (rewrite) | _____ | TODO | | | |
| T16 | Hyperparameter sweeps | _____ | TODO | | | |
| T17 | Mistral-7B alternate generator | _____ | TODO | | | |
| T18 | Full evaluation (all combos) | _____ | TODO | | | |
| T19 | Identify failure cases | _____ | TODO | | | |
| T20 | Annotation schema & taxonomy | _____ | TODO | | | |
| T21 | Annotate 50 failure cases | _____ | TODO | | | |
| T22 | Hallucination-type frequency + figure | _____ | TODO | | | |
| T23 | Curate qualitative case studies | _____ | TODO | | | |
| T24 | (Optional) RoBERTa classifier | _____ | TODO | | | |
| T25 | Assemble final tables & figures | _____ | TODO | | | |
| T26 | Expand related work (final) | _____ | TODO | | | |
| T27 | Write final paper (8 pages) | _____ | TODO | | | |
| T28 | Final review & submission | _____ | TODO | | | |
| **M4 — Presentation + Poster (due 2026-08-04)** | | | | | | |
| T29 | Design poster | _____ | TODO | | | |
| T30 | Build presentation slides | _____ | TODO | | | |
| T31 | Record video (≤8 min) | _____ | TODO | | | |
| T32 | Submit poster + video | _____ | TODO | | | |
| T33 | (Bonus) ACL workshop submission | _____ | TODO | | | |

### Bi-weekly checkpoint log (fill before each professor review)
| Review date | Milestone window | Completed since last review | Owners | Blockers / risks |
|-------------|------------------|-----------------------------|--------|------------------|
| 2026-06-24 | M1 done → M2 setup | M1 proposal submitted (6/16); **T02, T03, T04 DONE** — verified Python 3.12 env, FinanceBench data downloaded (150 records + 84 PDFs), and comprehensive EDA (notebook + 22 figures + summary). **T01 IN PROGRESS** — repo/structure/conventions done, collaborator invites pending. | Bhalchandra | Need 3 teammates' GitHub usernames to add as collaborators (closes T01); working OpenAI API key + credits to confirm (closes T02 fully for runs) |
| | M2 setup → baseline | _(next review — target T05, T06, T07 done; prelim paper draft started)_ | | |

---

## 2. Definition of Done (applies to every task)
- Code is committed to the shared GitHub repo on a branch and merged via PR (reviewed by ≥1 other member).
- Any produced artifact (data file, notebook, table, figure) is saved to the agreed repo location, not only on a local machine.
- The task's specific acceptance criteria are all checked.
- This document is updated (Status + Owner).

---

# Phase 1 — Setup & Data Preparation  *(gates M2)*

### T01 — Create shared GitHub repo & project structure
- **Status:** IN PROGRESS  · **Owner:** Bhalchandra  · **Est:** 0.5 day
- **Description:** Stand up the shared repository all four members will work in, with a sensible folder layout and collaboration rules.
- **Repo:** https://github.com/bshind87/finrag-hallucination (private, owner `bshind87`).
- **Subtasks:**
  - [x] Create one repo; ~~add all 4 members as collaborators~~ — repo created (private); **3 teammates still to be added as collaborators (awaiting their GitHub usernames).**
  - [x] Add folders: `/data` (raw + processed), `/src` (pipeline code), `/notebooks`, `/results`, `/paper`, `/annotations`.
  - [x] Add `.gitignore` (ignores `.env`, `__pycache__`, large data/PDFs, indices, model checkpoints, `results/raw_outputs/`).
  - [x] Add a `README.md` with project summary + setup instructions, linking this `PROJECT_PLAN.md` (plus `SETUP.md` for env + per-member API keys).
  - [x] Agree on a branch + PR workflow (`feature/<task-id>-name` → PR → review ≥1 member → merge) — documented in README "Contributing workflow".
- **Dependencies:** none (start here).
- **Acceptance criteria:**
  - [ ] All 4 members can clone and push. *(Owner can; pending: invite the 3 teammates via repo Settings → Collaborators once usernames are shared, and they accept.)*
  - [x] Folder structure + `.gitignore` + `README.md` committed. *(initial commit `5314fa7`.)*
  - [x] Branch/PR convention written in README. *(README "Contributing workflow" + Progress Tracker rules above.)*
- **Remaining to close T01:** collect the 3 teammates' GitHub usernames → add as collaborators → they accept the invite → flip Status to DONE.

### T02 — Python environment & dependency setup
- **Status:** DONE  · **Owner:** Bhalchandra  · **Est:** 0.5 day
- **Description:** Reproducible environment so every member runs the same stack.
- **Subtasks:**
  - Create a virtualenv/conda env; pin a `requirements.txt` with: `langchain`, `faiss-cpu`, `sentence-transformers`, `openai`, `ragas`, `transformers`, `pandas`, `datasets`, `rank_bm25`, `pymupdf` (or `pdfplumber`), `python-dotenv`.
  - Provide a `.env.example` (keys named, no secrets) and document storing the **OpenAI API key** in `.env` (never committed).
  - Verify `import` of all key libs runs clean.
  - Set up a Google Colab notebook template linked to the repo for GPU runs (needed later for Mistral/RoBERTa).
- **Dependencies:** T01.
- **Note:** use **Python 3.12** for the env — the pinned versions (`numpy<2.0`, `faiss-cpu`, `torch`) lack Python 3.13 wheels. See [SETUP.md](SETUP.md).
- **Acceptance criteria:**
  - [x] `pip install -r requirements.txt` succeeds on a clean env. *(verified on a fresh Python 3.12 venv; all key libs import OK.)*
  - [x] `.env.example` committed; real `.env` gitignored.
  - [x] A "hello world" OpenAI API call works for at least one member (key valid, billing/credits confirmed). *(per-member: each runs `python src/check_setup.py` with their own key — `.env` is not shared/committed.)*
  - [x] Colab template notebook committed. *(`notebooks/colab_gpu_template.ipynb`.)*

### T03 — Load & explore FinanceBench
- **Status:** DONE  · **Owner:** Bhalchandra  · **Est:** 1 day
- **Description:** Load the 150-example open-source FinanceBench set and understand its structure.
- **Subtasks:**
  - Download dataset from HuggingFace `PatronusAI/financebench`.
  - Load `financebench_open_source.jsonl` and `financebench_document_information.jsonl`; merge on `doc_name`.
  - Inspect fields: question, gold answer, evidence string, doc type (10-K/10-Q/8-K), company.
  - Download source PDFs from the GitHub `/pdfs/` folder.
- **Dependencies:** T02.
- **Result:** `python src/download_data.py` → 150 QA records + 84 source PDFs (161 MB, 0 failed). Merge on `doc_name` → 150 rows. Coverage: 32 companies; doc types 10-K (112), 10-Q (15), Earnings (14), 8-K (9). *(Data is gitignored — each member re-runs the script locally.)*
- **Acceptance criteria:**
  - [x] Merged dataframe of 150 examples loads in a notebook. *(merge verified; 150 rows.)*
  - [x] PDFs downloaded and stored under `/data`. *(84 PDFs under `data/pdfs/`.)*
  - [x] Short markdown note on dataset schema committed. *([data/README.md](data/README.md) documents fields + sources.)*

### T04 — Exploratory Data Analysis (EDA)
- **Status:** DONE  · **Owner:** Bhalchandra  · **Est:** 1 day
- **Description:** Produce the EDA that feeds the preliminary paper's data section and its first figure.
- **Subtasks:**
  - Distributions: question types, companies, doc types (10-K/10-Q/8-K), answer categories, answer lengths.
  - Produce at least one publication-quality figure (e.g. question-type distribution).
  - Write 1–2 paragraphs summarizing findings.
- **Dependencies:** T03.
- **Acceptance criteria:**
  - [x] EDA notebook committed under `/notebooks`. *(`notebooks/01_eda.ipynb`, executed; 10-part analysis: dataset overview, question/answer/evidence/source-doc/company analysis, retrieval-difficulty + hallucination-risk proxies, linguistic complexity, data-quality checks.)*
  - [x] ≥1 saved figure under `/results` usable in the paper. *(22 figures incl. `fig_eda_overview.png` — Figure 1 candidate — plus hallucination-risk, extractability CDF, company×year heatmap, evidence-depth scatter, wordcloud.)*
  - [x] Written EDA summary drafted for the paper's data section. *(`results/eda_summary.md`.)*
- **Key finding:** answers are ~98% non-verbatim (abstractive/computed), evidence is 69% table-heavy over ~128-page filings, median Q↔evidence cosine 0.47 — i.e. high grounded-but-wrong hallucination risk. (Added EDA deps `wordcloud`, `textstat` to `requirements.txt`; rerun `pip install -r requirements.txt`.)

### T05 — Document preprocessing & chunking
- **Status:** TODO  · **Owner:** _____  · **Est:** 1.5 days
- **Description:** Turn source PDFs into reusable, metadata-tagged chunks for retrieval.
- **Subtasks:**
  - Extract text from each PDF via `PyMuPDF` or `pdfplumber`.
  - Implement two chunking strategies: fixed-size (512 tokens) and sentence-aware.
  - Attach metadata to each chunk: company, doc type, page number, chunk ID.
  - Serialize chunks to disk (e.g. parquet/JSONL) so runs don't re-process PDFs.
- **Dependencies:** T03.
- **Acceptance criteria:**
  - [ ] Chunk files for both strategies saved under `/data/processed`.
  - [ ] Each chunk carries full metadata.
  - [ ] A loader function returns chunks without re-parsing PDFs.

---

# Phase 2 — Build RAG Pipelines  *(T06 gates M2; T14–T17 gate M3)*

### T06 — Pipeline 1: Baseline RAG (BM25 + GPT-3.5-turbo)
- **Status:** TODO  · **Owner:** _____  · **Est:** 2 days
- **Description:** The minimal end-to-end RAG needed for preliminary results. This is the critical path for M2.
- **Subtasks:**
  - Index chunks with `rank_bm25`.
  - For each question: retrieve top-3 chunks → GPT-3.5-turbo with the fixed prompt template ("Answer using only the provided context…").
  - Set temperature 0.0 for deterministic eval.
  - Save outputs in a standard schema: `question, retrieved_chunks, generated_answer, gold_answer, doc_name, question_type`.
- **Dependencies:** T05.
- **Acceptance criteria:**
  - [ ] Runs over all 150 examples without crashing.
  - [ ] Output file saved under `/results` in the standard schema.
  - [ ] Standard output schema documented (reused by all later pipelines + eval).

### T07 — Define & freeze the shared output schema + run config
- **Status:** TODO  · **Owner:** _____  · **Est:** 0.5 day
- **Description:** Lock the data contract so every pipeline and the evaluation code interoperate. (Do this alongside T06.)
- **Subtasks:**
  - Document the output JSON/CSV schema, including which fields RAGAS needs (question, answer, contexts, ground_truth).
  - Document run config: chunk size, top-k, temperature, model name, retrieval type — recorded per run for the results table.
- **Dependencies:** T06 (or in parallel).
- **Acceptance criteria:**
  - [ ] Schema + config doc committed under `/src` or `/results`.
  - [ ] T06 output conforms to it.

---

# Phase 3 — Evaluation  *(baseline subset gates M2; full eval gates M3)*

### T08 — RAGAS evaluation harness (baseline)
- **Status:** TODO  · **Owner:** _____  · **Est:** 1.5 days
- **Description:** Reusable evaluation that takes a pipeline output file and returns RAGAS metrics.
- **Subtasks:**
  - Configure RAGAS; compute faithfulness, answer relevancy, context precision.
  - Output mean ± std across the 150 examples.
  - Build a results DataFrame: `pipeline, model, faithfulness, answer_relevancy, context_precision`.
  - Run it on the T06 baseline output.
- **Dependencies:** T06, T07.
- **Acceptance criteria:**
  - [ ] One function/script evaluates any conformant output file.
  - [ ] Baseline RAGAS scores (mean ± std) saved under `/results`.

### T09 — Standard QA metrics (F1 + Exact Match)
- **Status:** TODO  · **Owner:** _____  · **Est:** 1 day
- **Description:** SQuAD-style token-level F1 and EM vs gold answers, complementing RAGAS.
- **Subtasks:**
  - Implement token-level F1 and EM with standard normalization.
  - Add scores to the results DataFrame alongside RAGAS.
  - Note the "grounded but wrong" case (high faithfulness, low F1) for the analysis section.
- **Dependencies:** T06, T07.
- **Acceptance criteria:**
  - [ ] F1/EM computed for the baseline run.
  - [ ] Combined results table (RAGAS + F1 + EM) saved under `/results`.

### T10 — Preliminary results table (baseline only)
- **Status:** TODO  · **Owner:** _____  · **Est:** 0.5 day
- **Description:** First real results artifact for the preliminary paper.
- **Subtasks:**
  - Assemble baseline metrics into a clean, paper-ready table.
  - Write 1 paragraph interpreting the numbers.
- **Dependencies:** T08, T09.
- **Acceptance criteria:**
  - [ ] Formatted table exported (LaTeX/markdown) under `/results`.
  - [ ] Interpretation paragraph drafted.

---

# Phase 5a — Literature Review & Preliminary Paper  *(gates M2)*

### T11 — Expand related work to 20–24 papers
- **Status:** TODO  · **Owner:** _____  · **Est:** 2 days (split reading across members)
- **Description:** Grow the 8 proposal papers to 20–24, grouped by theme (RAG methods, hallucination detection, financial NLP).
- **Subtasks:**
  - Identify 12–16 additional relevant papers (cite recent RAG-hallucination + financial QA work).
  - Each member writes 2–4 sentence summaries for their assigned papers.
  - Maintain a shared BibTeX/`.bib` file.
- **Dependencies:** none (can run in parallel with Phase 1–3).
- **Acceptance criteria:**
  - [ ] ≥20 papers in the `.bib` file with summaries.
  - [ ] Papers grouped by the three themes.

### T12 — Choose paper template & scaffold preliminary paper
- **Status:** TODO  · **Owner:** _____  · **Est:** 0.5 day
- **Description:** Set up the writing environment with the **instructor-provided template** (wrong template = zero).
- **Subtasks:**
  - Confirm required template (LaTeX vs Word) from course materials.
  - Create the 4-page skeleton: intro, related work, data + EDA, preliminary results.
  - Set up shared editing (Overleaf or repo `/paper`).
- **Dependencies:** none.
- **Acceptance criteria:**
  - [ ] Correct template confirmed and in use.
  - [ ] Section skeleton with headings committed/shared.

### T13 — Write & submit the preliminary paper (4 pages)
- **Status:** TODO  · **Owner:** _____  · **Est:** 3 days (parallel writing)
- **Description:** The M2 deliverable, due **7/3**.
- **Subtasks:**
  - Introduction: motivate RAG hallucination in finance; state the 3 research questions.
  - Related work: 20–24 papers (from T11).
  - Data + EDA: dataset description and ≥1 figure (from T04).
  - Preliminary results: baseline pipeline table + interpretation (from T10).
  - Full-group proofread; verify page limit and template compliance.
  - Submit per course instructions.
- **Dependencies:** T04, T10, T11, T12.
- **Acceptance criteria:**
  - [ ] All four sections complete; ≥1 table + ≥1 figure included.
  - [ ] Within page limit, correct template.
  - [ ] **Submitted before 7/3.**

---

# Phase 2 (cont.) — Remaining RAG Pipelines  *(gates M3)*

### T14 — Pipeline 2: Dense RAG (FAISS + MiniLM + GPT-3.5-turbo)
- **Status:** TODO  · **Owner:** _____  · **Est:** 2 days
- **Description:** Semantic retrieval variant.
- **Subtasks:**
  - Embed chunks with `sentence-transformers/all-MiniLM-L6-v2`.
  - Build FAISS flat index (`IndexFlatL2`); retrieve top-3 by similarity.
  - Reuse the T06 prompt template + generator; save outputs in the standard schema.
  - Qualitatively compare retrieved chunks vs BM25.
- **Dependencies:** T05, T07.
- **Acceptance criteria:**
  - [ ] Dense pipeline runs over all 150 examples; output conforms to schema.
  - [ ] Short note comparing dense vs BM25 retrieval.

### T15 — Pipeline 3: Enhanced RAG (query rewriting + dense)
- **Status:** TODO  · **Owner:** _____  · **Est:** 2 days
- **Description:** Add an LLM query-rewriting step before dense retrieval.
- **Subtasks:**
  - Prompt GPT-3.5-turbo to rewrite/expand each question.
  - Retrieve from the same FAISS index using the rewritten query.
  - Save outputs in standard schema; log original vs rewritten query.
  - Compare retrieval quality vs Pipeline 2.
- **Dependencies:** T14.
- **Acceptance criteria:**
  - [ ] Enhanced pipeline runs over all 150 examples; schema-conformant output.
  - [ ] Rewrite examples logged; comparison note written.

### T16 — Hyperparameter sweeps
- **Status:** TODO  · **Owner:** _____  · **Est:** 1.5 days
- **Description:** Tune the key knobs called out in the proposal.
- **Subtasks:**
  - Vary chunk size (256 vs 512), top-k (3 vs 5); keep temperature 0.0 for eval.
  - Record each run's config + metrics.
  - Pick the best-performing retrieval config to carry into the Mistral comparison.
- **Dependencies:** T14, T15, T08, T09.
- **Acceptance criteria:**
  - [ ] Sweep results table saved.
  - [ ] Best config chosen and documented.

### T17 — Swap in Mistral-7B-Instruct as alternate generator
- **Status:** TODO  · **Owner:** _____  · **Est:** 2 days
- **Description:** Open-source generator comparison on the best retrieval config (Colab GPU).
- **Subtasks:**
  - Load `mistralai/Mistral-7B-Instruct-v0.2` with 4-bit quantization (`bitsandbytes`) on Colab.
  - Apply the best retrieval config (from T16); identical prompt template for fairness.
  - Save outputs in the standard schema.
- **Dependencies:** T16.
- **Acceptance criteria:**
  - [ ] Mistral run completes over the eval set; schema-conformant output.
  - [ ] Generation config documented (quantization, params).

---

# Phase 3 (cont.) — Full Evaluation  *(gates M3)*

### T18 — Full evaluation across all pipeline × model combos
- **Status:** TODO  · **Owner:** _____  · **Est:** 1.5 days
- **Description:** Run the T08/T09 harness over every pipeline and model.
- **Subtasks:**
  - Evaluate Pipelines 1–3 (GPT-3.5) + best-config Mistral.
  - Produce the consolidated main results DataFrame (RAGAS + F1 + EM).
- **Dependencies:** T08, T09, T14, T15, T17.
- **Acceptance criteria:**
  - [ ] Single consolidated results table covering all combinations.
  - [ ] Saved under `/results`.

### T19 — Identify failure cases for error analysis
- **Status:** TODO  · **Owner:** _____  · **Est:** 0.5 day
- **Description:** Select the hallucination candidates to annotate.
- **Subtasks:**
  - Filter outputs where faithfulness < 0.5 OR F1 = 0.
  - From the baseline pipeline, draw a **stratified sample of 50** across question types/companies.
- **Dependencies:** T18.
- **Acceptance criteria:**
  - [ ] 50-case sample exported under `/annotations`.
  - [ ] Sample documented as stratified (coverage shown).

---

# Phase 4 — Error Analysis & Hallucination Taxonomy  *(gates M3 — the novel contribution)*

### T20 — Finalize annotation schema & taxonomy guidelines
- **Status:** TODO  · **Owner:** _____  · **Est:** 0.5 day
- **Description:** Lock the 4-category taxonomy and labeling rules before annotating.
- **Subtasks:**
  - Document categories: **numerical**, **entity**, **reasoning**, **unsupported extrapolation** — each with a definition + example.
  - Define the annotation sheet columns and the 10 shared cases for agreement.
- **Dependencies:** T19.
- **Acceptance criteria:**
  - [ ] Taxonomy + guidelines doc committed.
  - [ ] Annotation template (sheet) ready.

### T21 — Manual annotation of 50 failure cases
- **Status:** TODO  · **Owner:** _____  · **Est:** 1.5 days (split: ~12–13 cases/member)
- **Description:** Each member labels their share; 10 cases double-annotated for agreement.
- **Subtasks:**
  - For each case: read question, retrieved chunks, generated answer, gold answer; assign one label.
  - Compute inter-annotator agreement (Cohen's kappa) on the 10 shared cases.
- **Dependencies:** T20.
- **Acceptance criteria:**
  - [ ] All 50 cases labeled.
  - [ ] Cohen's kappa reported.
  - [ ] Disagreements resolved/adjudicated.

### T22 — Hallucination-type frequency analysis + figure
- **Status:** TODO  · **Owner:** _____  · **Est:** 0.5 day
- **Description:** Quantify and visualize the taxonomy distribution.
- **Subtasks:**
  - Compute frequency of each hallucination type.
  - Produce the bar chart (Figure 1 in the paper).
- **Dependencies:** T21.
- **Acceptance criteria:**
  - [ ] Frequency table + bar chart saved under `/results`.

### T23 — Curate qualitative case-study examples
- **Status:** TODO  · **Owner:** _____  · **Est:** 0.5 day
- **Description:** Pick 2–3 illustrative examples per hallucination type for the paper.
- **Subtasks:**
  - Select clear examples (question, generated answer, gold, label).
  - Format as a case-study table (Table 2).
- **Dependencies:** T21.
- **Acceptance criteria:**
  - [ ] Case-study table with 2–3 examples per category.

### T24 — (Optional) RoBERTa hallucination classifier
- **Status:** TODO  · **Owner:** _____  · **Est:** 2 days
- **Description:** Train an automatic hallucinated-vs-grounded classifier; evaluate against human labels.
- **Subtasks:**
  - Use RAGTruth (`wandb/RAGTruth`) as training supervision.
  - Fine-tune `roberta-base` (input: retrieved context + generated answer).
  - Evaluate on the 50 annotated FinanceBench cases; report precision/recall/F1.
  - Produce confusion matrix (Figure 2, optional).
- **Dependencies:** T21.
- **Acceptance criteria:**
  - [ ] Trained classifier + eval metrics saved.
  - [ ] Confusion matrix figure produced.
  - [ ] *(Skip if time-constrained — clearly mark as not done so the paper doesn't claim it.)*

---

# Phase 5b — Final Paper  *(gates M3, due 7/31)*

### T25 — Assemble all final tables & figures
- **Status:** TODO  · **Owner:** _____  · **Est:** 1 day
- **Description:** Gather every results artifact into final, paper-ready form.
- **Subtasks:**
  - Table 1: main results (all pipeline × model, RAGAS + F1/EM).
  - Figure 1: hallucination-type frequencies.
  - Table 2: qualitative examples.
  - Figure 2 (optional): classifier confusion matrix.
- **Dependencies:** T18, T22, T23, (T24 optional).
- **Acceptance criteria:**
  - [ ] All tables/figures finalized and captioned.

### T26 — Expand related work for final paper
- **Status:** TODO  · **Owner:** _____  · **Est:** 1 day
- **Description:** Ensure 20–24 papers are well-synthesized (not just listed), grouped by theme.
- **Dependencies:** T11.
- **Acceptance criteria:**
  - [ ] Related-work section reads as synthesis, grouped by theme.

### T27 — Write the final paper (8 pages)
- **Status:** TODO  · **Owner:** _____  · **Est:** 4 days (parallel)
- **Description:** Full paper: abstract, intro, related work, methodology, results, analysis, conclusions + future work.
- **Subtasks:**
  - Abstract (problem, approach, key findings).
  - Methodology: all 3 pipelines, eval setup, annotation process.
  - Results + Analysis: tables/figures from T25 + qualitative discussion.
  - Conclusions + future work (e.g. full 10K-example dataset).
- **Dependencies:** T25, T26.
- **Acceptance criteria:**
  - [ ] All sections drafted; figures/tables embedded.
  - [ ] Within 8 pages, correct template.

### T28 — Final paper review & submission
- **Status:** TODO  · **Owner:** _____  · **Est:** 1 day
- **Description:** Polish and submit the M3 deliverable.
- **Subtasks:**
  - Full-group proofread; check citations, page limit, template.
  - Submit per course instructions.
- **Dependencies:** T27.
- **Acceptance criteria:**
  - [ ] Proofread complete; references consistent.
  - [ ] **Submitted before 7/31.**

---

# Phase 6 — Presentation & Poster  *(gates M4, due 8/4)*

### T29 — Design the poster
- **Status:** TODO  · **Owner:** _____  · **Est:** 1.5 days
- **Description:** Visual poster following the standard flow.
- **Subtasks:**
  - Sections: motivation → research questions → pipeline diagram → results → taxonomy → conclusions.
  - Add QR code linking to the video + GitHub repo.
  - Keep text minimal (bullets over paragraphs).
- **Dependencies:** T28 (content finalized).
- **Acceptance criteria:**
  - [ ] Print-ready poster file.
  - [ ] QR code links verified.

### T30 — Build presentation slides
- **Status:** TODO  · **Owner:** _____  · **Est:** 1 day
- **Description:** Slide deck (reuse poster sections) for the video.
- **Dependencies:** T28.
- **Acceptance criteria:**
  - [ ] Deck covers intro → pipelines → results → analysis/conclusions.

### T31 — Record the video (max 8 minutes)
- **Status:** TODO  · **Owner:** _____  · **Est:** 1 day
- **Description:** Each member presents ~2 minutes on their section.
- **Subtasks:**
  - Record slides + talking head; practice timing.
  - Enforce hard 8-minute cutoff.
- **Dependencies:** T30.
- **Acceptance criteria:**
  - [ ] Final video ≤ 8:00.
  - [ ] All four members present.

### T32 — Final submission of poster + video
- **Status:** TODO  · **Owner:** _____  · **Est:** 0.5 day
- **Dependencies:** T29, T31.
- **Acceptance criteria:**
  - [ ] Poster + video submitted before **8/4**.

### T33 — (Bonus) ACL 2026 workshop submission
- **Status:** TODO  · **Owner:** _____  · **Est:** 1 day
- **Description:** Optional submission to "Towards Knowledgeable Foundation Models" for resume value.
- **Subtasks:**
  - Check workshop deadline; reformat to official ACL LaTeX style.
  - Submit via OpenReview.
- **Dependencies:** T28.
- **Acceptance criteria:**
  - [ ] Deadline checked; if viable, paper reformatted and submitted.

---

## 3. Critical Path (don't let these slip)
**For 7/3 (preliminary):** T01 → T02 → T03 → T05 → T06 → T08/T09 → T10 → T13 (with T04 + T11 + T12 in parallel).
**For 7/31 (final):** T14/T15 → T16 → T17 → T18 → T19 → T20 → T21 → T22/T23 → T25 → T27 → T28.
**For 8/4 (poster/video):** T28 → T29/T30 → T31 → T32.

## 4. Open Decisions / Risks
- [ ] **Template:** Confirm the instructor's exact paper template ASAP (T12) — wrong template = zero.
- [ ] **API budget:** $50 GCP credit + OpenAI cost — track spend; run full experiments at temperature 0.0 once, avoid re-runs.
- [ ] **Colab GPU:** Mistral (T17) and RoBERTa (T24) need GPU — confirm Colab access early.
- [ ] **RoBERTa classifier (T24) is optional** — drop first if the final-paper timeline is tight.
