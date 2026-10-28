# Judge audit — GST Evidence, 28 October 2026

**Review opinion:** a credible, inspectable synthetic reconciliation prototype with a clear officer-facing problem and strong presentation. It is not yet a complete submission because the required user-recorded demo video and final portal submission are outstanding. Real-taxpayer validation is absent. The most important technical finding was a deployed threshold mismatch; it was repaired with explicit user approval and verified against every V3-C monthly output.

This is a mock judge review by the coding assistant, not an official jury score, competition ranking or probability of winning. Evidence was read from code, SQL, local CSVs, artifacts, the live restricted database, the deck, website sources and GitHub. Provenance dates distinguish recorded runs from new checks.

## 1. Official rubric and provisional assessment

Official source: [Exasol event page](https://www.exasol.com/events/exathon-india-2026/), checked 28 October. Deadline: 31 October 2026, 11:59 pm IST. Solo entry is allowed. Public code, a permissive licence, a pitch deck, a short demo video, setup and run instructions are required. See SUBMISSION_CHECKLIST.md.


| Category | Maximum | Review estimate | Reason |
| --- | --- | --- | --- |
| Innovation / problem impact | 25 | 20 | Clear factory/officer pain and cross-source reconciliation. No field interviews, quantified officer benefit, or validated comparison with existing fraud platforms. |
| Effective use of Exasol Personal | 25 | 16 | Primary DB executes joins, windows and evidence/ranking SQL, with restricted follow-up queries. Fresh current full-scale evidence, UDF and MCP execution remain absent; DuckDB was faster in the recorded small comparison. |
| Technical excellence | 20 | 16 | Frozen splits, source-family rule, reproducible intervals, decoys and guards. Generator/verifier coupling and missing robustness/adversary measurements constrain trust. A serious live/offline threshold drift was caught and repaired. |
| Solution design / UX | 15 | 13 | Eight accessible static pages, three outcomes and source-linked results. Full officer queue workflow is an API, while public UI is a curated recorded explorer. |
| Documentation / reproducibility | 10 | 8 | Auditable metrics, compressed synthetic scoring inputs and clear commands. New author-machine clone scope must be stated; no second-machine proof. Required video remains an owner task. |
| Open-source quality | 5 | 4 | Public MIT source, CI, pinned dependencies and disclosed assistants; optional deck-authoring runtime is proprietary and not needed for the app. |
| Total | 100 | 77 | Conditional code/artifact review, not a completed-entry score. |


A judge should not award production accuracy, tax recovery, time savings or general database superiority from these results. A strong demo and candid answers could make the entry competitive; the audit cannot establish finalist or winning status without the other entries and official jury.

## 2. Findings, repairs and current evidence

Severity | Finding | Disposition
---|---|---
Critical | Schema default was 0.10, but published V3 threshold is 0.05. Live priorities were 2,837 instead of 3,775. | User approved a single SETTINGS update; no data/schema recreation. Loader now reads the frozen protocol; schema default fixed; API rejects mismatched source-family counts/status. See reports/threshold_repair.json.
High | Old deck, script and judge Q&A cited V2 metrics and K=4. | Current V3 files regenerated; old deck moved to legacy/submission/ with a do-not-submit label.
High | Audit scripts required ignored, unshipped CSVs. | Exact compressed synthetic A/B/C features and predictions published under data/audit/ with both compressed and original hashes; restore and CI commands added.
High | Prior clean-setup helper copied files without Git metadata, which current exporters need. | Replaced by a real local Git clone and isolated venv. Database loading is explicitly opt-in. Current result is reported separately from the older database reproduction.
Medium | make all ran only tests. | It now runs tests, evidence restoration, numeric audit, ablation replay and static export. It deliberately does not silently replace the database; make reproduce is the explicit loader path.
Medium | Claimed signal independence can be misunderstood. | Family grouping is implemented; causal independence is not established. The generator shares quantities and mechanisms across signals.
Medium | Loop tracing existed as context, not an independent loop trigger. | Marked implemented-as-context; general invoice-ring detection is not claimed.
Medium | Ranking exposure tie-breaker differs between SQL and frozen evaluator. | Source-family and weakest-link keys agree; exact monthly order diagnostics are in reports/ranking_alignment_audit.json. Published precision uses the frozen evaluator; no threshold/result was retuned.
Medium | Numeric note validation could be mistaken for complete semantic/legal validation. | Numeric membership and field binding are tested. Semantic truth, legal validity and external document authenticity are not validated.
Medium | Historical scale/robustness files and fresh results can be mixed up. | Current status register, artifact index and historical labels distinguish them.
Required owner action | No current user-recorded demo/video URL, and no final form submission. | Marked outstanding; no simulated recording or submission was created.

## 3. What the product does

The user is a GST officer reviewing manufacturing declarations. The prototype compares declared output, invoices and stock with power proxies, goods-movement records, supplier returns and bank flows. Exasol produces expected/observed/gap evidence. Monthly priority requires at least two source families. A factory queue requires enough prioritised months. Cases retain their source rows and a numeric-validated note for human review.

The problem statement remains verbatim and technology-free at the top of README and on the Problem page. Every dataset is synthetic. No real tax-system, power, transport or bank integration exists. “Cleared” is a prototype disposition under generated evidence; it is not legal clearance. The output is a review lead, not a fraud finding. No ML model decides flags.

## 4. Data inventory and origins

All current raw records originate in src/generate.py, not an external public dataset. A seeded random generator creates a factory-level scenario allocation, then twelve months of quantities and documents. Current A/B/C raw CSV header, count and SHA-256 inventories are in reports/dataset_inventory.json. The following table covers every generated dataset type:

| V3-C table | Records | Columns | Fields |
| --- | --- | --- | --- |
| factories | 2400 | 5 | factory_id, name, address, phone, vehicle_plate |
| suppliers | 2400 | 6 | supplier_id, name, address, phone, linked_factory_id, owner_factory_id |
| factory_month | 28800 | 12 | factory_id, period_month, product, opening_stock, purchases_kg, purchases_finished, declared_output, declared_dispatch, closing_stock, power_kwh, operating_hours, raw_stock_change |
| invoices | 28695 | 5 | invoice_id, factory_id, period_month, quantity, invoice_value |
| purchase_invoices | 28800 | 6 | purchase_invoice_id, buyer_factory_id, period_month, supplier_id, quantity, invoice_value |
| eway_bills | 57600 | 5 | eway_id, factory_id, period_month, quantity, vehicle_plate |
| supplier_returns | 27360 | 3 | supplier_id, period_month, declared_sales_kg |
| bank_entries | 57600 | 5 | transaction_id, factory_id, period_month, amount, direction |
| machines | 2560 | 4 | machine_id, factory_id, installed_month, rated_units_month |
| supporting_documents | 12590 | 6 | document_id, factory_id, period_month, document_type, verification_status, verified_by |
| truth | 28800 | 9 | factory_id, period_month, is_cheat, scenario, intensity, evasive, discrepancy_class, explanation, taxpayer_explanation |

| Dataset | Role | Seed | Factories | Months | Raw evidence rows |
| --- | --- | --- | --- | --- | --- |
| v3_a | calibration DEV | 51001 | 2400 | 12 | 241479 |
| v3_b | primary HELDOUT | 51002 | 2400 | 12 | 241492 |
| v3_c | confirmation HELDOUT | 51003 | 2400 | 12 | 241445 |


Feature exports contain six check rows per factory-month. Factory truth/scenario/intensity/evasive labels are evaluator-only. The compressed artifacts contain feature exports and scoring predictions, not all raw files; raw tables can be regenerated from the seeded generator. No database image, venv, credentials or employer data is uploaded.

Generator design: 30% of factories are assigned cheat scenarios, 40% honest-decoy scenarios and 30% ordinary honest scenarios. Cheat types are distributed by the scenario list; intensities are sampled from 5%, 15% and 30%, and approximately one quarter are designated evasive. Each cheat has a random subset of active months in April–December; January–March have no active cheats. Inactive months from cheat factories are honest months in monthly scoring. Distributions and exact active counts by period are in the inventory.

Honest decoys: machinery upgrade, product-mix shift, longer hours, seasonal stock build, supplier onboarding and lumpy bank flows. Ordinary multiplicative noise, occasional larger measurement errors and optional missing documents affect evidence. Supporting verification statuses come from generator scenario knowledge. Forged explanations are rejected by that simulated metadata; sophisticated forgers are not tested.

Synthetic addresses, phone strings and vehicle identifiers are formatting examples. No real contact or vehicle lookup is performed. Entity normalisation uses SQL string operations, not a validated identity-resolution model. Machines support documented-change context; actual capacity detection is stretch work.

## 5. Inputs, formulas and thresholds

Quantities are synthetic kg; power is kWh; operating time is hours; currency is INR. Assumptions of 80% material yield, 4 kWh/kg, INR 120/kg sales, INR 90/kg purchases and a toy 18% exposure multiplier are generator/check assumptions, not industry estimates or verified tax liabilities. Different products, inventory stages and lawful tax rates are not modelled comprehensively.

Check | Family | Calculation / purpose
---|---|---
material_output | production | Expected output = purchases_kg × 0.8; observed = declared_output. Severity is the maximum relative discrepancy from material and power_kWh/4.
dispatch_invoice | movement | Expected dispatch quantity minus invoiced quantity; severity is max(relative quantity gap, reused e-way-ID fraction). Missing invoice records are classified separately.
stock_rollforward | production | Expected closing = opening + finished purchases + declared output − declared dispatch. Severity also checks prior closing via LAG, with documented raw-stock-change tolerance.
supplier_chain | supplier | Purchase quantity versus supplier-declared sales. A three-party linked-factory cycle is included as context; cycle presence does not independently enter severity.
bank_sales | financial | Bank receipts minus invoice value, normalised by the larger value or one.
bank_purchases | financial | Bank payments minus purchase value, similarly normalised.

A row fires when severity is strictly greater than 0.05. Both material and stock belong to production; sales and purchase bank checks belong to financial. Taking the maximum severity within a family prevents counting multiple checks as multiple families. At least two families make a month “prioritise”; one family is “review only”; zero is “clear”.

The weakest-link score is the minimum of the firing family maxima. Ranking orders families descending, then weakest-link severity descending, then illustrative tax exposure descending, then factory ID. The SQL exposure takes a maximum within firing family and sums families, but the frozen evaluator takes the maximum across all feature rows. The tertiary ranking semantics are therefore not unified; exact diagnostic comparison is in reports/ranking_alignment_audit.json. This may change order on ties even when headline precision is unchanged. Both exposure variants can count related events and are heuristics, not recoverable tax or fiscal impact.

K=3 selected on V3-A means a factory needs at least three prioritised months. A/B/C are split by random seed, not by a different institution, industry, geography or generator. Statistical intervals are conditional on frozen choices and this generator family. The result artifact’s internal evaluation_version='v2' names the evaluator implementation, while V3 names the preregistered scenario suite; they should not be conflated.

Prior-hours and prior-power window values are computed in V_LEDGER. Prior hours support dispositions; prior power is not a deployed robust per-factory detector. No trained ML, robust MAD model, adaptive adversary, machine-capacity engine or general graph learner is implemented.

## 6. End-to-end architecture

Generator → label-free CSV tables → Exasol GST_EVIDENCE → V_LEDGER joins/windows → V_FEATURES → V_ALL_EVIDENCE (thresholded) → V_RANKED_CASES (family counts) → officer API / static recorded cases. Supporting documents and machine changes feed V_SINGLE_SIGNAL_DISPOSITIONS. Truth remains outside the detector, with a separate evaluator schema/access role when explicitly loaded.

The restricted reader has only session access, schema usage and explicit SELECT on four label-free views. The API binds localhost, bounds rows/time/rate, and never falls back to an administrator account. Follow-ups compile one of three exact SELECT templates; unknown intents and injection are rejected. A real MCP integration and Python UDF execution are not demonstrated.

Public GitHub Pages has no backend; all cases, answer tables and results are snapshots. A local API can execute follow-ups live. Canonical data/metrics.json generates the deployed JSON and an identical JS wrapper, keeping file/offline operation reliable. All eight pages share source links, metadata and navigation. Home/Problem explain the use case before Results/System show proof.

## 7. Evaluation: exact results and intervals

| Run | Unit | TP | FP | FN | TN | Recall | 95% CI | FPR | 95% CI | Precision | 95% CI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V3-A DEV | factory_month | 3184 | 516 | 786 | 24314 | 80.20% | 77.82% – 82.68% | 2.08% | 1.90% – 2.27% | 86.05% | 84.46% – 87.51% |
| V3-A DEV | factory | 592 | 13 | 128 | 1667 | 82.22% | 79.49% – 84.92% | 0.77% | 0.36% – 1.22% | 97.85% | 96.66% – 98.95% |
| V3-B HELDOUT | factory_month | 3230 | 545 | 751 | 24274 | 81.14% | 78.55% – 83.58% | 2.20% | 2.01% – 2.38% | 85.56% | 84.12% – 87.05% |
| V3-B HELDOUT | factory | 599 | 7 | 121 | 1673 | 83.19% | 80.44% – 85.93% | 0.42% | 0.12% – 0.77% | 98.84% | 97.90% – 99.67% |
| V3-C HELDOUT | factory_month | 3209 | 566 | 741 | 24284 | 81.24% | 78.88% – 83.64% | 2.28% | 2.06% – 2.49% | 85.01% | 83.30% – 86.61% |
| V3-C HELDOUT | factory | 590 | 15 | 130 | 1665 | 81.94% | 79.03% – 84.67% | 0.89% | 0.48% – 1.35% | 97.52% | 96.24% – 98.69% |

Monthly accuracy is not a substitute for factory-level queue results. A cheat factory may still contain honest inactive months. The confidence intervals use 1,000 factory-cluster percentile resamples with seed 721; they do not measure generator bias.

### V3-B: cheat type and intensity

| Type/intensity | TP | FN | Monthly recall | 95% CI |
| --- | --- | --- | --- | --- |
| eway_reuse/5% | 219 | 277 | 44.15% | 38.22% – 50.00% |
| eway_reuse/15% | 418 | 0 | 100.00% | 100.00% – 100.00% |
| eway_reuse/30% | 445 | 0 | 100.00% | 100.00% – 100.00% |
| hidden_production/5% | 225 | 171 | 56.82% | 49.36% – 64.23% |
| hidden_production/15% | 322 | 107 | 75.06% | 65.44% – 84.94% |
| hidden_production/30% | 362 | 83 | 81.35% | 72.83% – 89.11% |
| itc_inflation/5% | 292 | 113 | 72.10% | 67.16% – 76.44% |
| itc_inflation/15% | 509 | 0 | 100.00% | 100.00% – 100.00% |
| itc_inflation/30% | 438 | 0 | 100.00% | 100.00% – 100.00% |

### V3-B: honest decoys

| Decoy | Honest months flagged | Honest months total | Monthly FPR | 95% CI |
| --- | --- | --- | --- | --- |
| longer_hours | 78 | 1920 | 4.06% | 3.23% – 5.00% |
| lumpy_bank_flows | 98 | 1920 | 5.10% | 4.22% – 5.99% |
| machinery_upgrade | 82 | 1920 | 4.27% | 3.39% – 5.16% |
| new_supplier_onboarding | 102 | 1920 | 5.31% | 4.32% – 6.30% |
| product_mix_shift | 71 | 1920 | 3.70% | 2.97% – 4.43% |
| seasonal_stock_build | 78 | 1920 | 4.06% | 3.23% – 4.95% |

Evasive monthly recall: 52.18%; interval 44.63% – 59.55%. Stock-aware/evasive paired comparison remains unmeasured.

| Population | Monthly FPR | 95% CI |
| --- | --- | --- |
| clean_factories | 0.27% | 0.16% – 0.38% |
| honest_decoys | 4.42% | 4.05% – 4.78% |

### V3-B: discrepancy-class confusion

Unit from artifact: factory-month; strongest non-financial evidence, including review-only cases; clean months excluded. These are heuristic discrepancy categories, not legal findings.

| Truth / prediction | mismatch | missing documents | supplier issue | contradicting evidence | needs human review | no signal |
| --- | --- | --- | --- | --- | --- | --- |
| mismatch | 1270 | 0 | 0 | 0 | 0 | 0 |
| missing documents | 0 | 1529 | 0 | 0 | 0 | 0 |
| supplier issue | 1255 | 0 | 87 | 5 | 5 | 0 |
| contradicting evidence | 973 | 0 | 3 | 40 | 254 | 0 |
| needs human review | 0 | 0 | 35 | 2949 | 4216 | 0 |

### V3-B: prevalence and review capacity

| Assumed cheating prevalence | Analytically adjusted precision |
| --- | --- |
| 1.00% | 27.18% |
| 5.00% | 66.04% |
| 10.00% | 80.41% |
| 13.82% | 85.56% |

Top-50 monthly macro precision: 75.00%. This averages months without weighting their returned counts. Jan–Mar contain no active cheat months; their returned queues are false alarms. It is not a measured weekly-operations result. Top-200 monthly macro precision: 74.96%.

### V3-C: cheat type and intensity

| Type/intensity | TP | FN | Monthly recall | 95% CI |
| --- | --- | --- | --- | --- |
| eway_reuse/5% | 164 | 209 | 43.97% | 36.62% – 50.86% |
| eway_reuse/15% | 522 | 0 | 100.00% | 100.00% – 100.00% |
| eway_reuse/30% | 396 | 0 | 100.00% | 100.00% – 100.00% |
| hidden_production/5% | 265 | 181 | 59.42% | 52.88% – 65.79% |
| hidden_production/15% | 358 | 108 | 76.82% | 67.82% – 84.95% |
| hidden_production/30% | 306 | 123 | 71.33% | 60.51% – 81.57% |
| itc_inflation/5% | 280 | 120 | 70.00% | 65.27% – 74.71% |
| itc_inflation/15% | 464 | 0 | 100.00% | 100.00% – 100.00% |
| itc_inflation/30% | 454 | 0 | 100.00% | 100.00% – 100.00% |

### V3-C: honest decoys

| Decoy | Honest months flagged | Honest months total | Monthly FPR | 95% CI |
| --- | --- | --- | --- | --- |
| longer_hours | 83 | 1920 | 4.32% | 3.49% – 5.21% |
| lumpy_bank_flows | 73 | 1920 | 3.80% | 2.97% – 4.64% |
| machinery_upgrade | 85 | 1920 | 4.43% | 3.54% – 5.36% |
| new_supplier_onboarding | 109 | 1920 | 5.68% | 4.58% – 6.82% |
| product_mix_shift | 102 | 1920 | 5.31% | 4.38% – 6.41% |
| seasonal_stock_build | 82 | 1920 | 4.27% | 3.39% – 5.16% |

Evasive monthly recall: 53.95%; interval 47.11% – 60.94%. Stock-aware/evasive paired comparison remains unmeasured.

| Population | Monthly FPR | 95% CI |
| --- | --- | --- |
| clean_factories | 0.21% | 0.13% – 0.31% |
| honest_decoys | 4.64% | 4.27% – 5.02% |

### V3-C: discrepancy-class confusion

Unit from artifact: factory-month; strongest non-financial evidence, including review-only cases; clean months excluded. These are heuristic discrepancy categories, not legal findings.

| Truth / prediction | mismatch | missing documents | supplier issue | contradicting evidence | needs human review | no signal |
| --- | --- | --- | --- | --- | --- | --- |
| mismatch | 1186 | 0 | 0 | 0 | 0 | 0 |
| missing documents | 0 | 1545 | 0 | 0 | 0 | 0 |
| supplier issue | 1216 | 0 | 89 | 4 | 9 | 0 |
| contradicting evidence | 998 | 0 | 11 | 38 | 294 | 0 |
| needs human review | 0 | 0 | 27 | 2930 | 4243 | 0 |

### V3-C: prevalence and review capacity

| Assumed cheating prevalence | Analytically adjusted precision |
| --- | --- |
| 1.00% | 26.49% |
| 5.00% | 65.24% |
| 10.00% | 79.85% |
| 13.72% | 85.01% |

Top-50 monthly macro precision: 75.00%. This averages months without weighting their returned counts. Jan–Mar contain no active cheat months; their returned queues are false alarms. It is not a measured weekly-operations result. Top-200 monthly macro precision: 74.92%.


### Wrong-clears, ablation and historical robustness

Zero wrong-clears span 720 active-cheat factories in each held-out seed; B has 3,981 active cheat months and C has 3,950. The approximate factory-level rule-of-three upper bound is 3/720 = 0.4167%, assuming independent factory outcomes. It is not a measured cluster-bootstrap interval and does not validate an external document verifier.

Ablation comes from replaying the frozen A/B/C features with one check removed and no retuning. Baselines reproduce the published confusion matrices. It measures conditional contribution while other checks remain; a small material-check effect does not prove that physical evidence is unnecessary. Intervals remain unmeasured.

The saved noise ×1.5, noise ×2 and 10% missing-document reports are historical DEV artifacts from a different protocol, not current V3 robustness evidence. They show substantial false-positive failures in that older setup; they cannot be relabelled as current tests or silently mixed with current accuracy. A fresh V3 robustness sweep remains open. Full values remain accessible in reports/robustness_*.json and the artifact index.

## 8. Performance, database and concurrency

| Current V3-C check | Exasol median seconds | DuckDB median seconds | Matched flagged rows | Matched absolute gap sum |
| --- | --- | --- | --- | --- |
| stock_rollforward | 0.168596 | 0.006147 | 3577 | 814801.8772 |
| supplier_chain | 0.154323 | 0.005950 | 3059 | 2641161.4699 |

Current comparison: 2,400 factories, 172,800 feature rows, Apple M2 / 16 GiB machine per recorded hardware metadata. DuckDB is faster in this run. Query-result cache was off; load coverage and physical plans differ. CSV load/input hashing is separately recorded; Exasol ingestion is not remeasured. This is not general database superiority evidence. The 20,978,945-row workload and raw/cache profile are historical DEV and predate the current detector.

Today's actual API smoke passed health, queue, case, validated note, all intents, injection/unknown-intent rejection and activity. Eight parallel requests: p50 3.851653s; p95 4.096334s. This includes the new live protocol guard, so the older 1.240s p95 should not be treated as the current API timing. No 50-session result exists.

Live database verification: 28,800 monthly rows and 172,800 features. All live signal counts/flags match C after the approved repair. The restricted reader was denied truth access. Exact queries/outcomes: reports/judge_database_audit.json, reports/threshold_repair.json and reports/live_smoke.json.


## 9. Security and AI limits

No LLM determines priority or clearance. Optional note generation has a strict prompt and numeric validator; current demonstrations use the deterministic fallback. The validator binds expected, observed and gap fields but does not certify all prose or legal validity. No real API-key-backed model invocation was established by this audit.

The API uses a local self-signed TLS exception only for the local endpoint. Credentials are read at runtime from ignored environment/credential files and are not published. It has no production user authentication, multi-user access-control portal or durable tamper-proof audit log; activity is a bounded in-memory query buffer. These limitations matter before any real deployment.

A heuristic tracked-file scan found no obvious secret-token/private-key literals. This does not prove the absence of every possible secret. Machine paths, credentials, DB images, virtualenvs and unrelated installed packages are excluded from the submission package. Synthetic scoring labels are intentionally public for reproducibility, but the API cannot read database truth.

## 10. Reproducibility and upload scope

The repository contains source, SQL, tests, pinned runtime requirements, optional benchmark/PDF requirements, synthetic audit CSV archives with hashes, canonical site metrics, current deck/PDF/previews, result artifacts and this status register. Large regenerated datasets, runtime images, caches and credentials are intentionally excluded. See data/README.md and the submission manifest.

make all is an offline readiness pipeline: tests → restore/verify audit inputs → recompute numbers and ablation → export static site. make reproduce explicitly regenerates/loads the database and requires documented loader privileges; it is destructive and is not run automatically by an audit. The local API remains restricted. The clean helper now uses an actual clone and an isolated venv; its exact commit, scope and outcome are in reports/clean_setup.json. No second-machine or new clean database-installation claim is made.

The pitch PPTX uses native editable text and was imported, changed, checked and rendered with the supplied presentation runtime. Its native PDF exporter failed on a missing standard-font module; the PDF uses the inspected slide PNGs. The editable source is the PPTX. PowerPoint/Google Slides and second-machine file rendering remain unverified.

## 11. What a judge can fairly credit

- A specific officer-facing problem, a functioning SQL reconciliation engine in Exasol and an inspectable explanation trail.
- Better-than-declaration-only evidence grouping in the synthetic setup, including honest decoys and genuine published misses.
- Held-out synthetic evaluation with false-positive rates and cluster intervals, rather than only a catch-rate headline.
- A clean public snapshot demo with source links and a real guarded local query path, without hiding an engine comparison that favours DuckDB.
- An audit trail that records the threshold mistake and its repair instead of retroactively rewriting held-out results.

What is not established: novelty over the entire GST-fraud market, taxpayer accuracy, enforcement readiness, actual officer time saved, recovered tax revenue, robust fake-document verification, new current full-scale performance, a working UDF/MCP demo, weekly operational utility, or a win prediction.

## 12. Remaining priorities before submission

1. Kushagra records and checks the required video (maximum three minutes), adds a working public/unlisted URL and reviews the real submission files.
2. Complete the final portal submission before the official deadline. Repository upload is not portal submission.
3. Rehearse the local Live demo and its Snapshot fallback; show current mode and exact recorded metrics.
4. If time remains, independently reproduce on a second machine, predeclare and test sophisticated forgers, add missing uncertainty and current robustness, and run an authorised fresh full-scale workload. Do not invent completion or modify held-out thresholds to improve scores.

See docs/LICENCE_AUDIT.md and reports/licence_review.json for the actual Personal EULA inspection and tool-licence scope.

See PROJECT_STATUS.md for per-feature states and SUBMISSION_CHECKLIST.md for the actual mandatory hand-in items.
