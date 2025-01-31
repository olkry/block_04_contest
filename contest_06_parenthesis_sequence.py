'''
Напишите функцию is_correct_bracket_seq(), которая принимает на вход скобочную
последовательность и возвращает True, если последовательность правильная,
и False — в остальных случаях.

Что считать правильной последовательностью
Пустая строка — это правильная скобочная последовательность.
Правильная скобочная последовательность,
взятая в скобки одного типа, — тоже правильная: ( { [ ] } ).
Правильная скобочная последовательность с приписанной слева или
справа правильной скобочной последовательностью — правильная:
( { [ ] } ) ( [ ] ).'''


def is_correct_bracket_seq(arr: str):
    stack = []
    correct_chars = {')': '(', ']': '[', '}': '{'}

    for char in arr:
        if char in '{[(':
            stack.append(char)
        elif char in '}])':
            if not stack or stack[-1] != correct_chars[char]:
                return False
            stack.pop()
    return not stack


if __name__ == '__main__':
    with open('input.txt', 'r') as file_inp:
        income_arr = file_inp.readline()
    result = is_correct_bracket_seq(income_arr)
    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
