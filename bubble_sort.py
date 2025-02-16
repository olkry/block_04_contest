

def bubble_sort(array):
    last_index = len(array) - 1
    is_sorted = True

    while is_sorted:
        is_sorted = False
        for i in range(last_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = True
        last_index -= 1
    return array


if __name__ == '__main__':
    inp_arr = [4, 6, 1, 3, 2, 9, 7, 5, 6, 3, 2, 3,
               5, 5, 7, 6, 8, 4, 3, 9, 8, 4, 3, 8, 7, 4, 5]
    print(bubble_sort(inp_arr))


# example_array = [6, 5, 3, 1, 8, 7, 2, 4]

# def bubble_sort(data):
#     # Создаём внешний цикл for, указываем диапазон range.
#     # Первый аргумент в range - начало диапазона: len(data) - 1.
#     # Второй аргумент - конец диапазона (не включается в диапазон): 0.
#     # Третий аргумент - шаг для получения следующего значения диапазона: -1.
#     # На каждой итерации переменная last_index будет уменьшаться на 1.
#     for last_index in range(len(data) - 1, 0, -1):
#         # На этом проходе перестановок ещё не было:
#         swapped = False
#         # Вложенный цикл будет перебирать значения от 0 до last_index 
#         # (не включая last_index).
#         for item_index in range(last_index):
#             # Сравниваем значения текущего и следующего элементов списка.
#             if data[item_index] > data[item_index + 1]:
#                 # Если значения надо поменять местами - меняем.
#                 # Круглые скобки стоят, чтобы перенести длинную строку.
#                 data[item_index], data[item_index + 1] = (
#                     data[item_index + 1], data[item_index]
#                 )
#                 # Выставляем флаг "выполнена перестановка".
#                 swapped = True
#         # После окончания внутреннего цикла проверяем значение флага. 
#         # Если перестановок не было...
#         if not swapped:
#             # ...то выходим из внешнего цикла.
#             break
#     # Возвращаем отсортированный список.
#     return data

# print(bubble_sort(example_array)) 
