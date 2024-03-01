# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.
from typing import TextIO
__all__ = ['read_file', 'read_line_or_begin',]


def read_line_or_begin(fd: TextIO) -> str:
    """
    Эта функция читает строку файла и автоматически переходит на начало файла, если строки нет.
    :param fd:  -на вход принимает объект TextIO (файл, открытый в контекстном менеджере)
    :return:    -возвращает считанную строку
    """
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def read_file(file1: str, file2: str, file3: str):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, \
            open(file3, 'a', encoding='utf-8') as f3:
        length1 = len(f1.readlines())
        length2 = len(f2.readlines())
        length3 = max(length1, length2)
        for _ in range(length3):
            line1 = read_line_or_begin(f1)
            name = read_line_or_begin(f2)
            a, b = [float(i) for i in line1.split(' | ')]
            mult = a * b
            if mult > 0:
                name = name.upper()
                mult = round(mult)
            else:
                name = name.lower()
                mult = abs(mult)
            f3.write(f'{name}{mult}\n')


if __name__ == '__main__':
    read_file('output.txt', 'names.txt', 'passw.txt')


