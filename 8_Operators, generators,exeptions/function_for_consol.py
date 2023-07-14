import os
import shutil
import sys
import pickle


def separators(fc):
    def new_fc(*args, **kwargs):
        print('\n' + '*'*30)
        res = fc(*args, **kwargs)
        print('*'*30 + '\n')
        return res
    return new_fc


def crate_dir(name):
    os.mkdir(name)


def del_file_dir(name):
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    if name in lis:
        os.remove(name) if os.path.isfile(f'{dir_main}/{name}') else os.rmdir(name)
    else:
        print('Нет совпадения')


def copy(name, name_new):
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    if name in lis:
        shutil.copyfile(name, name_new) if os.path.isfile(f'{dir_main}/{name}') else shutil.copytree(name, name_new)
    else:
        print('Нет совпадения')


def get_input():
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    st = [i for i in lis]
    return st


def get_dir():
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    st = [i for i in lis if os.path.isdir(f'{dir_main}/{i}')]
    return st


def get_file():
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    st = [i for i in lis if os.path.isfile(f'{dir_main}/{i}')]
    return st


@separators
def info_os():
    print(os.name, sys.platform)


@separators
def about():
    print('Программу создал Севостьянов Александр Юрьевич')


def save_list_dir():
    list_folder = ', '.join(get_dir())
    list_files = ', '.join(get_file())
    st = f'files: {list_files}\ndirs: {list_folder}'
    with open('list_dir.data', 'wb') as file:
        pickle.dump(st, file)
    with open('listdir.txt', 'w') as file:
        file.write(st)
