# Demo outline (2:45 target)

Solo participant: Kushagra Gupta. Use the live dashboard and keep the exact metrics below in sync with results.json. The existing MP4 predates this evaluation and should not be submitted as the replacement demo.

## 0:00–0:15 — Problem

Show this exact problem statement as the opening card:

> A GST officer can’t tell which factories are hiding production or inflating tax credits, because every document she checks is declared by the factory itself, while the independent evidence (power use, goods movement, supplier records, bank flows) sits in separate places and is never compared. If this worked, she would start each week with a short list of units whose paperwork contradicts physical reality, each contradiction spelled out, and honest-but-unusual factories cleared.

## 0:15–1:05 — Planted cheat and evidence note

Open a prioritised held-out case. Show the independent source families, the evidence timeline, and its validated case note. State that SQL flags the case and the note only summarizes evidence rows.

## 1:05–1:35 — Honest decoy

Open product-mix decoy F000142 for 2026-04. Show its one-source-family signal and explain why it stays outside the priority queue. This is review routing, not legal clearance.

## 1:35–2:00 — Follow-up question

Ask for the selected factory's dispatch gap by month. Show the guarded SELECT and the actual result table. State that the example runs in deterministic query mode; the LLM does not make flags.

## 2:00–2:30 — Held-out results and scale

Seed A selected the threshold; seed B was held out. Show 84.42% factory-month recall, 16.76% factory-month false-positive rate, 99.31% factory recall, 84.17% factory false-positive rate, and 629 missed cheat months. Open one miss and its reason. For the separate scale run, show 20,978,945 raw evidence rows loaded in 56.42 seconds. Counts and gap checksums matched before and after ledger materialisation; query-result caching was disabled for the query comparison.

## 2:30–2:45 — Limits and Germany

State that data is synthetic, the observed false-positive rate rules out operational targeting, and real bank and power data need lawful access and privacy controls. Germany is a possible adaptation requiring local validation; this prototype does not implement German VAT rules.

### Recording checks

- Keep the finished recording at or below 2:50.
- Do not present the old static-screen MP4 as a live walkthrough.
- Use the problem statement verbatim and check every number against results.json before recording.
- No Germany-specific statistics are used. If a future version adds them, cite the source on the slide or remove them.
