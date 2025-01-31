'''
При путешествии по планете марсоход постоянно замеряет высоту рельефа и
сохраняет результаты замеров в массив.

Одна из задач марсохода — поиск «правильных гор». «Правильной» считается та
гора, у которой на пути от подножия до вершины высота постоянно растёт, а на
пути от вершины к подножию — постоянно уменьшается. Если у горы есть несколько
вершин или в каком-то месте встречается
горизонтальный участок — это «неправильная гора».

Напишите функцию valid_mountain_array, которая будет принимать на вход массив
с высотами и возвращать True или False в зависимости от
того, «правильная» это гора или нет.

Если в массиве менее трёх элементов, такой массив не может описывать
«правильную» гору.'''


def valid_mountain_array(array: list):
    # center_index = (int(len(array)/2) if len(array)/2 > int(len(array)/2)
    #                 else int(len(array)/2) - 1)
    # print(center_index)
    higer_index = array.index(max(array))
    if (len(array) < 3 or array[higer_index] == array[-1] or
            array[higer_index] == array[0]):
        return False
    for height in range(1, len(array)):
        if array[height] <= array[height - 1] and height < higer_index:
            return False
        if array[height] >= array[height - 1] and height > higer_index:
            return False
    return True


if __name__ == '__main__':
    with open('input.txt', 'r') as file_inp:
        income_arr = [int(ch) for ch in file_inp.readline().split()]
    result = valid_mountain_array(income_arr)
    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
