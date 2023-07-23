import pprint
import time
import telebot

bot = telebot.TeleBot('6041858940:AAFroDS0oTaiJdM4LAmz0dAb7yyctewztVk')


# say - say upper text
# timer - 5 sec timer
# beep - you know...

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# обработка команд
@bot.message_handler(commands=['timer'])
def timer(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i+1)


# обработка команд с параметрами
@bot.message_handler(commands=['beep'], func=lambda message: message.from_user.id == 837834140)
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, '!!!!!BEEP - THE GREATEST WARRIOR IN THE WORLD!!!!!')


# обработка команд с параметрами
@bot.message_handler(commands=['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, f'{text.upper()}!!!')



@bot.message_handler(content_types=['text'])
def message(message):
    print(message)
    beep_list = ['beep', 'Beep', 'BEEP', 'БИП', 'бип', 'Бип']
    if message.text in beep_list:
        bot.reply_to(message, "Это Величайший воин!!!! КИБЕРБИП")
        bot.reply_to(message, message.text[::-1])
    elif message.text == 'Буп':
        send_sticker(message)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    file_id = 'CAACAgIAAxkBAANGZL0Zh05QdI2tZcsyn2dFQjBvlH4AAgwAA6_GURp1rixSz2ZqXS8E'
    bot.send_sticker(message.chat.id, file_id)

bot.infinity_polling()
