import telebot
import requests
import time

# استبدل "YOUR_BOT_TOKEN" بالتوكن الخاص بالبوت
bot_token = '7441154483:AAEmqx-Ob3H3Cufux8Jo00Hdn4Iq-PntfJk'
bot = telebot.TeleBot(bot_token)

user_data = {}

# الخطوة الأولى: طلب عدد مرات الدورة
@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.reply_to(message, "مرحباً! كم عدد مرات الدورة؟")
    bot.register_next_step_handler(msg, process_cycle_count)

def process_cycle_count(message):
    try:
        cycle_count = int(message.text)
        user_data['cycle_count'] = cycle_count
        msg = bot.reply_to(message, "كم الوقت بين كل دورة (بالثواني)؟")
        bot.register_next_step_handler(msg, process_cycle_interval)
    except ValueError:
        msg = bot.reply_to(message, "الرجاء إدخال رقم صالح.")
        bot.register_next_step_handler(msg, process_cycle_count)

def process_cycle_interval(message):
    try:
        cycle_interval = int(message.text)
        user_data['cycle_interval'] = cycle_interval
        bot.reply_to(message, "شكراً! سيتم تنفيذ الطلبات الآن.")
        execute_requests(message)
    except ValueError:
        msg = bot.reply_to(message, "الرجاء إدخال رقم صالح.")
        bot.register_next_step_handler(msg, process_cycle_interval)

def execute_requests(message):
    cycle_count = user_data.get('cycle_count', 0)
    cycle_interval = user_data.get('cycle_interval', 0)
    
    url = "https://moakt.com/ar/inbox/extend"
    payload = "getJson=true"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        'sec-ch-ua-mobile': "?1",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'x-requested-with': "XMLHttpRequest",
        'save-data': "on",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://moakt.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://moakt.com/ar/inbox",
        'accept-language': "en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6",
        'priority': "u=1, i",
        'Cookie': "__utmz=213295240.1722176374.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=213295240.1597500418.1722176374.1722178668.1722188849.3; __utmc=213295240; __utmt=1; __gads=ID=2abd42b42e20e2b8:T=1722176654:RT=1722188846:S=ALNI_Ma7qqce6-p29-XAgc98G5Vd51J51g; __gpi=UID=00000ea767075e59:T=1722176654:RT=1722188846:S=ALNI_MZt9lqXU3hhPfEPyQ_0yzqBA7Lo8w; __eoi=ID=534120b796b835b6:T=1722176654:RT=1722188846:S=AA-AfjaCtFitlgehWG-Qc_MkBnte; tm_session=0f3d685121fb461e11eb078dd7c55cdf; __utmb=213295240.3.10.1722188849"
    }

    for _ in range(cycle_count):
        response = requests.post(url, data=payload, headers=headers)
        bot.send_message(message.chat.id, response.text)
        time.sleep(cycle_interval)

if __name__ == '__main__':
    bot.polling(none_stop=True)
