import sys
import re


def to_float(n):
    try:
        d = float(n)
    except ValueError:
        try:
            d = float(n.replace(',', '.'))
            print('В английском дробная часть отделяется точкой\n')
        except ValueError:
            print('Некорректный ввод, программа будет завершена.')
            sys.exit()
    return d


def task_1():
    s = ''
    n = 0
    print('Несколько строк, последняя из которых — "Спасибо.": ')
    while s != 'Спасибо.':
        s = input()
        n += 1
    print(n)


def task_2():
    n = 0
    sum_n = 0
    count_n = -1
    print('Несколько (не меньше одного) действительных чисел на отдельных строках — температура воздуха в разные дни.\n'
          'Действительное число, меньшее -300.')
    while n >= -300:
        sum_n += n
        count_n += 1
        n = to_float(input())
    print(sum_n / count_n)


def task_3():
    n = int(input('Одно целое число: '))
    # "введённое натуральное число"
    p = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
            p += 1
        else:
            p = 'Нет'
            break
    print(p)


def task_4():
    s1 = input('Две строки — пароль, введённый пользователем в первый и во второй раз: ')
    s2 = input()
    if len(s1) < 8:
        print('Короткий!')
        sys.exit()
    elif re.match('123', s1) is not None:
        print('Простой!')
        sys.exit()
    elif s1 != s2:
        print('Различаются')
    else:
        print('OK')


def task_5():
    n = int(input('Вводится одно натуральное число n: '))
    c = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
            c += 1
        else:
            n = 3 * n + 1
            n //= 2
            c += 2
    print(c)


def task_6():
    while True:
        if int(input()) % 10 != 0:
            break


def task_7():
    x = int(input())
    y = int(input())
    s = input()
    n = 0
    direction = 0
    turns = ['север', 'запад', 'юг', 'восток']
    while s != 'стоп':
        if s == 'вперёд':
            s = int(input()) * (1 - direction // 2 * 2)
            x += (direction % 2) * s
            y -= (1 - direction % 2) * s
        elif s == 'налево':
            direction = (direction + 1) % 4
        elif s == 'направо':
            direction = (direction - 1) % 4
        elif s == 'разворот':
            direction = (direction + 2) % 4
        else:
            continue
        n += 1
        if x == 0 & y == 0:
            break
        s = input()
    while s != 'стоп':
        s = input()
    print(n)
    print(turns[direction])


def task_8():
    s = '>'
    n = 1000
    old = 2000
    while s != '=':
        n, old = abs(n - old), n
        if s == '>':
            n = old - n // 2
        elif s == '<':
            n = old + n // 2 + n % 2
        print(n)
        s = input()
