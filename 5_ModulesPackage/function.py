import os
import shutil
import sys
import platform


def crate_dir(name):
    os.mkdir(name)


def del_file_dir(name):
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    if name in lis:
        if os.path.isfile(f'{dir_main}/{name}'):
            os.remove(name)
        elif os.path.isdir(f'{dir_main}/{name}'):
            os.rmdir(name)
    else:
        print('Нет совпадения')


def copy(name, name_new):
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    if name in lis:
        if os.path.isfile(f'{dir_main}/{name}'):
            shutil.copyfile(name, name_new)
        elif os.path.isdir(f'{dir_main}/{name}'):
            shutil.copytree(name, name_new)
    else:
        print('Нет совпадения')


def get_input():
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    st = []
    for i in lis:
        st.append(i)
    return st


def get_dir():
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    st = []
    for i in lis:
        if os.path.isdir(f'{dir_main}/{i}'):
            st.append(i)
    return st


def get_file():
    dir_main = os.getcwd()
    lis = os.listdir(dir_main)
    st = []
    for i in lis:
        if os.path.isfile(f'{dir_main}/{i}'):
            st.append(i)
    return st


def info_os():
    st = [os.name, sys.platform]
    return st


def about():
    return platform.node()

