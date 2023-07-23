import json
import requests
from bs4 import BeautifulSoup
import pprint

dom = 'https://onliner.by/'
dist_tem = {'money': 'Кошелек', 'realt': 'Недвижимость', 'tech': 'Технологии'}


def remove_left_right_space(name_str):
    return ' '.join(name_str.split())


def selec_menu():
    print('1. Выбрать раздел поиска новостей')
    print('2. Выход')

    while True:
        try:
            num_menu = int(input('Выбрать пункст меню - '))
            if 0 < num_menu < 3:
                break
        except ValueError:
            print('Вводим только числа')

    if num_menu == 2:
        return False
    if num_menu == 1:
        for i, tem in enumerate(dist_tem.values()):
            print(f' {i + 1}. {tem}')
        while True:
            tem = input('Выбрать тему поиска новостей - ')
            if tem in dist_tem.values():
                for item in dist_tem.items():
                    if tem in item:
                        url_tem = f'https://{item[0]}.onliner.by/'
                    return url_tem


def get_link_news(url_tem):
    result = requests.get(url_tem)
    soup = BeautifulSoup(result.text, 'html.parser')
    news_a = soup.find_all('a', class_='news-tiles__stub')
    news_div = soup.find_all('div', class_='news-tiles__subtitle max-lines-3')
    for i in range(len(news_div)):
        news_div[i] = remove_left_right_space(news_div[i].text.replace('\n', ''))
        print(f'{i + 1}. {news_div[i]}')
    return news_a, news_div


def get_one_new(link_one_news):
    result = requests.get(link_one_news)
    soup = BeautifulSoup(result.text, 'html.parser')
    date_post = soup.find('div', class_='news-header__time').text.replace('\n', '')
    date_post = remove_left_right_space(date_post)
    name_post = soup.find('div', class_='news-header__title').text.replace('\n', '')
    info = [date_post, name_post]
    start_post = soup.find('div', class_='news-text')
    all_news = []
    all_p = []
    n_li = 1
    for child in start_post.descendants:
        # pprint.pprint(child)
        if child.name == 'div':
            attr = child.attrs
            # print(attr)
            if 'id' in attr.keys() and attr['id'] in ['news-text-end', 'st-1']:
                red_end_text = all_p[-1]
                if '|' in red_end_text:
                    all_p[-1] = red_end_text[:red_end_text.index('|')]
                all_news[len(all_news) - 1].append(all_p)
                break
            # if 'class' in attr.keys() and (attr['class'] == ['news-promo'] or attr['class'] == ['news-promo__title']):
            #     continue

        elif child.name in ['h2', 'h1'] and child.text != '':
            all_news.append([child.text])
            if all_p:
                for i in range(len(all_p)):
                    if '|' in all_p[i]:
                        all_p[i] = all_p[i].replace('|', '')
                all_news[len(all_news) - 2].append(all_p)
                all_p = []

        elif child.name in ['li', 'p']:

            if child.text == 'Наш канал в Telegram. Присоединяйтесь!':
                red_end_text = all_p[-1]
                if '|' in red_end_text:
                    all_p[-1] = red_end_text[:red_end_text.index('|')]
                all_news[len(all_news) - 1].append(all_p)
                break
            if child.name == 'li':
                to_add = child.get_text(separator='|', strip=True)
                to_add = f'{n_li}. {to_add}'
                all_p.append(to_add)
                n_li += 1
            else:
                n_li = 1
                all_p.append(child.get_text(separator='|', strip=True))

    with open('test.json', 'w') as file:
        json.dump(all_news, file)

    return all_news, info


def save_to_json(for_json):
    file_name = url_tem[8:len(url_tem) - 1].replace('.', '_')
    with open(f'{file_name}_{num_tem}.json', 'w') as file:
        json.dump(for_json, file)


if __name__ == '__main__':
    while True:
        url_tem = selec_menu()
        if not url_tem:
            break

        news_a, news_div = get_link_news(url_tem)

        while True:
            try:
                num_tem = int(input('Выбрать номер новости - '))
                if 0 < num_tem < len(news_div) + 1:
                    break
            except ValueError:
                print(' Вводим только числа')

        href = news_a[num_tem-1].get('href')
        all_news, info = get_one_new(href)

        for_json = {'website': 'https://onliner.by/', 'section_url': url_tem, 'date_post': info[1],
                    'name_post': info[0], 'post': all_news}

        save_to_json(for_json)

        pprint.pprint(all_news)
        print('*'*50)
        print('Конец парсинга')
        print('*' * 50)
