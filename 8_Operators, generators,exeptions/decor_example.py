def save_call_to_file(fc):
    def new_cf(*args, **kwargs):
        with open('res.txt', 'a') as file:
            file.write(f'{fc.__name__}\n')
        res = fc(*args, **kwargs)
        return res
    return new_cf


@save_call_to_file
def hello():
    pass


@save_call_to_file
def other():
    pass


@save_call_to_file
def go():
    pass


go()
hello()
other()