# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.
from random import randint, choice
__all__ = ['gen_name', 'rec_file', ]
VOWELS = {'a', 'o', 'u', 'e', 'i', 'y'}


def gen_name():
    """
    Генерирует случайное имя.

    Имя должно начинаться с заглавной буквы,
    состоять из 4-7 букв, среди которых
    обязательно должны быть гласные.
    """
    length = randint(4, 7)
    min_letter = ord('a')
    max_letter = ord('z')
    name = ''
    for i in range(length):
        name += chr(randint(min_letter, max_letter))
    for letter in name:
        if letter in VOWELS:
            pass
        else:
            name = name.replace(choice(list(name)), choice(list(VOWELS)))
            name = name.capitalize()
            return name
    name = name.capitalize()
    return name


def rec_file(lines: int, name: str):
    """
    Записывает в файл имена.
    """
    with open(name, 'a', encoding='utf-8') as f:
        for _ in range(lines):
            f.write(f'{gen_name()}\n')


if __name__ == '__main__':
    rec_file(15, 'names.txt')
