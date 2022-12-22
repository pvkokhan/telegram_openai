import telebot
import config
import openai
import logging
import datetime
import countfule
from utils import generate_response

bot = telebot.TeleBot(config.TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
openai.api_key = config.api_key

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, config.start_msg)

data = {}



@bot.message_handler(content_types=['text'])
def lalala(message):
    data['message'] = message

    now = datetime.datetime.now()
    date_time = now.strftime(config.date_time_format)

    with open("log.txt", "a") as f:
        f.write(
            f"\n\n{countfule.counter} request start \n{date_time} \nUser {message.from_user.username}: \n {config.separator} \n{message.text}\n {config.separator} \n\n")

    user_input = message.text
    response = generate_response(user_input)
    bot.send_message(message.chat.id, response)
    with open("log.txt", "a") as f:
        f.write(f"bot:\n {config.separator} \n {response} \n {config.separator} \n{countfule.counter} request end")
    countfule.counter += 1

    with open("countfule.py", "w") as f:
        f.write(f"counter = {countfule.counter}\n")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(e)
        bot.send_message(data['message'].chat.id, "Не совсем понимаю. Попробуйте переформулировать ваш запрос")