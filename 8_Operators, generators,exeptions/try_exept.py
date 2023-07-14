while True:
    try:
        a = int(input('aefds'))
        print(100/a)
    except Exception as t:  # в t записывается ошибка
        print('вводим только числа')
        print(t)

while True:
    try:
        a = int(input('aefds'))
        print(100/a)
    except ZeroDivisionError:
        print('нельзя вводить 0')
    except ValueError:
        print('вводим только числа')
    else: # когда нет ошибок
        pass
    finally:# выполниться всегда даже если есть ошибки
        pass
