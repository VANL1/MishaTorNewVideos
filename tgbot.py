import telebot
from main import last_video
from time import sleep

bot = telebot.TeleBot('6903636918:AAHDnwtWYIZNTNVzQexEC-9uQsp26RdA6b8')

@bot.message_handler(commands=['start'])
def wlcome(message):
    bot.send_message(message.chat.id, f'Привет! Это бот который будет отпралять оповещения о новых видео МИШИ ТОРА!!!')
    sleep(2)
    bot.send_message(message.chat.id, f'👇Вот его последнее видео👇')
    sleep(1)
    bot.send_message(message.chat.id, f'https://www.youtube.com/watch?v={last_video()}')


bot.infinity_polling()