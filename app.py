import streamlit as st
import cloudscraper
import json

# إعداد واجهة المستخدم
st.title("تنفيذ طلبات HTTP")
mobile_number = st.text_input("الرجاء إدخال رقم الهاتف:")
email = st.text_input("الرجاء إدخال البريد الإلكتروني:")
name = st.text_input("الرجاء إدخال الاسم:")
password = st.text_input("الرجاء إدخال كلمة المرور:", type="password")
device_id = st.text_input("الرجاء إدخال معرف الجهاز:")
area_id = st.text_input("الرجاء إدخال معرف المنطقة:")
city_id = st.text_input("الرجاء إدخال معرف المدينة:")
dev_token = st.text_input("الرجاء إدخال رمز الجهاز:")

if st.button("تنفيذ الطلبات"):
    if mobile_number and email and name and password and device_id and area_id and city_id and dev_token:
        # إعداد الطلب الأول
        url_1 = "https://api.goooapp.com/api/Customers/Register"
        payload_1 = json.dumps({
            "DeviceId": device_id,
            "Email": email,
            "FlgLanguage": "ar-EG",
            "Mobile": mobile_number,
            "Name": name,
            "Password": password,
            "areaId": area_id,
            "cityId": city_id,
            "dev_token": dev_token
        })
        headers_1 = {
            'Host': "api.goooapp.com",
            'accept-language': "ar-EG",
            'content-type': "application/json; charset=UTF-8",
            'accept-encoding': "gzip",
            'user-agent': "okhttp/4.9.0"
        }

        # إعداد الطلب الثاني
        url_2 = "https://api.goooapp.com/api/Users/ForgetPassword"
        payload_2 = json.dumps({
            "Mobile": mobile_number
        })
        headers_2 = {
            'Host': "api.goooapp.com",
            'accept-language': "ar-EG",
            'content-type': "application/json; charset=UTF-8",
            'accept-encoding': "gzip",
            'user-agent': "okhttp/4.9.0"
        }

        # تنفيذ الطلبات باستخدام cloudscraper
        scraper = cloudscraper.create_scraper()

        response_1 = scraper.post(url_1, data=payload_1, headers=headers_1)
        response_2 = scraper.post(url_2, data=payload_2, headers=headers_2)

        # عرض النتائج
        st.write("الرد على الطلب الأول:")
        st.write(response_1.text)
        st.write("الرد على الطلب الثاني:")
        st.write(response_2.text)
    else:
        st.write("يرجى ملء جميع الحقول المطلوبة")
