# Current submission files

| File | Status | Use |
|---|---|---|
| exathon-india-2026-pitch.pptx | CURRENT V3; editable native text | Pitch deck |
| exathon-india-2026-pitch.pdf | CURRENT V3; rendered slide export | Portable five-page deck |
| ../docs/deck/slide-01.png through slide-05.png | CURRENT V3; inspected slide previews | Quick review |
| [Final submission video](https://github.com/kushagragupta2005/gst-evidence-reconciliation/releases/tag/walkthrough-2026-10-29) | UPLOADED | Original MP4 recorded by Kushagra Gupta |
| ../docs/demo_script.md | Recording script | Reference |
| ../legacy/submission/ | HISTORICAL; obsolete V2/K=4 | Do not submit |

The deck is generated from result/report artifacts by `scripts/update_submission_deck.mjs` using the Codex bundled Artifact Tool (authoring dependency; not needed to run the app). The native PDF exporter failed in that runtime on a missing standard-font module, so the PDF was rendered from the inspected slide PNGs with `scripts/render_pitch_pdf.py`. Its editable source remains the PPTX. Optional public PDF-export dependencies are pinned in requirements-deliverables.txt. Neither PowerPoint nor a second machine has been used to verify the final deck.

The user-recorded final submission video is hosted on GitHub Releases. Portal submission has not been performed.
