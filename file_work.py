# -*- coding: utf-8 -*-
def import_file(f, forma='1'):
    lst = []
    with open(f, 'r') as f:
        lst = f.readlines()
    if forma == '1':
        for el in lst:
            with open('phone_book.txt', 'a') as f:
                f.write(el)
    else:
        s = ''
        for i, elem in enumerate(lst):
            if elem != '\n':
                s += elem.strip() + ','
            else:
                with open('phone_book.txt', 'a') as f:
                    f.write(s[::-1] + '\n')
                s = ''
    print(f'Импорт {f} завершен')


def export_file(f_ex, n='all', forma=1):
    lst = []
    with open('phone_book.txt', 'r') as f:
        if n == 'all':
            lst = f.readlines()
        else:
            for i in range(int(n)):
                lst.append(f.readline())
        if forma == 'в строку':
            for el in lst:
                with open(f_ex, 'a') as f:
                    f.write(el)
        else:
            for elem in lst:
                el1 = elem.replace(',', '\n')
                with open(f_ex, 'a') as f:
                    f.write(el1 + '\n')
    # print(f'Экспорт завершен. Файл {f_new} создан')


def append_rec(f):
    stroka = input('Введите через "," Фамилию, Имя, номер телефона, и должность:\n') + '\n'
    with open(f, 'a') as f:
        f.write(stroka)
    print('Строка добавлена')


def show_all(f):
    s = ''
    with open(f, 'r') as f:
        stroki_spr = f.readlines()
    for el in stroki_spr:
        s += el.replace(',', ' ') # [:-1]
    return s


def count_rows(f):
    with open(f, 'r') as f:
        stroki_spr = f.readlines()
    return len(stroki_spr)

