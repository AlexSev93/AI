peoples = {'Илон Маск': 1971, 'Никола Тесла': 1856, 'Альберт Эйнштейн': 1879,
           'Леонард Эйлер': 1707, 'Иога́нн Карл Фри́дрих Га́усс': 1777}

while True:
    win = 0
    loss = 0
    for name in peoples.keys():
        year = int(input(f'Какой год рождения {name}? (Ответ {peoples[name]})'))
        if year == peoples[name]:
            print('Верно')
            win += 1
        else:
            print('Неверно')
            loss += 1
    print(f'Сделанно {win} ({win / 5 * 100}%) правильных и {loss} ({loss / 5 * 100}%) неправильных ответов')

    if input('Повторить викторину Да/Нет -') == 'Нет':
        break
