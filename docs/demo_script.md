# Demo recording script — owner: Kushagra Gupta

**Status: the user-recorded final video is uploaded; see [the release](https://github.com/kushagragupta2005/gst-evidence-reconciliation/releases/tag/walkthrough-2026-10-29). This is a reference script, not a transcript or duration certificate.** This script targets 2:45. All quantities below come from the current artifact files. Public Pages uses recorded examples; a local API can execute the guarded follow-ups live. Always state which mode is shown.

## 0:00–0:20 — Problem

Display the exact statement; do not try to read every word at speed:

> A GST officer can’t tell which factories are hiding production or inflating tax credits, because every document she checks is declared by the factory itself, while the independent evidence (power use, goods movement, supplier records, bank flows) sits in separate places and is never compared. If this worked, she would start each week with a short list of units whose paperwork contradicts physical reality, each contradiction spelled out, and honest-but-unusual factories cleared.

Say: “GST Evidence gives an officer a review list when declarations contradict evidence from other sources.”

## 0:20–1:00 — Caught cheat

Open Cases, choose Caught cheat: F000902, 2026-05. Show the source families, expected/observed/gap rows and validated deterministic note. Explain that SQL determines priority and the note explains evidence. Every record is synthetic.

## 1:00–1:25 — Honest exception and a miss

Choose Honest exception: F000016, 2026-04. Show the generated verification record supporting its machinery change. Choose Miss: F000025, 2026-08; only movement fires, so the planted cheat is review-only. Verification itself is simulated.

## 1:25–1:50 — Ask and inspect SQL

Choose “Dispatch gap by month”. Show the fixed SELECT and returned evidence. Public site: say “recorded response”. Local verified API: say “executed now through the restricted reader”. Do not claim an MCP or LLM live demo.

## 1:50–2:20 — Results and actual performance

Choose V3-C. Monthly recall 81.24%; false-positive rate 2.28%. V3-A froze threshold 0.05 and K=3. C missed 741 active cheat months. Wrong-clears are zero of 720 active-cheat factories, with approximate upper bound 0.42% under an independence assumption, using generated verification labels. System shows 172,800 current feature rows and an honest DuckDB comparison; the large historical workload is not a fresh run.

## 2:20–2:45 — Limits and close

Synthetic only. Human review, not an enforcement decision. Forger testing, ablation/wrong-clear intervals, second-machine reproduction and a fresh full-scale load remain open. Lawful access to tax, power and bank data is future work. Germany is only an unvalidated possible adaptation, with no figures or deployment claimed.

## Before uploading

Use a screen recording of the actual public or local site; keep the mode label visible. Check duration, sound and source figures. Do not use a stale MP4 or simulate a query. Put the final user-recorded video URL in docs/PROJECT_GUIDE.md and confirm its access permissions. The assistant has not submitted the portal form.
