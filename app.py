import streamlit as st
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# إعدادات Telegram API
api_id = '9355923'  # استبدل بـ API ID الخاص بك
api_hash = '8ee56b7dae77248f59104e833a9ceaa0'  # استبدل بـ API Hash الخاص بك

st.title("Telegram Login")

# خطوات تسجيل الدخول
if 'step' not in st.session_state:
    st.session_state.step = 'phone'

client = None

if st.session_state.step == 'phone':
    phone = st.text_input("Enter your phone number:")
    if st.button("Send Code"):
        if phone:
            client = TelegramClient('session_name', api_id, api_hash)
            client.connect()
            client.send_code_request(phone)
            st.session_state.step = 'code'
            st.session_state.phone = phone
            st.session_state.client = client

if st.session_state.step == 'code':
    code = st.text_input("Enter the code sent to your phone:")
    if st.button("Verify"):
        phone = st.session_state.phone
        client = st.session_state.client
        try:
            client.sign_in(phone=phone, code=code)
            if client.is_user_authorized():
                st.success("Logged in successfully!")
                st.session_state.step = 'logged_in'
            else:
                st.error("Failed to log in.")
        except SessionPasswordNeededError:
            st.session_state.step = 'password'

if st.session_state.step == 'password':
    password = st.text_input("Two-step verification password:", type='password')
    if st.button("Login"):
        client = st.session_state.client
        client.sign_in(password=password)
        if client.is_user_authorized():
            st.success("Logged in successfully!")
        else:
            st.error("Failed to log in.")
