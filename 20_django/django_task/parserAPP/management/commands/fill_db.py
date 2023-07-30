from django.core.management.base import BaseCommand
from parserAPP.models import Regions, Keywords, Vacancies
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('*' * 30)
        print('my command')

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
        def get_vacancies_id(country_id, name_vacancy, pages=1):
            vacancies_id = []
            for page in range(pages):
                params = {'text': name_vacancy, 'area': country_id, 'page': page}
                result = requests.get(url_vacancies, params=params).json()
                items = result['items']
                id_on_page = [int(item['id']) for item in items]
                vacancies_id.extend(id_on_page)

            return vacancies_id

        # находим ключевые слова
        def get_keywords(vacancies_id):
            headers = {
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                'referer': 'https://www.google.com/'}

            vacancies_info = {}
            one_vacancy_info = []
            vacancies_keywords = {}
            for i, id in enumerate(vacancies_id):
                status = f'Обрабатываем вакансию {i + 1} из {len(vacancies_id)}'
                print(status)
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
                    salary = 'от ' + str(result['salary']['from']) + 'до ' + str(result['salary']['to']) + ' ' + \
                             result['salary']['currency']

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
                    continue
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

        country = 'Беларусь'
        name_vacancy = 'Python Developer'
        keywords, _ = get_keywords(get_vacancies_id(get_country_id(country), name_vacancy))
        keywords = [key for key in keywords.keys()]

        regions_db = Regions.objects.all()
        regions_db = [str(region) for region in regions_db]
        if country not in regions_db:
            Regions.objects.create(region=country)

        keywords_db = Keywords.objects.all()
        keywords_db = [str(word) for word in keywords_db]
        keywords_id = []
        for word in keywords:
            if word not in keywords_db:
                Keywords.objects.create(word=word)
                keywords_id.append(Keywords.objects.get(word=word).id)

        region_id = Regions.objects.get(region=country).id

        # находим id слов из базы которые есть в запросе
        # keywords_id = [Keywords.objects.get(word=word).id for word in keywords]

        new_vacancy = Vacancies.objects.create(vacancy=name_vacancy, regions=Regions.objects.get(id=region_id))
        # добавляем ключевые слова по id которые уже были записаны в базу и относяться к этой записи
        for word_id in keywords_id:
            new_vacancy.words.add(word_id)

        print('END')
        print('*' * 30)

# выбор всех
# regions = Regions.objects.all()
# print(regions)
# print(type(regions))
# for item in regions:
#     print(item)
#     print(type(item))

# выбрать одну
# region = Regions.objects.get(region='Россия')
# print(region)
# print(type(region))

# выбрать несколько
# vacancies = Vacancies.objects.filter(vacancy='python developer')
# print(vacancies)
# print(type(vacancies))

# со связями
# vacancies = Vacancies.objects.all()[1]
# print(vacancies)
# print(vacancies.words.all())

# создание
# Regions.objects.create(region='Литва')

# изменение
# old_region = Regions.objects.get(region='Латвия')
# new_region = 'oooo'
# old_region.region = new_region
# old_region.save()

# удаление 1/несколько
# vacancies = Regions.objects.filter(region='oooo')
# vacancies.delete()

# vacancies = Regions.objects.all()
# vacancies.delete()
