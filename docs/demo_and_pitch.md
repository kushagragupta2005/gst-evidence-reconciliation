# Submission demo and pitch notes

## Three-minute demo sequence

Kushagra Gupta built and presents this project solo.

| Time | Show | Talk track |
| --- | --- | --- |
| 0:00–0:31 | Opening problem statement | Read the exact problem sentence. |
| 0:31–1:04 | A ranked planted-cheat case | Show expected, observed, gap, source evidence and the evidence-only case note for F000039. |
| 1:04–1:26 | An honest decoy | Show F000002, a product-mix-shift decoy cleared with zero discrepancy signals. The demo label is explicitly marked as an evaluation label. |
| 1:26–1:57 | Scale run | Show 120,000 factories, 360,000 monthly rows, 2.51 million evidence rows, 100% cheat catch rate, 0% honest-decoy false-positive rate and the 1.407-second prioritized-case query. State that these are synthetic results on one local 8 GB VM. |
| 1:57–2:17 | Germany connection | Explain the shared VAT carousel pattern and distinguish this prototype from German tax-rule coverage. |

The included narrated MP4 is 2 minutes 17 seconds, below the three-minute event limit. Its custom case and decoy screens use the same scored SQL rows shown in the dashboard.

## Pitch deck order

1. **Problem statement** — open with the exact README sentence, without a product name or technology.
2. **Evidence gaps** — show declarations beside physical and third-party evidence: material and power, e-way bills and invoices, stock, supplier records, and bank flows.
3. **Reconciliation method** — four SQL check families, evidence rows with expected/observed/gap, and a two-independent-signal threshold. Keep the LLM after the queue as a note writer.
4. **Measured prototype** — show 24,000/24,000 cheats caught, 0/24,000 honest decoys prioritised, 2.51 million loaded evidence rows, and the 1.407-second prioritised-case query from the full-scale run. Label these as synthetic, local-run results.
5. **Related pattern in Germany** — connect the supply-chain and invoice-trace idea to reported carousel VAT cases. Keep the jurisdictional and legal differences explicit.

## Germany slide research

- [EPPO, Germany: suspected €18 million VAT carousel fraud, 13 May 2026](https://www.eppo.europa.eu/media/news/germany-eppo-orders-searches-and-arrest-probe-eu18-million-vat-fraud-2026-05-13_en): reported purchases from German suppliers and sales to missing traders in other EU countries.
- [European Commission, VAT carousel fraud](https://taxation-customs.ec.europa.eu/taxation/vat/fight-against-vat-fraud/vat-carousel-fraud_en): explains the EU missing-trader mechanism and the use of cross-border B2B transactions.

