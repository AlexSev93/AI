n = input('Ввести целые числа через , ; / - ')
s = [',', ';', '/']
m = list(set(n))
for i in m:
    if i in s:
        m.remove(i)
m = [int(i) for i in m]
print(m)
