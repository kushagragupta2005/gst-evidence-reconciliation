# Current deck content and sources

The editable PPTX and PDF in deliverables/ use V3-B/V3-C, threshold 0.05 and K=3. The source deck under legacy/submission/ is obsolete and must not be submitted.

**How is this different from invoice matching?**

It reconciles declarations with material/power proxies, movement, supplier returns and bank flows. There is no benchmark against commercial fraud systems and no claim that the approach is unprecedented.

**Is this a machine-learning fraud classifier?**

No. Six deterministic SQL checks form four source families. SQL flags a month when at least two families fire. An optional LLM can explain evidence only; displayed notes use the deterministic fallback.

**What are the primary and confirmation results?**

V3-B monthly recall 81.14%, FPR 2.20%, precision 85.56%. V3-C monthly recall 81.24%, FPR 2.28%, precision 85.01%. All are synthetic and have factory-cluster intervals in the artifacts.

**Why trust synthetic results?**

They allow recovery of known planted scenarios to be measured. Held-out seeds share the same generator; intervals do not cover generator bias or real-taxpayer error. They do not establish operational accuracy.

**How was calibration done?**

V3-A alone selected threshold 0.05 and K=3. B and C use frozen choices. No new threshold was tuned in the judge audit; a stale live setting was repaired to the already-published value.

**What did the audit discover in Live mode?**

The schema default had been 0.10 while offline evaluation used 0.05. A user-approved settings-only repair restored 0.05. Every live monthly signal count and flag now matches saved V3-C, and API health rejects mismatched live decisions.

**What does the factory queue mean?**

A factory enters after at least K=3 prioritised months. V3-C queue size 605; recall 81.94%, FPR 0.89%, precision 97.52%. This differs from monthly classification.

**What is the top-50 precision?**

Monthly macro precision is 75.00%. The generator has no active cheats in Jan–Mar, whose small returned queues are false alarms; Apr–Dec each reach 100% in the top 50. This is a synthetic monthly snapshot statistic, not measured weekly effectiveness.

**Why is zero wrong-clears not proof of safety?**

Zero events span 720 active-cheat factories and 3950 active cheat months in C. Approximate factory-level rule-of-three upper bound is 0.42%, assuming independent factories. Verification labels come from the generator; sophisticated forgers and cluster-bootstrap wrong-clear intervals remain untested.

**What does Exasol actually do?**

Exasol Personal is the primary database for joins, aggregates, stock/baseline windows, reconciliation views, source-family prioritisation and guarded follow-up SELECTs. Loop links are evidence context; loop-only/ring detection is not implemented. UDF and MCP execution are not demonstrated.

**Was Exasol faster than DuckDB?**

No in the current recorded comparison: stock medians Exasol 0.169s, DuckDB 0.006s. Counts and gap sums match. Current dataset: 2,400 factories, 172,800 feature rows. Physical plans and load coverage differ. The 20.98M-row run is historical.

**What are the current Live and security results?**

The current guarded API smoke passed all three intents, notes, activity, injection/unknown-intent rejection and 8 parallel questions. Measured p95 4.096s includes the new protocol validation. The reader cannot read database truth. Public Pages always uses recorded snapshots; real power/bank access would require lawful privacy controls.
