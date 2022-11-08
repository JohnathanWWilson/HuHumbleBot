import telebot
import config
from random import choice, randint

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    List_Sti = ['HelloSti.webp', 'Hello1Sti.webp', 'Hello2Sti.webp']

    try:
        sti = open(f'stickers/{choice(List_Sti)}', 'rb')
    except:
        sti = open(f'/app/stickers/{choice(List_Sti)}', 'rb')
        
    bot.send_sticker(message.chat.id, sti)


    bot.send_message(message.chat.id, "Доброго времени суток, {0.first_name}!".format(message.from_user, parse_mode="html"))
    bot.send_message(message.chat.id, "Вы не против немного пообщаться?👉👈")

@bot.message_handler(content_types=['text', 'sticker'])
def lalala(message):
    List_Slov = ["Нет", "Да", "А хорошо сказано", 
                "Пожалуй", "Извиняюсь", "Пока.", 
                "ХАХАХАХХАХАХХАХАХАХАХХАХАХАХА",
                "Мой хозяин ещё не научил меня отвечать на подобные сообщения"]

    List_Sti = ['BlinSti.webp', 'CringeSti.webp', 'DiCaprioSti.webp', 'EeSti.webp', 
                'Hehe1Sti.webp', 'HeheSti.webp', 'IdeaSti.webp', 'NoSti.webp', 
                'OSti.webp', 'Rock1Sti.webp', 'RockSti.webp', 'TiltSti.webp', 
                'YameteSti.webp', 'YameteSti1.webp', 'YesSti.webp']

    try:
        sti = open(f'stickers/{choice(List_Sti)}', 'rb')
    except:
        sti = open(f'/app/stickers/{choice(List_Sti)}', 'rb')

    if randint(0, 1) == 0:
        bot.send_message(message.chat.id, choice(List_Slov))
    else:
        bot.send_sticker(message.chat.id, sti)

bot.infinity_polling(timeout=10, long_polling_timeout = 5)