### Code project of the real life app where I make the lines to write text.
## Importing...
from pathlib import Path
from fpdf import FPDF
import glob

## Reading the text files fro Text Files
filepaths = glob.glob("Text Files\\*.txt")

## Calling th e FPDF class from library.
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths:
    filename = Path(filepath).stem
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=24, txt=filename.title(), align="C", ln=1)

    with open(filepath,"r") as file:
        pdf.set_font(family="Times", style="B", size=12)
        pdf.multi_cell(w=0, h=7, txt=file.read())


## Creating the existing copy of the file which the users can interact with.
pdf.output("Output.pdf")
