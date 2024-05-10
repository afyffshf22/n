import streamlit as st
import requests

st.title('Verify Twilio')

phone_number = st.text_input('Enter your phone number (e.g., 01152555928):')

if st.button('Verify'):
    url = "https://egypt.yallamotor.com/verify-twilio/555555"

    params = {
        'phone': phone_number,
        'channeltype': "call",
        'locale': "en"
    }

    headers = {
        'User-Agent': "Mo",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua-mobile': "?1",
        'sec-fetch-site': "same-origin",
        'referer': "https://egypt.yallamotor.com/ar/login"
    }

    response = requests.get(url, params=params, headers=headers)

    st.text(response.text)
