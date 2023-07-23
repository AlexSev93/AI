import requests
import pprint

token = '6041858940:AAFroDS0oTaiJdM4LAmz0dAb7yyctewztVk'
main_url = f'https://api.telegram.org/bot{token}/'

methods = ['getMe', 'getUpdates']
available_methods = ['sendMessage']

# о боте
url_with_method = f'{main_url}{methods[0]}'
result = requests.get(url_with_method)
# print(result.json())

# проверка обновлений
url_with_method = f'{main_url}{methods[1]}'
messages = requests.get(url_with_method).json()['result']
pprint.pprint(messages)

#ответ на сообщение
# for message in messages:
#     chat_id = message['message']['chat']['id']
#     # text = message['text']
#
#     params = {'chat_id': chat_id, 'text': 'test_mess'}
#     url_with_method = f'{main_url}{available_methods[0]}'
#     result = requests.post(url_with_method, params=params)
