import requests
import telebot
from user_agent import generate_user_agent
from time import sleep

token = input('[~] Enter Token :')
bot = telebot.TeleBot(token)
#trakos
@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text=f"*Hi {first},اهلا بك في بوت الاذكار 💜 .\nBy @ttrakos ~ @trprogram*",parse_mode="markdown")
@bot.message_handler(func=lambda m:True)
def Get(message):
    try:
        msg = message.text
        while 1:
        	bot.send_message(message.chat.id, text="Wait")
        	url = requests.get(f'https://sand65.ml/api/azkar.php').text
        	bot.send_message(message.chat.id,f'{url}')
        	q =1
    except:
        pass
bot.polling(True)
