import os
import shutil
import sys


def crate_dir():
    name_dir = input('Ввести имя новой папки- ')
    os.mkdir(name_dir)


def del_file_dir():
    dir_main = os.getcwd()
    name = input('Ввести имя папки или файла для удаления - ')
    lis = os.listdir(dir_main)
    if name in lis:
        if os.path.isfile(f'{dir_main}/{name}'):
            os.remove(name)
        elif os.path.isdir(f'{dir_main}/{name}'):
            os.rmdir(name)
    else:
        print('Нет совпадения')


def copy():
    dir_main = os.getcwd()
    name = input('Ввести имя папки или файла для копирования - ')
    lis = os.listdir(dir_main)
    if name in lis:
        name_new = input('Ввести новое имя для копии - ')
        if os.path.isfile(f'{dir_main}/{name}'):
            shutil.copyfile(name, name_new)
        elif os.path.isdir(f'{dir_main}/{name}'):
            shutil.copytree(name, name_new)
    else:
        print('Нет совпадения')


def get_input():
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    for i in lis:
        print(i)


def get_dir():
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    for i in lis:
        if os.path.isdir(f'{dir_main}/{i}'):
            print(i)


def get_file():
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    for i in lis:
        if os.path.isfile(f'{dir_main}/{i}'):
            print(i)


def info_os():
    print(os.name)
    print(sys.platform)


def about():
    print(os.stat('main_consol.py'))
