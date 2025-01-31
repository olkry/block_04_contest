'''
Во время марсианских гроз ровер Impunity должен работать как «умный
громоотвод» — ловить разряды молний, замерять их напряжение и
сохранять полученные данные в массив.
Очередной раз попав в грозу, ровер должен замерить напряжение каждой новой
молнии, которая в него ударит, и проверить, есть ли такое значение в его
коллекции записей. Если есть — отметить это на счётчике. В результате он
сосчитает, сколько новых молний совпадают по напряжению с теми,
что уже записаны. Метеорологам это зачем-то нужно.
'''
# import time
# from random import randint

# start_time = time.time()
# DATA_SIZE = 100000
# MAX_RAND_NUMBER = 10000000

# # В цикле генерируем список случайных чисел в диапазоне от 1 до 10 млн.
# data = [randint(1, MAX_RAND_NUMBER) for _ in range(DATA_SIZE)]

# # Печатаем, сколько времени генерировался список data:
# print(f'Коллекция data сгенерирована за {time.time() - start_time} сек.')

# match_counter = 0

# for _ in range(10000):
#     # Генерируем случайное значение:
#     new_item = randint(1, MAX_RAND_NUMBER)
#     if new_item in data:
#         match_counter += 1

# print(f'Найдено совпадений: {match_counter}')
# print(f'Объектов в data: {len(data)}')
# # Печатаем, сколько времени работала программа.
# print(f'Программа отработала за {time.time() - start_time} сек.')

# start_time = time.time()

# DATA_SIZE = 500000
# MAX_RAND_NUMBER = 10000000

# # Теперь data - это не список, а множество. Скобки-то фигурные!
# data = {randint(1, MAX_RAND_NUMBER) for _ in range(DATA_SIZE)}
# print(f'Коллекция data сгенерирована за {time.time() - start_time} сек.')

# match_counter = 0

# for _ in range(10000):
#     new_item = randint(1, MAX_RAND_NUMBER)
#     if new_item in data:
#         match_counter += 1

# print(f'Найдено совпадений: {match_counter}')
# print(f'Объектов в data: {len(data)}')
# print(f'Программа отработала за {time.time() - start_time} сек.')


def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    count_in_ls1 = 0
    count_in_ls2 = 0
    len_ls_1 = len(list_set_1)
    len_ls_2 = len(list_set_2)
    for ch1 in list_set_1:
        if ch1 in list_set_2:
            count_in_ls2 += 1
    for ch2 in list_set_2:
        if ch2 in list_set_1:
            count_in_ls1 += 1
    if len_ls_1 == count_in_ls2 and len_ls_2 == count_in_ls1:
        return 'Наборы равны.'
    if len_ls_1 == count_in_ls2 and len_ls_2 != count_in_ls1:
        return f'Набор {list_set_2} - супермножество.'
    if len_ls_1 != count_in_ls2 and len_ls_2 == count_in_ls1:
        return f'Набор {list_set_1} - супермножество.'
    else:
        return 'Супермножество не обнаружено.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
