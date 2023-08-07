import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    text = row["Topic"]
    pdf.set_font(family="Times", size=12, style="B")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=24, txt=text, align="L", ln=1)
    pdf.line(x1=10, x2=21, y1=200, y2=21)

pdf.output("output.pdf")
