import telebot
import config
from random import choice

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    try:
        sti = open('stickers\HelloSti.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
    except:
        sti = open('/app/stickers/HelloSti.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Доброго времени суток, {0.first_name}!".format(message.from_user, parse_mode="html"))
    bot.send_message(message.chat.id, "Вы не против немного пообщаться?👉👈")

@bot.message_handler(content_types=['text', 'sticker'])
def lalala(message):
    List = ["Нет", "Да", "А хорошо сказано", 
            "Пожалуй", "Извиняюсь", "Пока.", 
            "ХАХАХАХХАХАХХАХАХАХАХХАХАХАХА",
            "Мой хозяин ещё не научил меня отвечать на подобные сообщения"]
    
    bot.send_message(message.chat.id, choice(List))

bot.polling(none_stop=True)