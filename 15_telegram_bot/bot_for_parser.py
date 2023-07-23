import os
import telebot
from telebot import types
from parser import get_link_news, get_one_new

bot = telebot.TeleBot('6041858940:AAFroDS0oTaiJdM4LAmz0dAb7yyctewztVk')
command_dist = {'start': 'Приветствие пользователей',
                'select_tem': 'Доступные темы для поиска',
                'file': 'Файл с текстом статьи',
                'help': 'Описание команд'}

dist_tem = {'money': 'Кошелек', 'realt': 'Недвижимость', 'tech': 'Технологии'}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Приветствую! Этот бот позволяет найти актуальные новости с сайта onliner.by")


@bot.message_handler(commands=['help'])
def send_help(message):
    message_help = ''
    for key in command_dist.keys():
        line = f'<b>{key}</b> ---> {command_dist[key]}\n'
        message_help += line
    bot.reply_to(message, message_help, parse_mode='HTML')


@bot.message_handler(commands=['select_tem'])
def send_tem(message):
    markup = types.InlineKeyboardMarkup()
    for i, tem in enumerate(dist_tem.items()):
        markup.add(types.InlineKeyboardButton(f'{i+1}. {tem[1]}', callback_data=tem[0]))
    bot.reply_to(message, "Выбери раздел для поиска:", reply_markup=markup)


@bot.message_handler(commands=['file'])
def save_to_file(message):
    chat_id = message.chat.id
    if os.path.exists('test.json'):
        with open('test.json') as file:
            bot.send_document(chat_id, file)
        bot.reply_to(message, 'Файл с содержанием статьи')
    else:
        bot.send_message(message, 'Файла нет. Необходимо выполнить поиск новостей')


@bot.callback_query_handler(func=lambda call: True)
def callback_tem(call):
    call_data = call.data
    if call_data in dist_tem.keys():
        news_a_link, title_news = get_news_tem(call_data)
        markup_mew = types.InlineKeyboardMarkup()
        for i in range(len(title_news)):
            markup_mew.add(types.InlineKeyboardButton(f'{title_news[i]}', callback_data=f'{call_data}_{i}'))
        bot.send_message(call.message.chat.id, "Выбери новость:", reply_markup=markup_mew)

    elif call_data[0:call_data.index('_')] in dist_tem.keys():
        news_a_link, title_news = get_news_tem(call_data[0:call_data.index('_')])
        for key in dist_tem.keys():
            if key in call_data:
                index_link = call_data.replace(key, '').replace('_', '')
                link_one_news = news_a_link[int(index_link)]
                # news_title = title_news[int(index_link)]
                break
        all_text_news, _ = get_one_new(link_one_news)
        for i in range(len(all_text_news)):
            all_text_news[i][0] = f'<b>{all_text_news[i][0]}</b>\n'

        text_for_tg = []
        for part in all_text_news:
            text_for_tg.append(part[0])
            text_for_tg.extend(part[1])

        st = ''
        for text in text_for_tg:
            if len(st) + len(text) < 4000:
                st = f'{st}{text}\n'
            else:
                bot.send_message(call.message.chat.id, f'{st}\n', parse_mode='HTML')
                st = ''
        bot.send_message(call.message.chat.id, st, parse_mode='HTML')
        bot.send_message(call.message.chat.id, f'\nСсылка на статью\n{link_one_news}')


def get_news_tem(item):
    url_tem = f'https://{item}.onliner.by/'
    news_a, news_div = get_link_news(url_tem)
    news_a_link = [link.get('href') for link in news_a]
    title_news = [f'{i+1}. {one_news}' for i, one_news in enumerate(news_div)]
    return news_a_link, title_news


bot.infinity_polling()
