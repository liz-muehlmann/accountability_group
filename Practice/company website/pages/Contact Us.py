import streamlit as st
from email import send_email
import pandas

df = pandas.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("your email address")
    option = st.selectbox('What topic do you want to discuss?',
                          df["topic"])
    raw_message = st.text_area("Text")

    message = f"""\
Subject: New email from company profile about {option}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")
