import time
import math


def task_1():
    n = int(input('Введите кол-во секунд: '))
    while n > -1:
        start_time = time.time()
        print('Осталось секунд:', n)
        n -= 1
        try:
            time.sleep(1 - (start_time - time.time()))
        except ValueError:
            continue
    print('Пуск')


def task_2():
    n = int(input('Высота пирамиды: '))
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for j in range(2 * i + 1):
            print('*', end='')
        print()


def task_3():
    for i in range(17):
        if i % int(input()) == 0:
            print('ДА')
        else:
            print('НЕТ')


def task_4():
    n = int(input())
    sum_iq = int(input())
    print(0)
    for i in range(1, n):
        current = int(input())
        sum_iq += current
        avg = sum_iq / (i + 1)
        if current > avg:
            print('>')
        elif current < avg:
            print('<')
        else:
            print(0)


def lkd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def task_5():
    n = int(input())
    nominator = int(input())
    denominator = int(input())
    for i in range(1, n):
        current_nominator = int(input())
        current_denominator = int(input())
        current_lkd = lkd(denominator, current_denominator)
        nominator = nominator * (denominator // current_lkd) + current_nominator * (current_denominator // current_lkd)
        denominator = denominator * current_denominator // current_lkd
        current_lkd = lkd(nominator, denominator)
        nominator //= current_lkd
        denominator //= current_lkd
    print(str(nominator) + '/' + str(denominator))


def task_6():
    n = int(input())
    sum_of_k = 0
    for i in range(1, n + 1):
        sum_of_k += 1 / i ** 2
    print(math.pi ** 2 / sum_of_k)


def task_7():
    n = int(input())
    result = 0
    for i in range(n):
        result += float(input()) * (1 - 2 * (i % 2))
    print(result)
