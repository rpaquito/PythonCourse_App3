import fpdf
import pandas as pd
from fpdf import FPDF


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    text = row["Topic"]
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=text, align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    pdf.ln(265)
    pdf.set_font(family="Times", size=8, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=text, align="R", ln=1)

# STUDENT EXERCISE
#    for x in range(20):
#        y = (14*x)+21
#        pdf.line(x1=10, y1=y, x2=200, y2=y)

    pages = int(row["Pages"])
    for y in range(pages-1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=text, align="R", ln=1)

# STUDENT EXERCISE
#        for x in range(20):
#            y = (14 * x) + 21
#            pdf.line(x1=10, y1=y, x2=200, y2=y)

pdf.output("output.pdf")
