"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""


def put_money(money):
    dmon = int(input('Сколько положить на счет?'))
    money += dmon
    return money


def get_history(history):
    for i in history:
        print(f'{i[0]} --> {i[1]}')


def buy_item(money):
    value = int(input('Сколько стоит?'))
    if value > money:
        print('Недостаточно средств')
    else:
        item = input('Что хотите купить?')
        return item, value


money = 0
history = []
while True:
    print(f'1. пополнение счета(на счету {money})')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        money = put_money(money)
    elif choice == '2':
        item, value = buy_item(money)
        money -= value
        history.append([item, value])
    elif choice == '3':
        get_history(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
