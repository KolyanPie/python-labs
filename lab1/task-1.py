def task_1():
    name = input('Введите ваше имя: ')
    surname = input('Введите вашу фамилию: ')
    animal = input('Введите ваше любимое животное: ')
    sign = input('Введите ваш знак зодиака: ')
    print('Индивидуальный гороскоп для пользователя', name, surname)
    print('Кем вы были в прошлой жизни:', animal)
    print('Ваш знак зодиака -', sign, ', поэтому вы - тонко чувствующая натура.')
    # "Пробел перед запятой по правилам, конечно, не ставится, но здесь пусть стоит."


def task_2():
    print('1 бит - минимальная единица количества информации.',
          '1 байт = 8 бит.',
          '1 Килобит = 1024 бита.',
          '1 Килобайт = 1024 байта.',
          '1 Килобайт = ' + str(8 * 1024) + ' бит.',
          sep='\n')


def task_3():
    first = input('Введите три фразы по очереди\n')
    second = input()
    third = input()
    print(third, second, first, sep='\n')
