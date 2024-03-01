# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
import os
from random import randint
from pathlib import Path

__all__ = ['multi_file_gen', 'file_gen', ]

def file_gen(link, extention, min_len_name=6, max_len_name=30, min_vol=256, max_vol=4096, quant=42):
    for i in range(quant):
        while True:
            file_name = ''
            min_letter = ord('a')
            max_letter = ord('z')
            name_len = randint(min_len_name, max_len_name)
            for i in range(name_len):
                file_name += chr(randint(min_letter, max_letter))
            if file_name not in os.listdir(link):
                break
        file_content = ''
        file_size = randint(min_vol, max_vol)
        for i in range(file_size):
            file_content += chr(randint(min_letter, max_letter))
        try:
            with open(Path(link) / str(file_name+'.'+extention), 'w') as f:
                f.write(file_content)
        except:
            os.mkdir(link)
            with open(Path(link) / str(file_name+'.'+extention), 'w') as f:
                f.write(file_content)


# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


def multi_file_gen(path_to_dir, min_len_name, max_len_name, min_vol, max_vol, **kwargs):
    dct = {**kwargs}
    for k, v in dct.items():
        file_gen(path_to_dir, k, min_len_name=min_len_name, max_len_name=max_len_name, min_vol=min_vol, max_vol=max_vol, quant=v)


if __name__ == '__main__':
    link = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar7\Common_files'
    multi_file_gen(link, 6, 10, 2, 100, txt=3, docx=1)
