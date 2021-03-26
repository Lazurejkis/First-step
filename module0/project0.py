import numpy as np


def intro():
    print("------------------------------------------------------")
    print("    Данная программа загадывает число от 1 до 100     ")
    print("  и сама же отгадывает, используя только информацию   ")
    print("   о том, больше или меньше предполагаемое число.     ")
    print("    Алгоритм отработал 1000 раз и вот результаты:     ")
    print("------------------------------------------------------")


# Зададим случайное число, которое нужно отгадать.
number = np.random.randint(1, 101)

def game_core(number):
    ''' В этой функции алгоритм будет угадывать число и возвращать количество попыток.'''
    count = 1
    start, end = 1, 101
    # Зададим случайное число, которое будет отгадывать первое.
    predict = np.random.randint(start, end)

    while predict != number:
        count += 1
        # На основе подсказок "больше-меньше" будем сужать диапазон поиска на каждом шаге.
        if predict > number:
            ''' 
            Если предполагаемое число больше загаданного, отбросим лишние числа из выборки
            до верхней границы и ограничим выборку для следующего шага цикла.
            '''
            end = predict
            predict = np.random.randint(start, predict-1)
        elif predict < number:
            ''' Здесь то же самое, но в другую сторону. Отсекаем меньшие числа '''
            start = predict
            predict = np.random.randint(predict+1, end)
    return (count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число.'''
    count_ls = []
    # Фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим.
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    # Добавим результаты игр в список и посчитаем среднее арифметическое.
    for value in random_array:
        count_ls.append(game_core(number))
        score = int(np.mean(count_ls))
    # Выделим минимальное значение из списка результатов.
    minimum = min(count_ls)
    if min(count_ls) == 1:
        attempt = "попытку"
    else:
        attempt = "попытки"
    # Выделим максимальное значение из списка результатов.
    maximum = max(count_ls)
    print(f"Самое быстрое угадывание произошло за {minimum} {attempt}")
    print(f"Дольше всего поиск значения велся в течение {maximum} попыток")
    print(f"Алгоритм угадывал число в среднем за {score} попыток")
    return(score)


intro()
score_game(game_core)
