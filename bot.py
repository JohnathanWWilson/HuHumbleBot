import telebot
import config, dictionary
import answers as ans
import questions as qu
from random import choice, randint
from fuzzywuzzy import process
from datetime import datetime


bot = telebot.TeleBot(config.TOKEN) # Импорт токена для инициализации бота


# Функция открытия стикера (либо с локальной машины, либо с облака)
def ans_sti(x):
    try:
        choiced = choice(x)
        sti = open(f'stickers/{choiced}', 'rb')
    except:
        choiced = choice(x)
        sti = open(f'/app/stickers/{choiced}', 'rb')
    print(f'Sticker: {choiced}')
    return sti

def half_random(message, x, xsti, y, ysti):
    if randint(0, 1) == 0:
        ans_or_sti(message, x, xsti)
    else:
        ans_or_sti(message, y, ysti)

def send_ans(x, y):
    mesg = bot.send_message(x, y)
    print(f'Answer: "{mesg.text}"')

# Случайный выбор ответа (стикером или сообщением)
def ans_or_sti(message, word, sti):
    selection = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if choice(selection) in [7, 8, 9]:
        bot.send_sticker(message, ans_sti(sti))
    else:
        send_ans(message, choice(word))

# Логи
def espionage(message):
    print(f'\n{datetime.now()}')
    print(f'Username: {message.from_user.username}')
    print(f'First name: {message.from_user.first_name}')
    print(f'Last name: {message.from_user.last_name}')
    print(f'id: {message.from_user.id}')
    print(f'Message: "{message.text}"')

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
    print()
    bot.send_sticker(message.chat.id, ans_sti(ans.Hello_Ans_Sti))
    send_ans(message.chat.id, "Доброго времени суток, {0.first_name}!".format(message.from_user, parse_mode="html"))
    send_ans(message.chat.id, "Вы не против немного пообщаться?👉👈")

# Основная часть интеллекта бота
@bot.message_handler(content_types=['text', 'sticker'])
def lalala(message):
    espionage(message)
    resemblance = process.extractOne(message.text, dictionary.Lang)
    print(f'Comparison: {resemblance}')
    if message.text.isupper() and resemblance[0] not in qu.HaHa_Qu:
        send_ans(message.chat.id, choice(ans.Is_Upper_Ans))
    else:
        if resemblance[1] > 80:
            if resemblance[0] in qu.Yes_Qu:
                half_random(message.chat.id, ans.Yes_Ans, ans.Yes_Ans_Sti, ans.No_Ans, ans.No_Ans_Sti)
            elif resemblance[0] in qu.No_Qu:
                half_random(message.chat.id, ans.No_Ans, ans.No_Ans_Sti, ans.Yes_Ans, ans.Yes_Ans_Sti)
            elif resemblance[0] in qu.How_Are_U_Qu:
                ans_or_sti(message.chat.id, ans.How_Are_U_Ans, ans.How_Are_U_Ans_Sti)
            elif resemblance[0] in qu.Who_Are_U_Qu:
                send_ans(message.chat.id, choice(ans.Who_Are_U_Ans))
            elif resemblance[0] in qu.Psychologist_Qu:
                send_ans(message.chat.id, choice(ans.Psychologist_Ans))
            elif resemblance[0] in qu.How_Old_Are_U_Qu:
                send_ans(message.chat.id, choice(ans.How_Old_Are_U_Ans))
            elif resemblance[0] in qu.What_Qu:
                ans_or_sti(message.chat.id, ans.What_Ans, ans.What_Ans_Sti)
            elif resemblance[0] in qu.About_What_Qu:
                ans_or_sti(message.chat.id, ans.About_What_Ans, ans.About_What_Ans_Sti)
            elif resemblance[0] in qu.What_Are_U_Doing_Qu:
                send_ans(message.chat.id, choice(ans.What_Are_U_Doing_Ans))
            elif resemblance[0] in qu.Hello_Qu:
                ans_or_sti(message.chat.id, ans.Hello_Ans, ans.Hello_Ans_Sti)
            elif resemblance[0] in dictionary.Foul:
                ans_or_sti(message.chat.id, ans.Foul_Ans, ans.Foul_Ans_Sti)
            elif resemblance[0] in qu.Good_Night_Qu:
                ans_or_sti(message.chat.id, ans.Good_Night_Ans, ans.Good_Night_Ans_Sti)
            elif resemblance[0] in qu.Bye_Qu:
                send_ans(message.chat.id, choice(ans.Bye_Ans))
            elif resemblance[0] in qu.HaHa_Qu:
                ans_or_sti(message.chat.id, ans.HaHa_Ans, ans.HaHa_Ans_Sti)
            elif resemblance[0] in qu.How_Many_Qu:
                send_ans(message.chat.id, choice(ans.How_Many_Ans))
        else:
            ans_or_sti(message.chat.id, ans.Not_Understood_Ans, ans.List_Ans_Sti)


bot.infinity_polling(timeout=10, long_polling_timeout = 5)