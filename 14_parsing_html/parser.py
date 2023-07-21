import json

import requests
from bs4 import BeautifulSoup
import pprint

dom = 'https://onliner.by/'
list_tem = ['money', 'realt', 'tech']
list_url_tem = [f'https://{part}.onliner.by/' for part in list_tem]


def remove_left_right_space(name_str):
    return ' '.join(name_str.split())


for url_tem in list_url_tem[:1]:
    result = requests.get(url_tem)
    soup = BeautifulSoup(result.text, 'html.parser')
    news_a = soup.find_all('a', class_='news-tiles__stub')
    for num_news, one_news in enumerate(news_a[3:4]):
        if one_news.get('href')[0] == 'h':
            print(one_news)
            href = one_news.get('href')
            result = requests.get(href)
            soup = BeautifulSoup(result.text, 'html.parser')

            date_post = soup.find('div', class_='news-header__time').text.replace('\n', '')
            date_post = remove_left_right_space(date_post)
            name_post = soup.find('div', class_='news-header__title').text.replace('\n', '')
            print(name_post)
            start_post = soup.find('div', class_='news-text')
            all_news = []
            all_p = []
            n_li = 1
            for child in start_post.descendants:
                # pprint.pprint(child)
                if child.name == 'div':
                    attr = child.attrs
                    if 'id' in attr.keys() and (attr['id'] == 'news-text-end' or attr['id'] == 'st-1'):
                        red_end_text = all_p[-1]
                        if '|' in red_end_text:
                            all_p[-1] = red_end_text[:red_end_text.index('|')]
                        all_news[len(all_news) - 1].append(all_p)
                        break

                elif (child.name == 'h2' or child.name == 'h1') and child.text != '':
                    all_news.append([child.text])
                    if all_p:
                        for i in range(len(all_p)):
                            if '|' in all_p[i]:
                                all_p[i] = all_p[i].replace('|', '')
                        all_news[len(all_news)-2].append(all_p)
                        all_p = []

                elif child.name == 'p' or child.name == 'li':

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

            for_json = {'website': 'https://onliner.by/', 'section_url': url_tem, 'date_post': date_post,
                        'name_post': name_post, 'post': all_news}

            file_name = url_tem[8:len(url_tem)-1].replace('.', '_')
            with open(f'{file_name}_{num_news}.json', 'w') as file:
                json.dump(for_json, file)
            pprint.pprint(all_news)
        else:
            continue