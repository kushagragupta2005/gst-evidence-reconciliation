# Site numbers audit

Scope: current displayed metrics, both seed selections, all recorded case/follow-up evidence and measured API artifacts. The single-page-to-multi-page audit began at db0e649; sources refreshed by the later threshold-repair audit are inventoried at their current values. The inventory below preserves original precision; page formatting is a separate concern. Numeric strings in recorded SQL rows are listed too. Layout dimensions and dates are not measurements.

## Findings and corrections

- No mismatch was found in the monthly/factory confusion matrices, ratios, displayed bootstrap intervals, prevalence formula, ablation ratios, median comparison timings or concurrent p95 arithmetic.
- V3-B and V3-C are separate real saved runs. Rounded C values (81.2%, 2.3%, 85.0%) must not be attributed to B (81.1%, 2.2%, 85.6%). Every result group now names its seed.
- Zero of 720 counts factories with at least one active cheat month. Zero of 3,950 counts active cheat months in V3-C; V3-B has 3,981. These are different units, not conflicting results. The 3/N approximate upper bound uses factories and assumes their outcomes are independent. It is not a measured cluster-bootstrap interval or real-world safety guarantee.
- The prevalence table was ordered by object keys, not probability, and its old generic numeric formatter hid differences by rounding probabilities/precision to two decimals. Sort by numeric assumed prevalence and display probabilities as percentages. Analytic reweighting assumes recall/FPR transfer across prevalence; it is not a regenerated low-prevalence experiment.
- Leave-one-check-out ablation is a post-hoc conditional contribution with the other checks still present. Small loss after removing material/output does not mean that evidence is useless: other production checks and families can still satisfy the threshold. Intervals are unmeasured.
- The case caption once used one gap sign for every check. Bank checks use flows minus invoices; other displayed checks use expected minus observed. The corrected wording is retained.
- Current benchmark medians and concurrency p95 reproduce from recorded repeats; elapsed timings cannot be regenerated from arithmetic. They remain measured artifacts from their stated dates and machines, not new runs during this audit. Exasol/DuckDB counts and gap checksums were previously matched; physical plans and ingestion coverage differ. DuckDB was faster in the recorded comparison.
- Historical 20,978,945 rows come from an older DEV manifest. Its run timestamp/source SHA are unavailable; do not substitute a later artifact commit date. It remains historical, not fresh.
- Case/evidence values and note validation are recorded observations. The new home line chart uses the complete recorded dispatch response for one factory, not interpolated or invented evidence.
- Per-artifact commit/date metadata describe when a file was committed. Explicit run timestamps are shown separately where the artifact contains one. Missing run timestamps stay unavailable.

## Reproduction

`PYTHONPATH=. .venv/bin/python scripts/audit_site_numbers.py` recomputes monthly/factory confidence intervals from the local held-out prediction CSVs (factory-cluster bootstrap, fixed seed and iterations), ratios, denominator counts and timing summaries. `scripts/site_ablation.py` separately replays the frozen feature files; its feature hashes and baseline matrices were checked. No detector thresholds were changed. Those local CSVs are intentionally not needed to render the deployed site.

## Verified groups

- v3_a: threshold 0.05 and K=3 recomputed from calibration inputs only; B/C were not used to choose them.
- v3_b: monthly and factory confusion matrices, all displayed CIs, prevalence precision and denominator counts reproduce exactly.
- v3_c: monthly and factory confusion matrices, all displayed CIs, prevalence precision and denominator counts reproduce exactly.

## Complete numeric inventory

Source file | JSON field | Exact value | Verification scope
---|---|---|---
`results.json` | `/factory_month/tp` | 3230 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/fp` | 545 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/fn` | 751 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/tn` | 24274 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/recall` | 0.8113539311730721 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/fpr` | 0.02195898303718925 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/precision` | 0.8556291390728477 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/ci95/recall/0` | 0.7854896569419634 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/ci95/recall/1` | 0.8358242200944961 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/ci95/fpr/0` | 0.02012890969634812 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/ci95/fpr/1` | 0.023766074335037215 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/ci95/precision/0` | 0.8412136734332176 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory_month/ci95/precision/1` | 0.8704919215098643 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/tp` | 599 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/fp` | 7 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/fn` | 121 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/tn` | 1673 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/recall` | 0.8319444444444445 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/fpr` | 0.004166666666666667 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/precision` | 0.9884488448844885 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/ci95/recall/0` | 0.8043743474027929 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/ci95/recall/1` | 0.8593103448275862 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/ci95/fpr/0` | 0.0011918951132300357 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/ci95/fpr/1` | 0.007706101223437058 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/ci95/precision/0` | 0.9789980308333026 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/factory/ci95/precision/1` | 0.9966998058949222 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`results.json` | `/prevalence_adjusted_precision/1.00%/assumed_prevalence` | 0.01 | Recomputed analytic reweighting
`results.json` | `/prevalence_adjusted_precision/1.00%/precision` | 0.27178366167845175 | Recomputed analytic reweighting
`results.json` | `/prevalence_adjusted_precision/5.00%/assumed_prevalence` | 0.05 | Recomputed analytic reweighting
`results.json` | `/prevalence_adjusted_precision/5.00%/precision` | 0.6604026530492458 | Recomputed analytic reweighting
`results.json` | `/prevalence_adjusted_precision/10.00%/assumed_prevalence` | 0.1 | Recomputed analytic reweighting
`results.json` | `/prevalence_adjusted_precision/10.00%/precision` | 0.8041290101254186 | Recomputed analytic reweighting
`results.json` | `/prevalence_adjusted_precision/synthetic observed/assumed_prevalence` | 0.13822916666666665 | Recomputed analytic reweighting
`results.json` | `/prevalence_adjusted_precision/synthetic observed/precision` | 0.8556291390728478 | Recomputed analytic reweighting
`results.json` | `/dataset/seed` | 51002 | Generator manifest; not real data
`results.json` | `/dataset/factories` | 2400 | Generator manifest; not real data
`results.json` | `/dataset/months` | 12 | Generator manifest; not real data
`results.json` | `/dataset/rows/factories` | 2400 | Generator manifest; not real data
`results.json` | `/dataset/rows/suppliers` | 2400 | Generator manifest; not real data
`results.json` | `/dataset/rows/factory_month` | 28800 | Generator manifest; not real data
`results.json` | `/dataset/rows/invoices` | 28711 | Generator manifest; not real data
`results.json` | `/dataset/rows/purchase_invoices` | 28800 | Generator manifest; not real data
`results.json` | `/dataset/rows/eway_bills` | 57600 | Generator manifest; not real data
`results.json` | `/dataset/rows/supplier_returns` | 27360 | Generator manifest; not real data
`results.json` | `/dataset/rows/bank_entries` | 57600 | Generator manifest; not real data
`results.json` | `/dataset/rows/machines` | 2560 | Generator manifest; not real data
`results.json` | `/dataset/rows/supporting_documents` | 12621 | Generator manifest; not real data
`results.json` | `/dataset/rows/truth` | 28800 | Generator manifest; not real data
`results.json` | `/dataset/raw_evidence_rows` | 241492 | Generator manifest; not real data
`results.json` | `/dataset/noise_multiplier` | 1.0 | Generator manifest; not real data
`results.json` | `/dataset/missing_documents_rate` | 0.0 | Generator manifest; not real data
`results.json` | `/protocol/threshold` | 0.05 | Frozen protocol / source manifest
`results.json` | `/protocol/months_per_factory` | 12 | Frozen protocol / source manifest
`results.json` | `/protocol/train_seed` | 51001 | Frozen protocol / source manifest
`results.json` | `/protocol/held_out_seed` | 51002 | Frozen protocol / source manifest
`results.json` | `/factory_queue/k` | 3 | Recomputed queue agrees
`results.json` | `/factory_queue/queue_size` | 606 | Recomputed queue agrees
`reports/v3_c_results.json` | `/factory_month/tp` | 3209 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/fp` | 566 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/fn` | 741 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/tn` | 24284 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/recall` | 0.8124050632911393 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/fpr` | 0.02277665995975855 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/precision` | 0.850066225165563 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/ci95/recall/0` | 0.7887847993904595 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/ci95/recall/1` | 0.8363693799865322 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/ci95/fpr/0` | 0.020632911292385554 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/ci95/fpr/1` | 0.024894438385804088 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/ci95/precision/0` | 0.8329588574469864 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory_month/ci95/precision/1` | 0.8660689414847141 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/tp` | 590 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/fp` | 15 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/fn` | 130 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/tn` | 1665 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/recall` | 0.8194444444444444 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/fpr` | 0.008928571428571428 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/precision` | 0.9752066115702479 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/ci95/recall/0` | 0.7902541977167471 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/ci95/recall/1` | 0.8467386746490246 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/ci95/fpr/0` | 0.004750382624146928 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/ci95/fpr/1` | 0.013497850727382498 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/ci95/precision/0` | 0.962417672197084 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/factory/ci95/precision/1` | 0.9869286376867223 | Recomputed counts, ratios and factory-cluster bootstrap intervals
`reports/v3_c_results.json` | `/prevalence_adjusted_precision/1.00%/assumed_prevalence` | 0.01 | Recomputed analytic reweighting
`reports/v3_c_results.json` | `/prevalence_adjusted_precision/1.00%/precision` | 0.264860478822843 | Recomputed analytic reweighting
`reports/v3_c_results.json` | `/prevalence_adjusted_precision/5.00%/assumed_prevalence` | 0.05 | Recomputed analytic reweighting
`reports/v3_c_results.json` | `/prevalence_adjusted_precision/5.00%/precision` | 0.6524494986375197 | Recomputed analytic reweighting
`reports/v3_c_results.json` | `/prevalence_adjusted_precision/10.00%/assumed_prevalence` | 0.1 | Recomputed analytic reweighting
`reports/v3_c_results.json` | `/prevalence_adjusted_precision/10.00%/precision` | 0.7985148943648397 | Recomputed analytic reweighting
`reports/v3_c_results.json` | `/prevalence_adjusted_precision/synthetic observed/assumed_prevalence` | 0.1371527777777778 | Recomputed analytic reweighting
`reports/v3_c_results.json` | `/prevalence_adjusted_precision/synthetic observed/precision` | 0.850066225165563 | Recomputed analytic reweighting
`reports/v3_c_results.json` | `/dataset/seed` | 51003 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/factories` | 2400 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/months` | 12 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/factories` | 2400 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/suppliers` | 2400 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/factory_month` | 28800 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/invoices` | 28695 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/purchase_invoices` | 28800 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/eway_bills` | 57600 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/supplier_returns` | 27360 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/bank_entries` | 57600 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/machines` | 2560 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/supporting_documents` | 12590 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/rows/truth` | 28800 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/raw_evidence_rows` | 241445 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/noise_multiplier` | 1.0 | Generator manifest; not real data
`reports/v3_c_results.json` | `/dataset/missing_documents_rate` | 0.0 | Generator manifest; not real data
`reports/v3_c_results.json` | `/protocol/threshold` | 0.05 | Frozen protocol / source manifest
`reports/v3_c_results.json` | `/protocol/months_per_factory` | 12 | Frozen protocol / source manifest
`reports/v3_c_results.json` | `/protocol/train_seed` | 51001 | Frozen protocol / source manifest
`reports/v3_c_results.json` | `/protocol/held_out_seed` | 51003 | Frozen protocol / source manifest
`reports/v3_c_results.json` | `/factory_queue/k` | 3 | Recomputed queue agrees
`reports/v3_c_results.json` | `/factory_queue/queue_size` | 605 | Recomputed queue agrees
`reports/v3_b_dispositions.json` | `/cleared_months` | 4767 | Artifact value; no new timing run
`reports/v3_b_dispositions.json` | `/cleared_honest_decoy_months` | 4767 | Artifact value; no new timing run
`reports/v3_b_dispositions.json` | `/wrong_clears_active_cheat_months` | 0 | Artifact value; no new timing run
`reports/v3_b_dispositions.json` | `/active_cheat_months` | 3981 | Artifact value; no new timing run
`reports/v3_b_dispositions.json` | `/wrong_clear_rate_active_cheat_months` | 0.0 | Artifact value; no new timing run
`reports/v3_b_dispositions.json` | `/rejected_fake_explanation_documents` | 3981 | Artifact value; no new timing run
`reports/v3_c_dispositions.json` | `/cleared_months` | 4795 | Artifact value; no new timing run
`reports/v3_c_dispositions.json` | `/cleared_honest_decoy_months` | 4795 | Artifact value; no new timing run
`reports/v3_c_dispositions.json` | `/wrong_clears_active_cheat_months` | 0 | Artifact value; no new timing run
`reports/v3_c_dispositions.json` | `/active_cheat_months` | 3950 | Artifact value; no new timing run
`reports/v3_c_dispositions.json` | `/wrong_clear_rate_active_cheat_months` | 0.0 | Artifact value; no new timing run
`reports/v3_c_dispositions.json` | `/rejected_fake_explanation_documents` | 3950 | Artifact value; no new timing run
`reports/wrong_clear_bounds.json` | `/seeds/v3_b/wrong_clear_factories` | 0 | Artifact value; no new timing run
`reports/wrong_clear_bounds.json` | `/seeds/v3_b/active_cheat_factories` | 720 | Artifact value; no new timing run
`reports/wrong_clear_bounds.json` | `/seeds/v3_b/approximate_upper_95` | 0.004166666666666667 | Artifact value; no new timing run
`reports/wrong_clear_bounds.json` | `/seeds/v3_b/active_cheat_months` | 3981 | Artifact value; no new timing run
`reports/wrong_clear_bounds.json` | `/seeds/v3_c/wrong_clear_factories` | 0 | Artifact value; no new timing run
`reports/wrong_clear_bounds.json` | `/seeds/v3_c/active_cheat_factories` | 720 | Artifact value; no new timing run
`reports/wrong_clear_bounds.json` | `/seeds/v3_c/approximate_upper_95` | 0.004166666666666667 | Artifact value; no new timing run
`reports/wrong_clear_bounds.json` | `/seeds/v3_c/active_cheat_months` | 3950 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/all_checks/tp` | 3230 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/all_checks/fp` | 545 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/all_checks/fn` | 751 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/all_checks/tn` | 24274 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/all_checks/recall` | 0.8113539311730721 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/all_checks/fpr` | 0.02195898303718925 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_purchases/tp` | 3128 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_purchases/fp` | 394 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_purchases/fn` | 853 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_purchases/tn` | 24425 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_purchases/recall` | 0.7857322280833962 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_purchases/fpr` | 0.01587493452596801 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_sales/tp` | 2958 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_sales/fp` | 314 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_sales/fn` | 1023 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_sales/tn` | 24505 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_sales/recall` | 0.7430293896006028 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/bank_sales/fpr` | 0.012651597566380596 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/dispatch_invoice/tp` | 2756 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/dispatch_invoice/fp` | 545 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/dispatch_invoice/fn` | 1225 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/dispatch_invoice/tn` | 24274 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/dispatch_invoice/recall` | 0.6922883697563427 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/dispatch_invoice/fpr` | 0.02195898303718925 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/material_output/tp` | 3216 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/material_output/fp` | 99 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/material_output/fn` | 765 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/material_output/tn` | 24720 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/material_output/recall` | 0.8078372268274303 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/material_output/fpr` | 0.003988879487489424 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/stock_rollforward/tp` | 2615 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/stock_rollforward/fp` | 545 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/stock_rollforward/fn` | 1366 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/stock_rollforward/tn` | 24274 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/stock_rollforward/recall` | 0.6568701331323789 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/stock_rollforward/fpr` | 0.02195898303718925 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/supplier_chain/tp` | 2919 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/supplier_chain/fp` | 299 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/supplier_chain/fn` | 1062 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/supplier_chain/tn` | 24520 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/supplier_chain/recall` | 0.7332328560663149 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_b/checks/supplier_chain/fpr` | 0.012047221886457956 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/all_checks/tp` | 3209 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/all_checks/fp` | 566 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/all_checks/fn` | 741 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/all_checks/tn` | 24284 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/all_checks/recall` | 0.8124050632911393 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/all_checks/fpr` | 0.02277665995975855 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_purchases/tp` | 3111 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_purchases/fp` | 429 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_purchases/fn` | 839 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_purchases/tn` | 24421 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_purchases/recall` | 0.7875949367088607 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_purchases/fpr` | 0.017263581488933602 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_sales/tp` | 2997 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_sales/fp` | 336 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_sales/fn` | 953 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_sales/tn` | 24514 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_sales/recall` | 0.7587341772151899 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/bank_sales/fpr` | 0.013521126760563381 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/dispatch_invoice/tp` | 2772 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/dispatch_invoice/fp` | 566 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/dispatch_invoice/fn` | 1178 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/dispatch_invoice/tn` | 24284 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/dispatch_invoice/recall` | 0.7017721518987342 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/dispatch_invoice/fpr` | 0.02277665995975855 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/material_output/tp` | 3198 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/material_output/fp` | 96 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/material_output/fn` | 752 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/material_output/tn` | 24754 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/material_output/recall` | 0.809620253164557 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/material_output/fpr` | 0.00386317907444668 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/stock_rollforward/tp` | 2573 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/stock_rollforward/fp` | 566 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/stock_rollforward/fn` | 1377 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/stock_rollforward/tn` | 24284 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/stock_rollforward/recall` | 0.6513924050632911 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/stock_rollforward/fpr` | 0.02277665995975855 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/supplier_chain/tp` | 2846 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/supplier_chain/fp` | 285 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/supplier_chain/fn` | 1104 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/supplier_chain/tn` | 24565 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/supplier_chain/recall` | 0.7205063291139241 | Artifact value; no new timing run
`reports/site_ablation.json` | `/seeds/v3_c/checks/supplier_chain/fpr` | 0.011468812877263581 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/hardware/memory_bytes` | 17179869184 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/threshold` | 0.05 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/seed` | 51003 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/factories` | 2400 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/months` | 12 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/factories` | 2400 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/suppliers` | 2400 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/factory_month` | 28800 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/invoices` | 28695 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/purchase_invoices` | 28800 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/eway_bills` | 57600 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/supplier_returns` | 27360 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/bank_entries` | 57600 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/machines` | 2560 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/supporting_documents` | 12590 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/rows/truth` | 28800 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/raw_evidence_rows` | 241445 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/noise_multiplier` | 1.0 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/data_manifest/missing_documents_rate` | 0.0 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/exasol_seconds/0` | 0.16160758399928454 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/exasol_seconds/1` | 0.17117145800148137 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/exasol_seconds/2` | 0.1685958330053836 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/duckdb_seconds/0` | 0.0122445839951979 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/duckdb_seconds/1` | 0.006147291998786386 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/duckdb_seconds/2` | 0.004778750000696164 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/exasol_median_seconds` | 0.1685958330053836 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/duckdb_median_seconds` | 0.006147291998786386 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/matched_flagged_rows` | 3577 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/stock_rollforward/matched_abs_gap_sum` | 814801.8772 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/exasol_seconds/0` | 0.15710454100189963 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/exasol_seconds/1` | 0.15301341700251214 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/exasol_seconds/2` | 0.1543232080002781 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/duckdb_seconds/0` | 0.009320958000898827 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/duckdb_seconds/1` | 0.005950334001681767 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/duckdb_seconds/2` | 0.005594332993496209 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/exasol_median_seconds` | 0.1543232080002781 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/duckdb_median_seconds` | 0.005950334001681767 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/matched_flagged_rows` | 3059 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/checks/supplier_chain/matched_abs_gap_sum` | 2641161.4699 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/duckdb_threads` | 4 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/duckdb_csv_load_seconds` | 0.14328008399752434 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/current_factory_months` | 28800 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/current_factories` | 2400 | Artifact value; no new timing run
`reports/benchmark_current_reader.json` | `/current_feature_rows` | 172800 | Artifact value; no new timing run
`reports/live_smoke.json` | `/health/threshold` | 0.05 | Artifact value; no new timing run
`reports/live_smoke.json` | `/health/query_timeout_seconds` | 30 | Artifact value; no new timing run
`reports/live_smoke.json` | `/health/row_limit` | 200 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes//case/F000902/status` | 200 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes//case/F000902/evidence_rows` | 22 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes//note/F000902/status` | 200 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes//note/F000902/evidence_rows` | 22 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes/ask_dispatch/status` | 200 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes/ask_dispatch/rows` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes/ask_timeline/status` | 200 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes/ask_timeline/rows` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes/ask_evidence/status` | 200 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes/ask_evidence/rows` | 22 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes/injection/status` | 400 | Artifact value; no new timing run
`reports/live_smoke.json` | `/outcomes/unknown_intent/status` | 400 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/queries` | 8 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/latencies_seconds/0` | 2.95874087500124 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/latencies_seconds/1` | 3.1774352919965168 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/latencies_seconds/2` | 3.74642108399712 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/latencies_seconds/3` | 3.758142749997205 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/latencies_seconds/4` | 3.7824448750034207 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/latencies_seconds/5` | 3.8089818750013364 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/latencies_seconds/6` | 3.8140431659994647 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/latencies_seconds/7` | 3.863338916002249 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/p50_seconds` | 3.770293812500313 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/p95_seconds` | 3.8460854035012746 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/rows_each/0` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/rows_each/1` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/rows_each/2` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/rows_each/3` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/rows_each/4` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/rows_each/5` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/rows_each/6` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/parallel_ask/rows_each/7` | 12 | Artifact value; no new timing run
`reports/live_smoke.json` | `/activity_rows` | 15 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/evidence/0/severity` | 0.2785582050114638 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/evidence/1/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/evidence/2/severity` | 0.2738096603461148 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/evidence/3/severity` | 0.18262276960651794 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/0/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/0/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/0/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/1/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/1/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/1/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/2/signal_count` | 2 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/2/total_severity` | 0.26337077649995566 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/2/weakest_link_normalised_gap` | 0.12717311971477258 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/3/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/3/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/3/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/4/signal_count` | 4 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/4/total_severity` | 1.2349906349640964 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/4/weakest_link_normalised_gap` | 0.18262276960651794 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/5/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/5/total_severity` | 1.0455243041650597 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/5/weakest_link_normalised_gap` | 0.2539159903532607 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/6/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/6/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/6/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/7/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/7/total_severity` | 1.0357734887359968 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/7/weakest_link_normalised_gap` | 0.2437289147402798 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/8/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/8/total_severity` | 1.0598114916690535 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/8/weakest_link_normalised_gap` | 0.26454925700138066 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/9/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/9/total_severity` | 1.051572453216578 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/9/weakest_link_normalised_gap` | 0.2487406029962557 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/10/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/10/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/10/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/11/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/11/total_severity` | 1.0442102009916157 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/0/timeline/11/weakest_link_normalised_gap` | 0.24071686905958603 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/evidence/0/severity` | 0.24190376510835304 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/0/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/0/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/0/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/1/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/1/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/1/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/2/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/2/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/2/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/3/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/3/total_severity` | 0.24190376510835304 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/3/weakest_link_normalised_gap` | 0.24190376510835304 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/4/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/4/total_severity` | 0.26873068704511627 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/4/weakest_link_normalised_gap` | 0.26873068704511627 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/5/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/5/total_severity` | 0.2678982356084832 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/5/weakest_link_normalised_gap` | 0.2678982356084832 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/6/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/6/total_severity` | 0.25245770665694395 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/6/weakest_link_normalised_gap` | 0.25245770665694395 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/7/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/7/total_severity` | 0.2630604668793421 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/7/weakest_link_normalised_gap` | 0.2630604668793421 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/8/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/8/total_severity` | 0.25062758930554274 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/8/weakest_link_normalised_gap` | 0.25062758930554274 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/9/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/9/total_severity` | 0.2766216142775409 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/9/weakest_link_normalised_gap` | 0.2766216142775409 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/10/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/10/total_severity` | 0.243723490955938 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/10/weakest_link_normalised_gap` | 0.243723490955938 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/11/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/11/total_severity` | 0.24703349723961848 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/1/timeline/11/weakest_link_normalised_gap` | 0.24703349723961848 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/evidence/0/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/0/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/0/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/0/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/1/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/1/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/1/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/2/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/2/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/2/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/3/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/3/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/3/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/4/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/4/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/4/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/5/signal_count` | 2 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/5/total_severity` | 2.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/5/weakest_link_normalised_gap` | 1.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/6/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/6/total_severity` | 0.10174902184619065 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/6/weakest_link_normalised_gap` | 0.10174902184619065 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/7/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/7/total_severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/7/weakest_link_normalised_gap` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/8/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/8/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/8/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/9/signal_count` | 1 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/9/total_severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/9/weakest_link_normalised_gap` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/10/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/10/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/10/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/11/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/11/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/examples/2/timeline/11/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/0/severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/1/severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/2/severity` | 6.164155656765513e-08 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/3/severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/4/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/5/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/6/severity` | 8.180167870132964e-08 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/7/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/8/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/9/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/10/severity` | 7.139257936962922e-08 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/rows/11/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/row_limit` | 200 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/response/timeout_seconds` | 30 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/0/latency_ms` | 526.6138340011821 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/0/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/0/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/0/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/1/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/1/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/1/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/2/signal_count` | 2 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/2/total_severity` | 0.26337077649995566 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/2/weakest_link_normalised_gap` | 0.12717311971477258 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/3/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/3/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/3/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/4/signal_count` | 4 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/4/total_severity` | 1.2349906349640964 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/4/weakest_link_normalised_gap` | 0.18262276960651794 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/5/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/5/total_severity` | 1.0455243041650597 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/5/weakest_link_normalised_gap` | 0.2539159903532607 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/6/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/6/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/6/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/7/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/7/total_severity` | 1.0357734887359968 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/7/weakest_link_normalised_gap` | 0.2437289147402798 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/8/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/8/total_severity` | 1.0598114916690535 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/8/weakest_link_normalised_gap` | 0.26454925700138066 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/9/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/9/total_severity` | 1.051572453216578 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/9/weakest_link_normalised_gap` | 0.2487406029962557 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/10/signal_count` | 0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/10/total_severity` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/10/weakest_link_normalised_gap` | 0.0 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/11/signal_count` | 3 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/11/total_severity` | 1.0442102009916157 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/rows/11/weakest_link_normalised_gap` | 0.24071686905958603 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/row_limit` | 200 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/response/timeout_seconds` | 30 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/1/latency_ms` | 431.3006660013343 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/0/severity` | 0.12717311971477258 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/1/severity` | 0.1361976567851831 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/2/severity` | 0.2785582050114638 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/3/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/4/severity` | 0.2738096603461148 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/5/severity` | 0.18262276960651794 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/6/severity` | 0.2916083138117991 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/7/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/8/severity` | 0.2539159903532607 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/9/severity` | 0.29204457399571715 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/10/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/11/severity` | 0.2437289147402798 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/12/severity` | 0.2952622346676728 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/13/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/14/severity` | 0.26454925700138066 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/15/severity` | 0.3028318502203222 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/16/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/17/severity` | 0.10864439514016845 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/18/severity` | 0.2487406029962557 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/19/severity` | 0.30349333193202954 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/20/severity` | 0.5 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/rows/21/severity` | 0.24071686905958603 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/row_limit` | 200 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/response/timeout_seconds` | 30 | Artifact value; no new timing run
`reports/site_examples.json` | `/questions/2/latency_ms` | 413.5758749980596 | Artifact value; no new timing run
`reports/benchmark_full.json` | `/manifest/raw_evidence_rows` | 20978945 | Historical DEV manifest only; not a fresh scale run
`reports/site_examples.json` | `/examples/0/evidence/0/expected` | 112302.0817 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/0/observed` | 155663.3986 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/0/gap` | 43361.3169 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/0/estimated_tax_exposure_inr` | 7805.037042 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/1/expected` | 1336.9296 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/1/observed` | 935.8507 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/1/gap` | 401.0789 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/1/estimated_tax_exposure_inr` | 8663.30424 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/2/expected` | 2313.6512 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/2/observed` | 1912.5724 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/2/gap` | 401.0788 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/2/estimated_tax_exposure_inr` | 8663.30208 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/3/expected` | 1831.011 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/3/observed` | 1496.6267 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/3/gap` | 334.3843 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/evidence/3/estimated_tax_exposure_inr` | 5417.02566 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/0/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/1/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/2/estimated_tax_exposure_inr` | 10012.610772 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/3/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/4/estimated_tax_exposure_inr` | 30548.669022 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/5/estimated_tax_exposure_inr` | 29996.26659 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/6/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/7/estimated_tax_exposure_inr` | 27594.390816 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/8/estimated_tax_exposure_inr` | 23409.853074 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/9/estimated_tax_exposure_inr` | 29873.773098 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/10/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/0/timeline/11/estimated_tax_exposure_inr` | 25707.279114 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/evidence/0/expected` | 1410.4144 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/evidence/0/observed` | 1419.0091 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/evidence/0/gap` | -8.5947 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/evidence/0/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/0/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/1/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/2/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/3/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/4/estimated_tax_exposure_inr` | 271.363824 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/5/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/6/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/7/estimated_tax_exposure_inr` | 401.027328 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/8/estimated_tax_exposure_inr` | 32.774976 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/9/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/10/estimated_tax_exposure_inr` | 429.893568 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/1/timeline/11/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/evidence/0/expected` | 1121.3356 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/evidence/0/observed` | 1065.2688 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/evidence/0/gap` | 56.0668 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/evidence/0/estimated_tax_exposure_inr` | 1211.04288 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/0/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/1/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/2/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/3/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/4/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/5/estimated_tax_exposure_inr` | 65020.947048 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/6/estimated_tax_exposure_inr` | 3328.879248 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/7/estimated_tax_exposure_inr` | 1211.04288 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/8/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/9/estimated_tax_exposure_inr` | 1847.6964 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/10/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/examples/2/timeline/11/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/0/expected` | 1527.203 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/0/observed` | 1527.203 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/0/gap` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/1/expected` | 1417.3832 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/1/observed` | 1417.3832 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/1/gap` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/2/expected` | 1622.2822 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/2/observed` | 1622.2823 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/2/gap` | -0.0001 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/3/expected` | 1564.5162 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/3/observed` | 1564.5162 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/3/gap` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/4/expected` | 1336.9296 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/4/observed` | 935.8507 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/4/gap` | 401.0789 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/5/expected` | 1563.5984 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/5/observed` | 1094.5188 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/5/gap` | 469.0796 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/6/expected` | 1222.4688 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/6/observed` | 1222.4687 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/6/gap` | 0.0001 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/7/expected` | 1437.4118 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/7/observed` | 1006.1883 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/7/gap` | 431.2235 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/8/expected` | 1213.2734 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/8/observed` | 849.2914 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/8/gap` | 363.982 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/9/expected` | 1529.8122 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/9/observed` | 1070.8685 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/9/gap` | 458.9437 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/10/expected` | 1400.7058 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/10/observed` | 1400.7059 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/10/gap` | -0.0001 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/11/expected` | 1315.0624 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/11/observed` | 920.5437 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/0/response/rows/11/gap` | 394.5187 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/0/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/1/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/2/estimated_tax_exposure_inr` | 10012.610772 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/3/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/4/estimated_tax_exposure_inr` | 30548.669022 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/5/estimated_tax_exposure_inr` | 29996.26659 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/6/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/7/estimated_tax_exposure_inr` | 27594.390816 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/8/estimated_tax_exposure_inr` | 23409.853074 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/9/estimated_tax_exposure_inr` | 29873.773098 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/10/estimated_tax_exposure_inr` | 0 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/1/response/rows/11/estimated_tax_exposure_inr` | 25707.279114 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/0/expected` | 1942.61272 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/0/observed` | 1695.5646 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/0/gap` | 247.04812 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/1/expected` | 2119.4557 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/1/observed` | 1830.7908 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/1/gap` | 288.6649 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/2/expected` | 112302.0817 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/2/observed` | 155663.3986 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/2/gap` | 43361.3169 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/3/expected` | 1336.9296 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/3/observed` | 935.8507 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/3/gap` | 401.0789 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/4/expected` | 2313.6512 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/4/observed` | 1912.5724 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/4/gap` | 401.0788 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/5/expected` | 1831.011 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/5/observed` | 1496.6267 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/5/gap` | 334.3843 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/6/expected` | 131342.2613 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/6/observed` | 185409.0948 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/6/gap` | 54066.8335 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/7/expected` | 1563.5984 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/7/observed` | 1094.5188 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/7/gap` | 469.0796 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/8/expected` | 2665.4343 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/8/observed` | 2196.3548 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/8/gap` | 469.0795 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/9/expected` | 120742.5957 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/9/observed` | 170551.1269 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/9/gap` | 49808.5312 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/10/expected` | 1437.4118 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/10/observed` | 1006.1883 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/10/gap` | 431.2235 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/11/expected` | 3200.1542 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/11/observed` | 2768.9307 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/11/gap` | 431.2235 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/12/expected` | 101914.9627 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/12/observed` | 144614.022 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/12/gap` | 42699.0593 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/13/expected` | 1213.2734 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/13/observed` | 849.2914 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/13/gap` | 363.982 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/14/expected` | 3295.4965 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/14/observed` | 2931.5145 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/14/gap` | 363.982 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/15/expected` | 128504.2238 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/15/observed` | 184323.1419 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/15/gap` | 55818.9181 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/16/expected` | 1529.8122 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/16/observed` | 1070.8685 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/16/gap` | 458.9437 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/17/expected` | 1831.54112 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/17/observed` | 1845.0695 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/17/gap` | -13.52838 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/18/expected` | 3705.7155 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/18/observed` | 3246.7718 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/18/gap` | 458.9437 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/19/expected` | 110465.2389 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/19/observed` | 158598.9682 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/19/gap` | 48133.7293 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/20/expected` | 1315.0624 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/20/observed` | 920.5437 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/20/gap` | 394.5187 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/21/expected` | 4276.0413 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/21/observed` | 3881.5226 | Recorded decimal string; original value preserved
`reports/site_examples.json` | `/questions/2/response/rows/21/gap` | 394.5187 | Recorded decimal string; original value preserved
