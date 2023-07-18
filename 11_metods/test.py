while True:
    try:
        row = int(input(f'В каком ряду число - ? - ')) - 1
    except ValueError:
        print('Вводим только числа')
    else:
        break
while True:
    try:
        col = int(input(f'В каком столбце число - ? - ')) - 1
    except ValueError:
        print('Вводим только числа')
    else:
        break


print(row, col)