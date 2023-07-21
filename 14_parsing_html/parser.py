import requests
from bs4 import BeautifulSoup
import pprint

dom = 'https://onliner.by/'
list_tem = ['money', 'auto', 'realt', 'tech']
list_url_tem = [f'https://{part}.onliner.by/' for part in list_tem]

for url_tem in list_url_tem[:1]:
    result = requests.get(url_tem)
    soup = BeautifulSoup(result.text, 'html.parser')

    news_a = soup.find_all('a', class_='news-tiles__stub')
    for one_news in news_a:
        if one_news.get('href')[0] == 'h':
            href = one_news.get('href')
            result = requests.get(href)
            soup = BeautifulSoup(result.text, 'html.parser')

            date_post = soup.find('div', class_='news-header__time').text
            name_post = soup.find('div', class_='news-header__title').text
            print(date_post, name_post)
            start_post = soup.find('div', class_='news-text')
            end_post = soup.find('div', class_='news-text-end')
            # print(start_post, end_post)
            all_h2 = []
            for parent in start_post.children:
                if parent.name == 'h2' and parent.text != '':
                    all_h2.append(parent.text)

                if parent.name == 'p':
                    print(parent.text)
                    print(type(parent.text))
                    print('*' * 50)
                # if parent.name == 'p':
                # print(parent)
                # print(type(parent))
                # print('*' * 50)
            print(all_h2)
            # for i in all_p:
            #     end_post = soup.find('div', class_='news-text-end')
            #     print(end_post)
            #     break
                # if i == soup.find('div', class_='news-text-end'):
                #     break
                # if i.string != None:
                    # if 'Конец статьи для измерения глубины прочтения' in i.string:
                    #     break
                # print(i)
                # print('*'*50)
            # for i in start:
            #     if '<h2>' in i or '<p>' in i:
            #         if i == '<p><!--Конец статьи для измерения глубины прочтения--></p>':
            #             break
            #         test.append(i)
            # print(test)
            # all_p = [p.text for p in soup.find_all('p')]
            # pprint.pprint(all_p)
            break


