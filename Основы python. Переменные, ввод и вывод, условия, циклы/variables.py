object = {}
object['Тип'] = 'Конденсатор'
object['Имя'] = 'CC-200N'
object['Емкость'] = 0.1
object['Напряжение'] = 50
object['Полярный'] = False


for i in object.values():
    print(f'Содержимое {i} типа {type(i)}')