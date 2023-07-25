import json
import pprint

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

    vacancies_info = {}
    one_vacancy_info = []
    vacancies_keywords = {}
    for i, id in enumerate(vacansies_id):
        print(f'Обрабатываем вакансию {i + 1} из {len(vacansies_id)}')
        url_vacancies_id = f'{url_vacancies}/{id}'
        result = requests.get(url_vacancies_id, headers=headers).json()
        # pprint.pprint(result)
        # break
        one_vacancy_info.append(result['alternate_url'])
        one_vacancy_info.append(result['name'])
        if str(result['salary']) == 'None':
            salary = 'Не указана'
        elif result['salary']['from'] and str(result['salary']['to']) == 'None':
            salary = 'от ' + str(result['salary']['from']) + ' ' + result['salary']['currency']
        elif result['salary']['to'] and str(result['salary']['from']) == 'None':
            salary = 'до ' + str(result['salary']['to']) + ' ' + result['salary']['currency']
        else:
            salary = 'от ' + str(result['salary']['from']) + 'до ' + str(result['salary']['to']) + ' ' + result['salary']['currency']

        description = 'Занятость: ' + result['employment']['name'] + '. ' + \
                      'Опыт: ' + result['experience']['name'] + '. ' + \
                      'Должность: ' + result['professional_roles'][0]['name'] + '. ' + \
                      'Зарплата: ' + salary + '. '
        one_vacancy_info.append(description)
        list_skill = []
        try:
            for skill in result['key_skills']:
                if ord(skill['name'][0]) < 192:
                    list_skill.append(skill['name'])
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
        one_vacancy_info.append(list_skill)
        vacancies_info[id] = one_vacancy_info
        one_vacancy_info = []

    # обработка лишнего
    del_key = []
    for key in vacancies_keywords.keys():
        if vacancies_keywords[key] == 1:
            del_key.append(key)
    for key in del_key:
        vacancies_keywords.pop(key)

    # сортировка по убыванию
    sorted_val = sorted(vacancies_keywords.items(), key=lambda item: item[1])
    sorted_val.reverse()
    sorted_vacancies_keywords = {key: val for key, val in sorted_val}

    # вычисление процентов
    # sum_val = sum(sorted_vacancies_keywords.values())
    # for key in sorted_vacancies_keywords.keys():
    #     sorted_vacancies_keywords[key] = [sorted_vacancies_keywords[key],
    #                                       round(sorted_vacancies_keywords[key] / sum_val * 100)]

    return sorted_vacancies_keywords, vacancies_info


def write_to_json(name_vacansy, vacansies_id, vacancies_keywords):
    # подготовка к записи в json
    to_json = [{'name_vacansy': name_vacansy, 'count_vacansy': len(vacansies_id),
                'key_words': [
                    {'name': key, 'count': vacancies_keywords[key][0], 'persent': vacancies_keywords[key][1]}
                    for key in vacancies_keywords.keys()]}]

    with open('data.json', 'w') as file:
        json.dump(to_json, file)


def get_better_vacanci(sorted_vacancies_keywords, vacancies_info):
    if len(sorted_vacancies_keywords) >= 3:
        often_keywords = []
        for i, key in enumerate(sorted_vacancies_keywords.keys()):
            if i == 4:
                break
            else:
                often_keywords.append(key)

    true_vacanci = []
    for vac_id in vacancies_info.keys():
        keywords_in_vacanci = vacancies_info[vac_id][-1]
        cheak = 0
        for often in often_keywords:
            if often in keywords_in_vacanci:
                cheak += 1

        if cheak == 3:
            true_vacanci.append(vacancies_info[vac_id])

    return true_vacanci


if __name__ == '__main__':
    country_id = get_country_id('Беларусь')
    name_vacansy = 'Python Developer'

    vacansies_id = get_vacansies_id(country_id, name_vacansy)

    vacancies_keywords = get_keywords(vacansies_id)

    write_to_json(name_vacansy, vacansies_id, vacancies_keywords)
