n = input('Ввести значения первого списка через ,  - ')
n = [int(i) for i in list(n.split(','))]
print(n)

m = input('Ввести значения первого списка через ,  - ')
m = [int(i) for i in list(m.split(','))]
print(m)

for i in m:
    while i in n:
        if i in n:
            n.remove(i)
print(n)
