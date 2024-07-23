import streamlit as st
import cloudscraper
import json

# إعداد واجهة المستخدم
st.title("تحقق من رقم الهاتف")
phone_number = st.text_input("الرجاء إدخال رقم الهاتف:")

if st.button("تحقق"):
    if phone_number:
        url = "https://api.halan.io/api/v1/client/register/check"
        payload = json.dumps({
            "phoneNumber": phone_number
        })
        headers = {
            'User-Agent': "okhttp/4.8.0",
            'Accept-Encoding': "gzip",
            'selectedcountry': "",
            'storeversion': "5.5.2",
            'version': "350",
            'content-type': "application/json; charset=UTF-8"
        }
        scraper = cloudscraper.create_scraper()
        response = scraper.post(url, data=payload, headers=headers)
        st.write(response.text)
    else:
        st.write("يرجى إدخال رقم الهاتف")
