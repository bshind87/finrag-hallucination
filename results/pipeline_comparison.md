# Pipeline comparison: retrieval strategies (T14/T15/T18)

Three RAG configurations on FinanceBench (all 150 questions), identical except for retrieval: **Baseline** = sparse BM25; **Dense** = FAISS over MiniLM embeddings; **Enhanced** = LLM query rewrite + dense. Generator, query-rewriter, and RAGAS judge are GPT-3.5-turbo at temperature 0. Retr@3 = share of questions whose top-3 retrieval reached the correct filing.

| Pipeline | Retr@3 | Faithful. | Ans. Rel. | Ctx. Prec. | Answered | F1 |
|---|---|---|---|---|---|---|
| Baseline (BM25) | 43% | 0.102 | 0.211 | 0.534 | 47/150 | 0.083 |
| Dense (FAISS) | 64% | 0.179 | 0.393 | 0.770 | 82/150 | 0.116 |
| Enhanced (rewrite) | 69% | 0.184 | 0.418 | 0.843 | 87/150 | 0.121 |

## Interpretation

Holding the generator (GPT-3.5-turbo), prompt, chunks, and top-$k$ fixed, only \emph{retrieval} changes across the three pipelines, so the trend isolates the effect of retrieval quality. Retrieval accuracy climbs steadily: the correct filing reaches the top-3 for 43\% of questions under sparse BM25, 64\% under dense MiniLM retrieval, and 69\% once an LLM rewrites the query first. Because the generator is instructed to answer only from context, better retrieval directly lifts coverage: the model answers 47, 82, and 87 of 150 questions respectively, and token F1 rises from 0.083 to 0.116 to 0.121. RAGAS context precision moves the same way, confirming the gains come from putting the right chunk in front of the model rather than from changes in generation. Exact match stays near zero throughout because gold answers are short numeric values formatted many ways ($1,577 vs.\ 1577.00). The headline for RQ1 is that retrieval, not the generator, is the dominant lever on this benchmark: dense retrieval and query rewriting each add coverage, yet even the strongest configuration answers well under half the set, leaving a substantial gap---and a pool of answered-but-unsupported cases---for the error analysis to characterize.
