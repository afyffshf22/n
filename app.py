import telebot
from telebot import types
import requests
import re
import time
from bs4 import BeautifulSoup
import string
from colorama import Fore, init

init(autoreset=True)
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
B = Fore.BLUE
K = Fore.RESET

API_TOKEN = '6974710665:AAFrmjSsp9z7h_RLE-Z2lOMyPQqhKjqNa0k'
bot = telebot.TeleBot(API_TOKEN)
headers = {
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'x-requested-with': "XMLHttpRequest",
    'sec-fetch-site': "same-origin",
    'Cookie': "cookie_csrf_token=d93bc7e09a0fca4f62c046f090e57fd2; cookie_sessionhash=SHASH%3A66126b43e250337d73c65938d5138a1c; cookie_setlang=en"
}

fetch_messages_enabled = False

last_messages = []

def fetch_cleaned_domains():
    try:
        url = "https://m.kuku.lu/en.php"
        response = requests.get(url, headers=headers, timeout=100)
        response.raise_for_status()
        domains = re.findall(r'@[\w.-]+', response.text)
        at_rules = ['@media', '@supports', '@-webkit-keyframes', '@keyframes', '@tensi.org', '@kukusama']
        cleaned_domains = [domain for domain in domains if not any(at_rule in domain for at_rule in at_rules)]
        return cleaned_domains
    except requests.exceptions.RequestException:
        return []

def reserve_domain(username, domain):
    try:
        url = "https://m.kuku.lu/index.php"
        params = {
            'action': "addMailAddrByManual",
            'by_system': "1",
            'csrf_token_check': "d93bc7e09a0fca4f62c046f090e57fd2",
            'newdomain': domain.strip('@'),
            'newuser': username
        }
        response = requests.get(url, params=params, headers=headers, timeout=100)
        response.raise_for_status()
        response_text = response.text
        if "NG:Sorry, the account name is already in use." in response_text:
            return None, "Sorry, the username is unavailable. Please enter a different username. /start    ادخل اسم مختلف"
        elif "NG:Sorry, the domain name is not available." in response_text:
            return None, "Sorry, the domain name is not available. Please choose a different domain. /start"
        else:
            return username, f"{username}@{domain.strip('@')}"
    except requests.exceptions.RequestException:
        return None, "Failed to reserve domain. Please check your internet connection."

def clean_text(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    allowed_chars = string.ascii_letters + string.digits + string.punctuation + ' ' + ''.join(chr(i) for i in range(0x0600, 0x06FF)) 
    cleaned_text = ''.join(c for c in text if c in allowed_chars)
    return cleaned_text

def fetch_messages(email):
    try:
        url = "https://m.kuku.lu/smphone.app.recv._ajax.php"
        params = {
            'q': email,
            'nopost': "1",
            'csrf_token_check': "d93bc7e09a0fca4f62c046f090e57fd2",
            'csrf_subtoken_check': "06ed5512c403eeb497050076eb059ad4",
            '_': "1722264747698"
        }
        response = requests.get(url, params=params, headers=headers, timeout=100)
        response.raise_for_status()
        response_text = response.text

        pattern = re.compile(r"openMailData\('(\d+)',\s*'([^']*)',\s*'([^']*)'\)")
        matches = pattern.findall(response_text)

        if matches:
            messages = []
            for match in matches:
                mail_id, token, additional_info = match
                message_details = get_message_details(mail_id, token)
                messages.append(message_details)
            return messages
        else:
            return ["لا يوجد رسائل   جار التحديث   🤌🤏"]
    except requests.exceptions.RequestException:
        return ["Failed to fetch messages. Please check your internet connection. /start"]

def get_message_details(mail_id, token):
    try:
        url = "https://m.kuku.lu/smphone.app.recv.view.php"
        payload = {
            'num': mail_id,
            'key': token,
            'noscroll': "1"
        }
        response = requests.post(url, data=payload, headers=headers, timeout=100)
        response.raise_for_status()
        cleaned_response = clean_text(response.text)
        return cleaned_response
    except requests.exceptions.RequestException:
        return "Failed to get message details. Please check your internet connection. /start"

def check_existing_email(email):
    try:
        url = "https://m.kuku.lu/smphone.app.index._addrlist.php"
        params = {
            't': "1722267814520",
            'nopost': "1",
            '_': "1722267793252"
        }
        response = requests.get(url, params=params, headers=headers, timeout=100)
        response.raise_for_status()
        return email in response.text
    except requests.exceptions.RequestException:
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global fetch_messages_enabled
    fetch_messages_enabled = False
    bot.reply_to(message, 'Welcome! Use /new to create a new email or /existing to use an existing email.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('/start'), types.KeyboardButton('/stop'))
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(commands=['stop'])
def stop_fetching(message):
    global fetch_messages_enabled
    fetch_messages_enabled = False
    bot.reply_to(message, 'Fetching messages stopped. Use /start to resume.')

@bot.message_handler(commands=['new'])
def new_email(message):
    cleaned_domains = fetch_cleaned_domains()
    if not cleaned_domains:
        bot.reply_to(message, "No available domains found.  /start")
        return

    bot.send_message(message.chat.id, "Please enter your desired Gmail username: ")
    bot.register_next_step_handler(message, process_username, cleaned_domains, new=True)

@bot.message_handler(commands=['existing'])
def existing_email(message):
    cleaned_domains = fetch_cleaned_domains()
    if not cleaned_domains:
        bot.reply_to(message, "No available domains found. /start /n اختر رقم اخر")
        return

    bot.send_message(message.chat.id, "Please enter your Gmail username:")
    bot.register_next_step_handler(message, process_username, cleaned_domains, new=False)

def process_username(message, cleaned_domains, new):
    username = message.text.strip()
    if not username.isalnum():
        bot.send_message(message.chat.id, "Invalid username. Please enter a valid alphanumeric username. /start")
        return
    
    domain_list = ""
    for i in range(0, len(cleaned_domains), 2):
        if (i + 1) < len(cleaned_domains):
            domain_list += f"{i+1}. {cleaned_domains[i]}             {i+2}. {cleaned_domains[i+1]}\n"
        else:
            domain_list += f"{i+1}. {cleaned_domains[i]}\n"

    bot.send_message(message.chat.id, f"Choose a domain from the following list:\n{domain_list}")
    bot.register_next_step_handler(message, process_domain, username, cleaned_domains, new)

def process_domain(message, username, cleaned_domains, new):
    try:
        domain_index = int(message.text.strip()) - 1
        if 0 <= domain_index < len(cleaned_domains):
            selected_domain = cleaned_domains[domain_index]
            if new:
                reserved_username, response_message = reserve_domain(username, selected_domain)
                if reserved_username:
                    email = f"{reserved_username}{selected_domain}"
                    bot.send_message(message.chat.id, f"Email created: {email}")
                    fetch_and_display_messages(message, email)
                else:
                    bot.send_message(message.chat.id, response_message)
            else:
                email = f"{username}{selected_domain}"
                if not check_existing_email(email):
                    reserved_username, response_message = reserve_domain(username, selected_domain)
                    if reserved_username:
                        email = f"{reserved_username}{selected_domain}"
                        bot.send_message(message.chat.id, f"Email created: {email}")
                        fetch_and_display_messages(message, email)
                    else:
                        bot.send_message(message.chat.id, response_message)
                else:
                    bot.send_message(message.chat.id, f"Email found: {email}")
                    fetch_and_display_messages(message, email)
            cleaned_domains.clear()  # Clear the domain list
        else:
            bot.send_message(message.chat.id, "Invalid choice, please try again.")
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a valid number.")

def fetch_and_display_messages(message, email):
    global fetch_messages_enabled
    fetch_messages_enabled = True
    displayed_messages = []
    while fetch_messages_enabled:
        messages = fetch_messages(email)
        
        # حذف الرسائل القديمة
        for chat_id, message_id in displayed_messages:
            try:
                bot.delete_message(chat_id, message_id)
            except telebot.apihelper.ApiException as e:
                print(f"Failed to delete message {message_id}: {e}")

        # عرض الرسائل الجديدة وتخزين معرفاتها
        displayed_messages = []
        for msg in messages:
            sent_message = bot.send_message(message.chat.id, msg)
            displayed_messages.append((sent_message.chat.id, sent_message.message_id))
        
        time.sleep(20)

# تهيئة البوت والبدء في الاستماع للرسائل
if __name__ == "__main__":
    bot.polling()
