import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('stickers/HelloSti.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Привет!, {0.first_name}!".format(message.from_user, parse_mode="html"))
    bot.send_message(message.chat.id, "Вы не против немного пообщаться?👉👈")

@bot.message_handler(content_types=['text', 'sticker'])
def lalala(message):
    bot.send_message(message.chat.id, "Мой хозяин ещё не научил меня отвечать на подобные сообщения")

bot.polling(none_stop=True)