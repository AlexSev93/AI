import requests


url = 'https://github.com/dashboard'
# запрос на главную страницу
result = requests.get(url)

print(result)
print('код ответа с ссервера', result.status_code)
# print('текст ответа', result.text)
# print('данные в json', result.json())

# отправить данные
# res = requests.post(url, data={})
# изменение
# res = requests.put(url, data={'данные на замену'})
# удаление
# res = requests.delete(url)
# опции
# res = requests.options(url)

#эмуляция работы браузера
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
#                          '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# res = requests.get(url, headers=headers)
