import telebot
import requests
import json

bot = telebot.TeleBot('7718825492:AAFd-iKy6NzFmJ44xwY3f7xPpj0ZfIwqg60')
API = ('dc96cb452d4eb3e75dc7b981adca4cb6')

@bot.message_handler(commands=['start'] )
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть ! Напиши название города?')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')
        image = 'sun.png' if temp > 5.0 else 'sunny.png'


        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id,file)
    else:
        bot.reply_to(message, f'Город указан не верно, введите пожалуйста корректное название!')


bot.polling(none_stop=True)











