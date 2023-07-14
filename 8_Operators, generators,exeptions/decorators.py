# декорабор позволяет выполнить действие до и после выполнения функции

def hello():
    print('hello')


# функция декоратор
def add_separators(hello): # к какой функции применяем
    def inner(): # функция с новым поведением
        print('*'*10)
        res = hello()
        print('*'*10)
        return res
    # возвращается новая фукнция inner  с новым поведением
    return inner


@add_separators  # new_other = add_separators(other)
def other():
    return 'other'

new_hello = add_separators(hello)
new_hello()

# new_other = add_separators(other)
# res = new_other()
# print(res)

# res = other()
# print(res)
def my_separators(fc):
    def new_fc(*args, **kwargs):
        print('\n' + '*'*30)
        res = fc(*args, **kwargs)
        print('*'*30 + '\n')
        return res
    return new_fc

@my_separators
def msum(a, b):
    return a+b


if __name__ == '__main__':

    res = msum(2,4)
    print(res)
