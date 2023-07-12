import function as fc
import sys
import os

print('1- создать папку;                                    ')
print('2- удалить (файл/папку);                             ')
print('3- копировать (файл/папку);                          ')
print('4- просмотр содержимого рабочей директории;          ')
print('5- посмотреть только папки;                          ')
print('6- посмотреть только файлы;                          ')
print('7- просмотр информации об операционной системе;      ')
print('8- создатель программы;                              ')
print('9- играть в викторину;                               ')
print('10- мой банковский счет;                              ')
print('11- смена рабочей директории (*необязательный пункт); ')
print('12- выход.                                            ')

while True:
    menu = int(input('Выбрать номер меню - '))
    if menu == 1:
        fc.crate_dir()
    elif menu == 2:
        fc.del_file_dir()
    elif menu == 3:
        fc.copy()
    elif menu == 4:
        fc.get_input()
    elif menu == 5:
        fc.get_dir()
    elif menu == 6:
        fc.get_file()
    elif menu == 7:
        fc.info_os()
    elif menu == 8:
        fc.about()
    elif menu == 9:
        sys.path.append('../3_list,str,set,turple')
        import victory
    elif menu == 10:
        sys.path.append('../4_function_in_python')
        import use_functions
    elif menu == 11:
        pass
    elif menu == 12:
        break
    else:
        print('Нет такого пункта')