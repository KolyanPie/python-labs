import random


def task_1():
    d = int(input())
    m = int(input())
    y = int(input())
    m = (m + 9) % 12 + 1
    c = y // 100
    y = y % 100
    c = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
    print(c % 7)


def task_2():
    n = int(input())
    c = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        c += 1
    print(c)


def task_3():
    a = [int(input()), int(input())]
    while a[0] + a[1] > 0:
        a[int(input()) - 1] -= int(input())
        # a[(int(input()) - 1) % 2] -= int(input())
        print(a[0], a[1])


def task_4():
    n = int(input())
    ai_turn = True
    while n > 0:
        if ai_turn:
            print('Ход программы: ')
            a = n % 4
            a = a + (0 ** a) * int(random.random() * 3 + 1)
        else:
            a = 0
            while not (a in range(1, min(4, n + 1))):
                a = int(input('ваш ход: '))
        n -= a
        if a == 1:
            print('Взят  1 камень. Осталось', n)
        else:
            print('Взято', a, ' камня. Осталось', n)
        ai_turn = not ai_turn
    if ai_turn:
        print('Победа')
    else:
        print('Поражение')


def task_5():
    n = int(input())
    # по сути победит тот кто оставит 1 камень вместо 0, как в прошлый раз
    n -= 1
    ai_turn = True
    while n > 0:
        if ai_turn:
            print('Ход программы: ')
            a = n % 4
            a = a + (0 ** a) * int(random.random() * 3 + 1)
        else:
            a = 0
            while not (a in range(1, min(4, n + 2))):
                a = int(input('ваш ход: '))
        n -= a
        if a == 1:
            print('Взят  1 камень. Осталось', n + 1)
        else:
            print('Взято', a, ' камня. Осталось', n + 1)
        ai_turn = not ai_turn
    n += 1
    if n == 0:
        print('Поражение')
    elif ai_turn:
        print('Взят  1 камень. Осталось 0')
        print('Победа')
    else:
        a = 0
        while not (a == 1):
            a = int(input('ваш ход: '))
        print('Взят  1 камень. Осталось 0')
        print('Поражение')


def task_6():
    a = [int(input()), int(input()), int(input())]
    while a[0] + a[1] + a[2] > 0:
        a[int(input()) - 1] -= int(input())
        print(a[0], a[1], a[2])
    return


def int_input():
    n = 0
    while n < 1:
        try:
            n = int(input('Введите натуральное число: '))
        except ValueError:
            continue
    return n


def int_input_max(maximum):
    n = int_input()
    while n > maximum:
        print('Число должно быть <=', maximum)
        n = int_input()
    return n


def task_7():
    # nim_game(2)
    n = [int_input(), int_input()]
    ai_turn = True
    while n[0] > 0 or n[1] > 0:
        if ai_turn:
            d = n[1] - n[0]
            if d == 0:
                number = int(random.random() * 2)
                count = int(random.random() * (n[number] // 2) + 1)
            else:
                number = (1 + d // abs(d)) // 2
                count = abs(d)
        else:
            number = int_input_max(2) - 1
            while n[number] == 0:
                print('Куча пуста, выберите другую')
                number = int_input_max(2) - 1
            count = int_input_max(n[number])
        n[number] -= count
        print('Взято', count, 'камней из', number + 1, 'кучи. Теперь камней:', n[0], n[1])
        ai_turn = not ai_turn
    if ai_turn:
        print('Победа')
    else:
        print('Поражение')


def nim_game(counts_of_batch):
    n = [int_input() for i in range(counts_of_batch)]
    ai_turn = True
    while sum(n) > 0:
        if ai_turn:
            nim_sum = n[counts_of_batch - 1]
            for i in range(counts_of_batch - 1):
                nim_sum ^= n[i]
            if nim_sum == 0:
                number = int(random.random() * counts_of_batch)
                while n[number] == 0:
                    number = (number + 1) % counts_of_batch
                count = int(random.random() * (n[number] // 2) + 1)
            else:
                for i in range(counts_of_batch):
                    if nim_sum ^ n[i] < n[i]:
                        number = i
                        count = n[i] - nim_sum ^ n[i]
                        break
        else:
            number = int_input_max(counts_of_batch) - 1
            while n[number] == 0:
                print('Куча пуста, выберите другую')
                number = int_input_max(counts_of_batch) - 1
            count = int_input_max(n[number])
        n[number] -= count
        print('Взято', count, 'камней из', number, 'кучи. Теперь камней: ', n)
        ai_turn = not ai_turn
    if ai_turn:
        print('Победа')
    else:
        print('Поражение')


def task_8():
    nim_game(3)
