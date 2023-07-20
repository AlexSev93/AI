import requests
import pprint

def all_country_id():
    countres = requests.get(url_country_id).json()
    for country in countres:
        pprint.pprint(country)


dom = 'https://api.hh.ru'
url_vacancies = f'{dom}/vacancies'
url_country_id = f'{dom}/areas/countries'
all_country_id()
