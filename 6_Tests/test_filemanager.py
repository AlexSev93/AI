import sys

sys.path.append('../5_ModulesPackage')

from function import get_file, get_input, get_dir, about, crate_dir, del_file_dir, info_os, copy
import os
import platform

dir_main = os.getcwd()
lis = os.listdir(dir_main)


def test_consol():
    assert len(get_file()) >= 0
    assert len(get_dir()) >= 0
    for i in get_file():
        assert i in lis
    for i in get_dir():
        assert i in lis
    assert get_input() == lis
       
    assert about() == platform.node()
    assert len(info_os()) == 2
    assert info_os() == [os.name, sys.platform]


def test_create_dir():
    if 'TEST_FOLDER' in os.listdir(dir_main):
        os.rmdir('TEST_FOLDER')
    crate_dir('TEST_FOLDER')
    assert 'TEST_FOLDER' in os.listdir(dir_main)
    os.rmdir('TEST_FOLDER')


def test_copy():
    if 'TEST_FOLDER' in os.listdir(dir_main):
        os.rmdir('TEST_FOLDER')
    if 'TEST_FOLDER_COPY' in os.listdir(dir_main):
        os.rmdir('TEST_FOLDER_COPY')
    crate_dir('TEST_FOLDER')
    copy('TEST_FOLDER', 'TEST_FOLDER_COPY')
    assert 'TEST_FOLDER' in os.listdir(dir_main)
    os.rmdir('TEST_FOLDER')
    os.rmdir('TEST_FOLDER_COPY')

    if 'test_file.txt' in os.listdir(dir_main):
        os.remove('test_file.txt')
    if 'test_file_copy.txt' in os.listdir(dir_main):
        os.remove('test_file_copy.txt')
    test_file = open('test_file.txt', 'w')
    test_file.close()
    copy('test_file.txt', 'test_file_copy.txt')
    os.remove('test_file.txt')
    os.remove('test_file_copy.txt')


def test_del_file_dir():
    if 'TEST_FOLDER' in os.listdir(dir_main):
        os.rmdir('TEST_FOLDER')
    os.mkdir('TEST_FOLDER')
    assert del_file_dir('TEST_FOLDER') not in os.listdir(dir_main)

    if 'test_file.txt' in os.listdir(dir_main):
        os.remove('test_file.txt')

    test_file = open('test_file.txt', 'w')
    test_file.close()
    assert del_file_dir('test_file.txt') not in os.listdir(dir_main)
