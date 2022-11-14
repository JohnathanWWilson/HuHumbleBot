import telebot
import config, dictionary
import answers as ans
import questions as qu
from random import choice, randint
from fuzzywuzzy import process


bot = telebot.TeleBot(config.TOKEN) # Импорт токена для инициализации бота


# Функция открытия стикера (либо с локальной машины, либо с облака)
def ans_sti(x):
    try:
        sti = open(f'stickers/{choice(x)}', 'rb')
    except:
        sti = open(f'/app/stickers/{choice(x)}', 'rb')
    return sti

def half_random(message, x, xsti, y, ysti):
    if randint(0, 1) == 0:
        ans_or_sti(message, x, xsti)
    else:
        ans_or_sti(message, y, ysti)


# Случайный выбор ответа (стикером или сообщением)
def ans_or_sti(message, word, sti):
    selection = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if choice(selection) in [7, 8, 9]:
        bot.send_sticker(message, ans_sti(sti)) 
    else:
        bot.send_message(message, choice(word))  

# Тест вывода всех смайликов
@bot.message_handler(commands=['stickers'])
def demonstration(message):
    for i in ans.List_Ans_Sti:
        try:
            sti = open(f'stickers/{i}', 'rb')
        except:
            sti = open(f'/app/stickers/{i}', 'rb')
        bot.send_sticker(message.chat.id, sti)

# Приветствие
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, ans_sti(ans.Hello_Ans_Sti))
    bot.send_message(message.chat.id, "Доброго времени суток, {0.first_name}!".format(message.from_user, parse_mode="html"))
    bot.send_message(message.chat.id, "Вы не против немного пообщаться?👉👈")

# Основная часть интеллекта бота
@bot.message_handler(content_types=['text', 'sticker'])
def lalala(message):
    resemblance = process.extractOne(message.text, dictionary.Lang)
    if message.text.isupper() and resemblance[0] not in qu.HaHa_Qu:
        bot.send_message(message.chat.id, choice(ans.Is_Upper_Ans))
    else:
        if resemblance[1] > 80:
            if resemblance[0] in qu.Yes_Qu:
                half_random(message.chat.id, ans.Yes_Ans, ans.Yes_Ans_Sti, ans.No_Ans, ans.No_Ans_Sti)
            elif resemblance[0] in qu.No_Qu:
                half_random(message.chat.id, ans.No_Ans, ans.No_Ans_Sti, ans.Yes_Ans, ans.Yes_Ans_Sti)
            elif resemblance[0] in qu.How_Are_U_Qu:
                ans_or_sti(message.chat.id, ans.How_Are_U_Ans, ans.How_Are_U_Ans_Sti)
            elif resemblance[0] in qu.Who_Are_U_Qu:
                bot.send_message(message.chat.id, choice(ans.Who_Are_U_Ans))
            elif resemblance[0] in qu.Psychologist_Qu:
                bot.send_message(message.chat.id, choice(ans.Psychologist_Ans))
            elif resemblance[0] in qu.How_Old_Are_U_Qu:
                bot.send_message(message.chat.id, choice(ans.How_Old_Are_U_Ans))
            elif resemblance[0] in qu.What_Qu:
                ans_or_sti(message.chat.id, ans.What_Ans, ans.What_Ans_Sti)
            elif resemblance[0] in qu.About_What_Qu:
                ans_or_sti(message.chat.id, ans.About_What_Ans, ans.About_What_Ans_Sti)
            elif resemblance[0] in qu.What_Are_U_Doing_Qu:
                bot.send_message(message.chat.id, choice(ans.What_Are_U_Doing_Ans))
            elif resemblance[0] in qu.Hello_Qu:
                ans_or_sti(message.chat.id, ans.Hello_Ans, ans.Hello_Ans_Sti)
            elif resemblance[0] in dictionary.Foul:
                ans_or_sti(message.chat.id, ans.Foul_Ans, ans.Foul_Ans_Sti)
            elif resemblance[0] in qu.Good_Night_Qu:
                ans_or_sti(message.chat.id, ans.Good_Night_Ans, ans.Good_Night_Ans_Sti)
            elif resemblance[0] in qu.Bye_Qu:
                bot.send_message(message.chat.id, choice(ans.Bye_Ans))
            elif resemblance[0] in qu.HaHa_Qu:
                ans_or_sti(message.chat.id, ans.HaHa_Ans, ans.HaHa_Ans_Sti)
        else:
            ans_or_sti(message.chat.id, ans.Not_Understood_Ans, ans.List_Ans_Sti)


bot.infinity_polling(timeout=10, long_polling_timeout = 5)