# function_for_consol.py, list_dir.data, listdir.txt
import function_for_consol as fc
import sys

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
print('12- сохранить содержимое рабочей области; ')
print('13- выход.                                            ')

while True:
    menu = int(input('Выбрать номер меню - '))
    if menu == 1:
        name = input('Ввести имя новой папки- ')
        try:
            fc.crate_dir(name)
        except:
            print('Нельзя использовать символы * . " / \ [ ] : ; |,')
    elif menu == 2:
        name = input('Ввести имя папки или файла для удаления - ')
        fc.del_file_dir(name)
    elif menu == 3:
        name = input('Ввести имя папки или файла для копирования - ')
        name_new = input('Ввести новое имя для копии - ')
        fc.copy(name, name_new)
    elif menu == 4:
        print(fc.get_input())
    elif menu == 5:
        print(fc.get_dir())
    elif menu == 6:
        print(fc.get_file())
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
        fc.save_list_dir()
    elif menu == 13:
        break
    else:
        print('Нет такого пункта')
