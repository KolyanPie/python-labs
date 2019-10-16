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
    n = input('Введите дробное число: ')
    d = to_float(n)
    if d < 0:
        print('-')
    elif d == 0:
        print('0')
    else:
        print('+')
    return


def task_2():
    n = input('Введите дробное число: ')
    d1 = to_float(n)
    n = input('Введите ещё дробное число: ')
    d2 = to_float(n)
    n = input('Введите операцию (+, -, *, /): ')
    if n == '+':
        print(d1 + d2)
    elif n == '-':
        print(d1 - d2)
    elif n == '*':
        print(d1 * d2)
    elif n == '/':
        try:
            print(d1 / d2)
        except ZeroDivisionError:
            print(888888)
    else:
        print(888888)
    return


def task_3():
    n = input('Введите год: ')
    y = int(n)
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        print('Високосный')
    else:
        print('Не високосный')


def task_4():
    n = input('Введите число: ')
    y = int(n)
    if y % 2 == 0:
        print('чётное')
    else:
        print('нечётное')


def task_5():
    print(len(input('Самое длинное имя, которое только можно придумать: ')) * 2 + 3)
    return


def task_6():
    cod = input('Целое трёхзначное число: ')
    if re.fullmatch('\\d{3}', cod) is None:
        print('Некорректный ввод, программа будет завершена.')
        sys.exit()
    list(cod)
    if (cod[0] == cod[1]) and (cod[1] == cod[2]):
        print('В числе три одинаковые цифры')
    elif (cod[0] == cod[1]) or (cod[1] == cod[2]) or (cod[0] == cod[2]):
        print('В числе две одинаковые цифры')
    else:
        print('ОК')


def task_7():
    n = input('Строка, содержащая трехзначное число: ')
    n = re.match('\\d{3}', n)
    if n is None:
        print('Некорректный ввод, программа будет завершена.')
        sys.exit()
    n = int(n.group(0))
    n = [n // 100, n % 100 // 10, n % 10, 0]
    n[3] = (n[0] + n[1] + n[2])
    if (n[3] == n[0] * 3) or (n[3] == n[1] * 3) or (n[3] == n[2] * 3):
        print('Вы ввели красивое число')
    else:
        print('Жаль, вы ввели обычное число')


def task_8():
    n = input('Строка, содержащая трехзначное число: ')
    n = re.match('\\d{3}', n)
    if n is None:
        print('Некорректный ввод, программа будет завершена.')
        sys.exit()
    n = int(n.group(0))
    n = [n // 100 + n % 100 // 10, n % 100 // 10 + n % 10]
    if n[0] > n[1]:
        print(n[0], n[1], sep='')
    else:
        print(n[1], n[0], sep='')


def task_9():
    n = input('Строка, содержащая сообщение: ')
    n = len(n) * 40
    print(n // 100, 'р.', n % 100, 'коп.')
