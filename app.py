import requests
import telebot
import time

# مرر التوكن إلى المكتبة
bot = telebot.TeleBot('7060312406:AAGqNhOh6s4RVufoV4Qp1eq8D0DNNDfDiZs')

# ارسال رسالة الى هذا ال id
chat_id = 5939899289

# دالة لجلب البيانات من الموقع
def fetch_data():
    url = "https://moakt.com/ar/inbox/extend"
    payload = "getJson=true"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua': "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://moakt.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://moakt.com/ar/inbox",
        'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6",
        'priority': "u=1, i",
        'Cookie': "__utmz=213295240.1716310207.25.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=213295240.1559448545.1709239546.1716549903.1716629676.29; __utmt=1; __gads=ID=1d223ca717efeadc:T=1709239555:RT=1716631015:S=ALNI_Ma6Cp3tFOzfUR0cdX4GXo4XCL1A8g; __gpi=UID=00000d373df316dc:T=1709239555:RT=1716631015:S=ALNI_MZechVD-lq-3ECTKieSVLaJTEFDuQ; __eoi=ID=8b881da4c3755c5f:T=1709239555:RT=1716631015:S=AA-Afjbgz9J7pBxKE5yRxVDSEARl; __utmc=213295240; tm_session=317ebe6c68523405ec659ccce7444e57; __utmb=213295240.10.10.1716629676"
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.text

# دالة لإرسال البيانات المجمعة بشكل دوري
def send_periodic_updates():
    while True:
        data = fetch_data()
        bot.send_message(chat_id, data)
        time.sleep(10 * 60)  # الانتظار لمدة 10 دقائق

# دالة للاستجابة للرسائل وإعادة إرسالها
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

# بدء تشغيل الاستماع للرسائل في خيط منفصل
import threading
threading.Thread(target=send_periodic_updates).start()

# بدء الاستماع للرسائل
bot.polling()
