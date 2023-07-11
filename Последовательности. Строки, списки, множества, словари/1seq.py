count = int(input('Ввести количество элементов списка = '))
lis = [int(input(f'Ввести значение элемента {i+1}= ')) for i in range(count)]

print('Исходный список', lis)
lis_sort = lis.count()
lis_sort.sort()
print('Отсортированный список', lis_sort)
