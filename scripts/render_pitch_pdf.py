"""Render the inspected deck PNGs into a matching PDF; editable source is PPTX."""
from pathlib import Path
from reportlab.pdfgen import canvas
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'00_SUBMISSION/Pitch.pdf'
c=canvas.Canvas(str(out),pagesize=(960,540))
c.setTitle('GST Evidence — V3 synthetic evaluation')
c.setAuthor('Kushagra Gupta')
for i in range(1,6):
 image=ROOT/f'docs/deck/slide-{i:02}.png'
 if not image.exists():raise FileNotFoundError(image)
 c.drawImage(str(image),0,0,width=960,height=540);c.showPage()
c.save()
from pypdf import PdfReader
assert len(PdfReader(out).pages)==5
print('Rendered and reopened five-slide PDF; editable text remains in PPTX.')
