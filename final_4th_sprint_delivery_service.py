# 132817447 - первая итерация.
# 132878393 - вторая итерация (Актуальная, после 1го ревью).

def calculating_platforms(weight_list: list[int], weight_limit: int) -> int:
    """Функция вычисляет необходимое количество платформ для транспортировки
    роботов. Ограничение - не более 2х роботов, по условию.

    Аргументы:
    - weight_list: list[int] - список веса роботов.
    - weight_limit: int - максимальная нагрузка на платформу.

    Возвращает:
    - объект int. - количество платформ.

    Сортирует список и попарно сравнивает самый тяжелый с легким объекты.
    На платформу всегда грузится самый тяжелый объект, смещая правую границу.
    Если на платформу можно поместить и самый лёгкий объект,
    смещаются обе границы."""

    ordered_weights = sorted(weight_list)
    count: int = 0
    lightest_robot: int = 0
    heaviest_robot: int = len(weight_list) - 1
    while lightest_robot <= heaviest_robot:
        if (ordered_weights[lightest_robot] + ordered_weights[heaviest_robot]
                <= weight_limit):
            lightest_robot += 1
        heaviest_robot -= 1
        count += 1
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        weights = [int(num) for num in file_in.readline().split()]
        max_weight = int(file_in.readline())
    result = calculating_platforms(weights, max_weight)
    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
