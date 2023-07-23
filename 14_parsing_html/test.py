dist_tem = {'money': 'Кошелек', 'realt': 'Недвижимость', 'tech': 'Технологии'}

tem = 'Недвижимость'
if tem in dist_tem.values():
    for item in dist_tem.items():
        if tem in item:
            url_tem = f'https://{item[0]}.onliner.by/'

print(url_tem)