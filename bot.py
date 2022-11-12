import telebot
import config, dictionary
import answers as ans
import questions as qu
from random import choice, randint
from fuzzywuzzy import fuzz, process


bot = telebot.TeleBot(config.TOKEN) # Импорт токена для инициализации бота


# Функция открытия смайлика (либо с локального компьютера, либо с облака)
def ans_sti(x):
    try:
        sti = open(f'stickers/{choice(x)}', 'rb')
    except:
        sti = open(f'/app/stickers/{choice(x)}', 'rb')
    return sti


# Рандомный выбор, ответить стикером или сообщением 
def ans_or_sti(message, word, sti):
    if randint(0, 1) == 0:
        bot.send_message(message, choice(word))
    else:
        bot.send_sticker(message, ans_sti(sti))    


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, ans_sti(ans.Hello_Sti))
    bot.send_message(message.chat.id, "Доброго времени суток, {0.first_name}!".format(message.from_user, parse_mode="html"))
    bot.send_message(message.chat.id, "Вы не против немного пообщаться?👉👈")


@bot.message_handler(content_types=['text', 'sticker'])
def lalala(message):
    resemblance = process.extractOne(message.text, dictionary.Lang)
    if resemblance[1] > 80:
        if resemblance[0] in qu.Yes_Qu:
            ans_or_sti(message.chat.id, ans.Yes_Ans, ans.Yes_Ans_Sti)
        elif resemblance[0] in qu.How_Are_U_Qu:
            ans_or_sti(message.chat.id, ans.How_Are_U_Ans, ans.How_Are_U_Ans_Sti)
        elif resemblance[0] in qu.Who_Are_U_Qu:
            bot.send_message(message.chat.id, choice(ans.Who_Are_U_Ans))
        elif resemblance[0] in qu.Psychologist_Qu:
            bot.send_message(message.chat.id, choice(ans.Psychologist_Ans))
        elif resemblance[0] in qu.How_Old_Are_U_Qu:
            bot.send_message(message.chat.id, choice(ans.How_Old_Are_U_Ans))
        elif resemblance[0] in qu.What_Qu:
            bot.send_message(message.chat.id, choice(ans.What_Ans))
        elif resemblance[0] in qu.What_Are_U_Doing_Qu:
            bot.send_message(message.chat.id, choice(ans.What_Are_U_Doing_Ans))
    else:
        ans_or_sti(message.chat.id, ans.Not_Understood_Ans, ans.List_Sti)


bot.infinity_polling(timeout=10, long_polling_timeout = 5)