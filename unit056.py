print("-------------------")
print("  Добро пожаловать ")
print("      в игру       ")
print("  крестики-нолики  ")
print("-------------------")
print(" Вводите два числа ")
print("   через пробел    ")
print("     от 1 до 3:    ")
print("  первое - номер   ")
print("   ряда, второе -  ")
print("      столбца      ")


def field():
    '''Функция для отрисовки поля.'''
    print()
    print("    | 1 | 2 | 3 | ")  # Нумеруем столбцы.
    print("  ~~~~~~~~~~~~~~~ ")
    for i, row in enumerate(cell):  # Нумеруем ряды.
        row_str = f"  {i + 1} | {' | '.join(row)} | "
        print(row_str)
        print("  ~~~~~~~~~~~~~~~ ")
    print()


def correctness():
    '''Функция для ввода и проверки корректности чисел.'''
    while True:
        move = input("       Ваш ход: ").split()
        # Проверим количество введенных значений.
        if len(move) != 2:
            print(" Введите два числа! ")
            continue

        x, y = move  # Распакуем переменные потенциальных координат.

        if not (x.isdigit()) or not (y.isdigit()):  # Проверим, что игрок ввел цифры.
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 1 > x or x > 3 or 1 > y or y > 3:  # Проверим, что числа в нужном диапазоне.
            print(" Введите числа от 1 до 3! ")
            continue

        x, y = x - 1, y - 1  # Приведем нумерацию для работы с индексами координат.

        if cell[x][y] != " ":   # Проверим возможность походить в указанную клетку.
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    '''Функция для проверки выигрышных комбинаций. Переберем все 8 вариантов.'''
    win_line = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))

    for line in win_line:  # Запустим проверку выигрышных линий одинаковыми символами.
        a, b, c = line[0], line[1], line[2]

        if cell[a[0]][a[1]] == cell[b[0]][b[1]] == cell[c[0]][c[1]] != " ":
            return True
    return False


# Объявим массив пустых ячеек и запустим счетчик ходов.
cell = [[" "] * 3 for i in range(3)]
motion = 0

while True:
    field()
    motion += 1

    if motion % 2 == 1:  # Определим очередность ходов.
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = correctness()

    if motion % 2 == 1:  # Заполняем ячейки символами соответственно ходу.
        cell[x][y] = "X"
    else:
        cell[x][y] = "0"

    if motion > 4 and check_win():  # С 5 хода делаем проверку на выигрыш.
        field()
        if motion % 2 == 1:
            print("Выиграл крестик!")
        else:
            print("Выиграл нолик!")
        break

    if motion == 9:  # После девятого хода фиксируем ничью.
        field()
        print("Ничья!")
        break