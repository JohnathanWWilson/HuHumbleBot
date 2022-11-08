import telebot
import config
from random import choice, randint
from flask import Flask, request
import git

url = 'https://mrolive.pythonanywhere.com/' + config.secret

bot = telebot.TeleBot(config.TOKEN)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)
@app.route('/'+config.secret, methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('path/to/git_repo')
        origin = repo.remotes.origin

        origin.pull

        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


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

bot.polling(none_stop=True)