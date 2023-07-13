import os
import pickle


def add_money(money, dmoney):
    with open('info.data', 'rb') as file:
        data = pickle.load(file)
        data[0] = money + dmoney
    with open('info.data', 'wb') as file:
        pickle.dump(data, file)
    return data[0]


def get_history(history):
    for i in history:
        print(f'{i[0]}-->{i[1]}')


def buy_item(item, value):
    with open('info.data', 'rb') as file:
        data = pickle.load(file)
        data[1].append([item, value])
    with open('info.data', 'wb') as file:
        data[0] = data[0] - value
        pickle.dump(data, file)
    return data[0]


def create_file_defaut_value():
    if 'info.data' not in os.listdir():
        info = [0, []]
        with open('info.data', 'wb') as file:
            pickle.dump(info, file)
    else:
        with open('info.data', 'rb') as file:
            info = pickle.load(file)
    money, history = info[0], info[1]
    return money, history


money, history = create_file_defaut_value()

while True:
    print(f'1. пополнение счета(на счету {money})')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню - ')
    if choice == '1':
        dmon = int(input('Сколько положить на счет?'))
        money = add_money(money, dmon)

    elif choice == '2':
        value = int(input('Сколько стоит?'))
        if value > money:
            print('Недостаточно средств')
        else:
            item = input('Что хотите купить?')
            money = buy_item(item, value)
            history.append([item, value])

    elif choice == '3':
        get_history(history)

    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
