# GST Evidence

### [Pitch PDF](00_SUBMISSION/Pitch.pdf) · [Pitch PPTX](00_SUBMISSION/Pitch.pptx) · [Watch video](https://github.com/kushagragupta2005/gst-evidence-reconciliation/releases/tag/walkthrough-2026-10-29) · [Open demo](https://kushagragupta2005.github.io/gst-evidence-reconciliation/)

**Evidence-backed GST investigations. Built on Exasol Personal.**

> A GST officer can’t tell which factories are hiding production or inflating tax credits, because every document she checks is declared by the factory itself, while the independent evidence (power use, goods movement, supplier records, bank flows) sits in separate places and is never compared. If this worked, she would start each week with a short list of units whose paperwork contradicts physical reality, each contradiction spelled out, and honest-but-unusual factories cleared.

**Kushagra Gupta · Solo project · ExaThon India 2026 · Track 01: Money, Risk & Regulation**

## From scattered records to a case an officer can explain

GST Evidence compares declarations with goods movement, supplier records, electricity use and bank flows. It turns contradictions into a review list with the supporting numbers attached.

- **Reconcile:** six SQL checks across production, movement, supplier and financial evidence.
- **Corroborate:** two source families must fire before a month is prioritised; three prioritised months put a factory in the review queue.
- **Explain:** inspect expected values, observed values, gaps and a validated case note. Try a [caught cheat, an honest exception and a miss](https://kushagragupta2005.github.io/gst-evidence-reconciliation/cases/).

SQL determines priority. No ML model or LLM decides flags. The demonstrated notes use a deterministic fallback; an LLM option is implemented separately.

## Results you can inspect

**2,400 synthetic factories · 12 months · 28,800 factory-months per seed.** V3-A chose the threshold and queue rule; V3-B and V3-C tested those frozen choices.

| Held-out test | Cheating months caught | Honest months falsely flagged | Precision |
|---|---:|---:|---:|
| V3-B · primary | 81.14% | 2.20% | 85.56% |
| V3-C · confirmation | 81.24% | 2.28% | 85.01% |

[Explore results and confidence intervals](https://kushagragupta2005.github.io/gst-evidence-reconciliation/results/) · [Primary report](results.json) · [Confirmation report](reports/v3_c_results.json)

All data is synthetic. These are scenario-recovery results, not real-world fraud accuracy. Alerts support human review. Verification assumptions, measurement scope and remaining work are documented in the [project guide](docs/PROJECT_GUIDE.md#limits).

## Run it

Requires Git, Make and Python 3.12+. The recorded demo and offline audit need no database or API key.

```sh
git clone https://github.com/kushagragupta2005/gst-evidence-reconciliation.git
cd gst-evidence-reconciliation
sh scripts/bootstrap.sh
make all
make site
```

Open **http://127.0.0.1:8081/**. For live Exasol setup, architecture, reproduction and verification details, use the [project guide](docs/PROJECT_GUIDE.md).

## Project

[Submission materials](00_SUBMISSION/) · [Project guide](docs/PROJECT_GUIDE.md) · [Source](src/) · [SQL checks](sql/) · [Synthetic evaluation inputs](data/audit/README.md)

Source is [MIT-licensed](LICENSE). [Dependency licences and tool disclosures](docs/licences/) include Exasol Personal's separate EULA and the optional OpenAI API's service terms. All records come from the seeded generator; there are no real taxpayer records or live tax, power or bank integrations. Real use needs lawful access and human review.

OpenAI Codex coding assistants helped build and audit the project. Kushagra Gupta is responsible for final review and submission.
