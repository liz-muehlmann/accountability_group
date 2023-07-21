# App 4
# Creating a pdf template generation app
# from csv to PDF

from fpdf import FPDF

import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")



#The topics become headers for each page

for index, row in df.iterrows():
    pdf.add_page()              # the parent page

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)     #RGB combination for grew
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
         ln=1)
    pdf.line(10,22,200,22)

    # set the footer
    pdf.ln(265)         #line break
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # line coordinates
    x = 22
    while x < 265:
        x = x + 7
        pdf.line(10, x, 200, x)

    # next I want to create the number of pages that the csv file shows
    # use for loop
    # x=3
    # for i in range(x):
    # print("Hello")
    for i in range(row["Pages"] - 1):
        pdf.add_page()
    # this is called the nested loop

    #set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=10, txt = row["Topic"], align = "R")

    x = 22
    while x < 265:
        x = x + 7
        pdf.line(10, x, 200, x)




pdf.output("output.pdf")

