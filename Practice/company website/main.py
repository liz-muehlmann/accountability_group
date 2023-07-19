import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
content = 'blah blah blah'
st.write(content)

st.header("Our Team")

col1, empty_col1, col2, empty_col2, col3 =  st.columns([1, 0.25, 1, 0.25, 1])

df =  pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].title() + " " +row["last name"].title())
        st.write(row["role"])
        st.image("images/"+row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.header(row["first name"].title() + " " +row["last name"].title())
        st.write(row["role"])
        st.image("images/"+row["image"])