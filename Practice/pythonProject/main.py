# App 4
# Creating a pdf template generation app
# from csv to PDF

from fpdf import FPDF

import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

#The topics become headers for each page

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)     #RGB combination for grew
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
         ln=1)
    pdf.line(10,22,200,22)

# next I want to create the number of pages that the csv file shows
# use for loop
# x=3
# for i in range(x):
# print("Hello")
    for i in range(row["Pages"] - 1):
        pdf.add_page()


pdf.output("output.pdf")

