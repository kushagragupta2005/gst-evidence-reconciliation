# Evaluation protocol

The old perfect-score benchmark is superseded. Never compare its three-month scenario counts with this benchmark.

- Generator seed A = 20261019, B = 20261020, 2,400 factories per seed, 12 months. Each cheat factory has 3–8 active months, drawn from April–December. Inactive months count as negatives. Annual factory truth is any active cheat month; annual prediction is any prioritised month.
- Scenarios: hidden production, ITC inflation (with explicitly represented three-party supplier ownership cycles), and reused e-way documents. Intensities: 5%, 15%, 30%. A quarter of cheat factories in expectation are evasive; realised counts are measured. Evasive cases suppress cross-source corroboration; incidental noise may still produce a second signal.
- Decoys: machinery upgrades, product mix, extended hours, seasonal raw-stock build, missing onboarding returns, and lumpy payments. Some single-source anomalies remain review-only. That is exclusion from the priority queue, not a finding of innocence.
- Production groups material, power, and stock together. Movement groups invoice gaps and document reuse. Supplier and financial sources are the other two groups. Multiple discrepancies from the same family count once. These are distinct source families, not a statistical independence guarantee.
- Grid: 0.025, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20, 0.25, 0.30, 0.40, 0.55. Select minimum `(1 - recall + FPR) / 2` on A at factory-month level; choose the larger threshold on a tie. No desired accuracy target, no B-driven threshold adjustment. Threshold choice and classification heuristic are different: a fixed 0.08 power ratio selects the descriptive evidence class only.
- Report B at the selected threshold. The B sensitivity curve is descriptive, not calibration. Bootstrap resamples factories and preserves their months. Metrics are conditional on the fitted threshold, not nested training uncertainty. Degenerate intervals in small subgroups are not safety guarantees.
- Precision@k is the mean over nonempty monthly queues of up to k prioritised factories, not daily/weekly operational precision. A separate weekly dataset is not fabricated. Queue bootstrap repeats the ranking with resampled clusters (duplicates represent resampled factory copies).
- Confusion rows are planted discrepancy descriptions, columns are the strongest nonfinancial observed discrepancy (financial-only: needs human review). A sixth column records no signal; clean truth months are excluded. Class predictions are reported even if fewer than two source families fire. Honest decoys can have a mismatch class without becoming fraud allegations.
- Truth.csv stays outside the detection schema and is loaded only into the
  evaluator-only `GST_EVALUATION` schema when explicitly requested. Factory
  scenario metadata is not loaded into the detector database. Production uses
  assumed 80% yield and four kWh/unit; these deliberately imperfect assumptions
  cause legitimate discrepancies.
- Raw evidence rows count monthly production, invoices, purchase invoices, shipment observations, returns, and bank transactions. They exclude truth and factory/supplier/machine dimensions. Derived feature rows are reported separately and are never added to raw row counts.
- Synthetic monthly aggregates simplify allocation, supplier ownership, units, bank timing, and observability. All numerical results are scenario-recovery measurements, not tax-fraud prevalence or real-world validation.
