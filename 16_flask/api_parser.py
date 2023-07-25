import json
import requests


dom = 'https://api.hh.ru'
url_vacancies = f'{dom}/vacancies'
url_country_id = f'{dom}/areas/countries'


# получаем ид страны
def get_country_id(name_country):
    countres = requests.get(url_country_id).json()
    for country in countres:
        if name_country == country['name']:
            return int(country['id'])


# находим ид вакансий
def get_vacansies_id(country_id, name_vacansy):
    params = {'text': name_vacansy, 'area': country_id}
    result = requests.get(url_vacancies, params=params).json()
    pages = result['pages']

    # ограничение на количество вакансий а то вылезает капча
    pages = 2 if pages > 2 else pages


    vacansies_id = []
    for page in range(pages):
        params = {'text': 'Python Developer', 'area': 16, 'page': page}
        result = requests.get(url_vacancies, params=params).json()
        items = result['items']
        id_on_page = [int(item['id']) for item in items]
        vacansies_id.extend(id_on_page)

    return vacansies_id


# находим ключевые слова
def get_keywords(vacansies_id):
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        'referer': 'https://www.google.com/'}

    vacancies_keywords = {}
    for i, id in enumerate(vacansies_id):
        print(f'Обрабатываем вакансию {i + 1} из {len(vacansies_id)}')
        url_vacancies_id = f'{url_vacancies}/{id}'
        result = requests.get(url_vacancies_id, headers=headers).json()
        try:
            for skill in result['key_skills']:
                if ord(skill['name'][0]) < 192:
                    if skill['name'] not in vacancies_keywords:
                        vacancies_keywords[skill['name']] = 1
                    elif skill['name'] in vacancies_keywords:
                        vacancies_keywords[skill['name']] += 1
        except KeyError:
            # TODO: что-то делать с капчей
            continue
            # webbrowser.register('chrome', None,
            #                     webbrowser.BackgroundBrowser(
            #                         "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            # err_url = result['errors'][0]['captcha_url']
            # webbrowser.get('chrome').open(err_url)
            # next = input('Продолжить')

    # обработка лишнего
    del_key = []
    for key in vacancies_keywords.keys():
        if vacancies_keywords[key] == 1:
            del_key.append(key)
    for key in del_key:
        vacancies_keywords.pop(key)

    # вычисление процентов
    sum_val = sum(vacancies_keywords.values())
    for key in vacancies_keywords.keys():
        vacancies_keywords[key] = [vacancies_keywords[key], round(vacancies_keywords[key] / sum_val * 100, 2)]

    return vacancies_keywords

def write_to_json(name_vacansy, vacansies_id, vacancies_keywords):
    # подготовка к записи в json
    to_json = [{'name_vacansy': name_vacansy, 'count_vacansy': len(vacansies_id),
                'key_words': [
                    {'name': key, 'count': vacancies_keywords[key][0], 'persent': vacancies_keywords[key][1]}
                    for key in vacancies_keywords.keys()]}]

    with open('data.json', 'w') as file:
        json.dump(to_json, file)



if __name__ == '__main__':
    country_id = get_country_id('Беларусь')
    name_vacansy = 'Python Developer'

    vacansies_id = get_vacansies_id(country_id, name_vacansy)

    vacancies_keywords = get_keywords(vacansies_id)

    write_to_json(name_vacansy, vacansies_id, vacancies_keywords)