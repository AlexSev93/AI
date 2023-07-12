import random
n = [i for i in range(8)]
peoples = {'Илон Маск': '28.07.1971', 'Никола Тесла': '10.07.1856', 'Альберт Эйнштейн': '14.03.1879',
           'Леонард Эйлер': '15.04.1707', 'Иога́нн Карл Фри́дрих Га́усс': '30.04.1777', 'Исаак Ньютон': '04.01.1643',
           'Юрий Гагарин': '09.03.1934', 'Нильс Бор': '07.10.1885'}

q = random.sample(n, 5)



def date_to_str(date):
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
              'октябрь', 'ноябрь', 'декабрь']
    day = ['',' один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь',
           'девять', 'десять', 'надцать', 'двадцать']
    date = [int(i) for i in list(date.split('.'))]
    if date[0] > 20:
        day_st = day[-1] + day[date[0] % 10]
    if date[0] == 20:
        day_st = day[-1]
    if date[0] == 10:
        day_st = day[-3]
    if 10 < date[0] < 20:
        day_st = day[date[0] % 10] + day[-2]
    if date[0] < 10:
        day_st = day[date[0]]

    st = f'{day_st}  {months[date[1]-1]} {date[2]} года'
    return st


while True:
    win = 0
    loss = 0
    for i, name in enumerate(peoples):
        if i in q:
            year = input(f'Какая дата рождения {name}? (Ответ {peoples[name]})')
            if year == peoples[name]:
                print('Верно')
                win += 1
            else:
                print(date_to_str(peoples[name]))
                loss += 1
    print(f'Сделанно {win} ({win / 5 * 100}%) правильных и {loss} ({loss / 5 * 100}%) неправильных ответов')

    if input('Повторить викторину Да/Нет -') == 'Нет':
        break
