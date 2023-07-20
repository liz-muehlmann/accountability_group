import streamlit as st
from email import send_email

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("your email address")
    option = st.selectbox('What topic do you want to discuss?',
                           ("Job Inquiries", "Project Proposals","Other"))
    raw_message = st.text_area("Your message")

    message = f"""\
    Subject: New email from company profile about {option}
    From: {user_email}
    {raw_message}
    """
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")
