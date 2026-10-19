## Exasol scale and query measurements

Raw checks aggregate count and absolute gap, forcing evaluation. Optimised queries use a batch-materialised monthly ledger, then run three sequential repetitions (median below, all samples in results.json). Query-result caching was disabled for the comparison. Data pages can be warm; neither cold-page control nor concurrency isolation was enforced. The cache build is reported separately and must rerun after every source update.

| Dataset | Factories | Raw evidence rows | CSV load seconds | Ledger refresh seconds |
|---|---:|---:|---:|---:|
| small | 2,400 | 228,854 | 2.069 | 0.324 |
| full | 220,000 | 20,978,945 | 56.423 | 16.263 |

| View | Small raw (s) | Small cached median (s) | Full raw (s) | Full cached median (s) |
|---|---:|---:|---:|---:|
| V_MATERIAL_OUTPUT | 0.296 | 0.022 | 14.174 | 0.413 |
| V_DISPATCH_INVOICE | 0.276 | 0.021 | 27.609 | 0.286 |
| V_STOCK_ROLLFORWARD | 0.274 | 0.020 | 32.376 | 0.281 |
| V_SUPPLIER_LOOP | 0.275 | 0.020 | 29.851 | 0.305 |
| V_RANKED_CASES | 0.317 | 0.099 | 48.946 | 6.141 |

### pandas comparison

The two slowest individual checks in each raw SQL run are reproduced in pandas using the same CSVs, threshold, aggregation and gap checksum. CSV read time and computation time are separate. pandas uses host memory; Exasol runs in a local VM and raw SQL also resolves the shared ledger. This is a single-machine workload comparison, not an engine superiority claim. pandas is faster on some checks.

| Dataset / check | CSV read (s) | pandas compute (s) | pandas total (s) | Exasol raw (s) |
|---|---:|---:|---:|---:|
| small / V_MATERIAL_OUTPUT | 0.024 | 0.002 | 0.026 | 0.296 |
| small / V_DISPATCH_INVOICE | 0.055 | 0.024 | 0.078 | 0.276 |
| full / V_STOCK_ROLLFORWARD | 1.906 | 0.381 | 2.287 | 32.376 |
| full / V_SUPPLIER_LOOP | 2.102 | 1.402 | 3.504 | 29.851 |

### Profile and optimisation

Saved session profiles: [small](reports/profile_small.json), [full](reports/profile_full.json). The profile exposes repeated grouping, joining and sorting through the shared ledger. Materialising that ledger once amortises this work across the six signals and case ranking. Counts and absolute-gap checksums are asserted unchanged before reporting any timings. [Exasol profiling documentation](https://docs.exasol.com/db/latest/database_concepts/profiling.htm).

Window functions implement prior-closing continuity and a trailing power baseline. A historical-only median/MAD Python UDF is included in sql/30_baseline_udf.sql, but execution failed because this Exasol installation lacks a Python script-language container. It is optional, not used for flagging, and no UDF speedup is claimed.

### Why an in-memory analytic database

This workload repeatedly scans numeric evidence columns, groups shipments and payments by factory and period, joins independent ledgers, and evaluates window functions over annual histories. Exasol keeps these operations close to the primary data and makes the same SQL evidence available to scoring, the dashboard and guarded follow-ups. Batch materialisation makes repeated reads cheaper while preserving a traceable SQL path to raw evidence. The measured local VM results establish feasibility at this synthetic scale; they do not establish a speed advantage over every alternative or production latency.
