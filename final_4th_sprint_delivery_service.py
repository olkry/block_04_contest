def calculating_platforms(weight_list: list[int], weight_limit: int) -> str:
    """Функция вычисляет необходимое количество платформ для транспортировки
    роботов. Ограничение - не более 2х роботов, по условию.

    Аргументы:
    - weight_list: list[int] - список веса роботов.
    - weight_limit: int - максимальная нагрузка на платформу.

    Возвращает:
    - объект str. - количество платформ, в виде строки для записи в файл.

    Сортирует список и попарно сравнивает самый тяжелый с легким объекты.
    На платформу всегда грузится самый тяжелый объект, смещая правую границу.
    Если на платформу можно поместить и самый лёгкий объект,
    смещаются обе границы."""

    weight_list.sort()
    count: int = 0
    left: int = 0
    right: int = len(weight_list) - 1
    while left <= right:
        if weight_list[left] + weight_list[right] <= weight_limit:
            left += 1
        right -= 1
        count += 1
    return str(count)


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        weights = [int(num) for num in file_in.readline().split()]
        max_weight = int(file_in.readline())
    result = calculating_platforms(weights, max_weight)
    with open('output.txt', 'w') as file_out:
        file_out.write(result)
