### Main code of the app "Generating PDF files via Python"
## Importing...
from pathlib import Path
from fpdf import FPDF
import pandas as pd
import glob

## Reading the filepaths
filepaths = glob.glob("invoices\\*.xlsx")

## Running script for each Excel file
for filepath in filepaths:
    ## Getting filename
    filename = Path(filepath).stem

    ## Creating a dataframe for each file
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    ## Creating the pdf variable for Python to make the PDF file with
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    ## Adding invoice number.
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=24, txt=f"Invoice number {invoice_nr}", ln=1)

    ## Adding date
    date = filename.split("-")[1]
    pdf.cell(w=0, h=24, txt=f"Date {date}", ln=1)

    ## Adding columns
    raw_columns = df.columns
    columns = [item.title().replace("_", " ", -1) for item in raw_columns]
    pdf.set_font(family="Times", style="B", size=14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1, align="C")
    pdf.cell(w=50, h=8, txt=columns[1], border=1, align="C")
    pdf.cell(w=50, h=8, txt=columns[2], border=1, align="C")
    pdf.cell(w=40, h=8, txt=columns[3], border=1, align="C")
    pdf.cell(w=25, h=8, txt=columns[4], border=1, align="C", ln=1)

    ## Adding rows
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=12)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1, align="C")
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1, align="C")
        pdf.cell(w=50, h=8, txt=str(row["amount_purchased"]), border=1,
                 align="C")
        pdf.cell(w=40, h=8, txt=f"$ {str(row['price_per_unit'])}", border=1,
                 align="C")
        pdf.cell(w=25, h=8, txt=f"$ {str(row['total_price'])}", border=1, align="C",
                 ln=1)

    ## Adding the final cost
    pdf.ln(h=10)
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=40, h=8, txt="Final Price: ", align="C")
    pdf.cell(w=25, h=8, txt=f"$ {str(df['total_price'].sum())}", align="C", ln=1)

    ## Exporting the PDF file which can be accessed by the user.
    pdf.output(f"PDFs\\{filename}.pdf")
