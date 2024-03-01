# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов
# внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6
# из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов
# и расширение.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет  для работы с файлами
import os
__all__ = ['file_rename']


def file_rename(path_to_dir, old_file_name, new_file_name, number, num, extention_old, extention_new, old_name_part):
    a, b = old_name_part
    if old_file_name.split('.')[-1] == extention_old:
        os.rename(path_to_dir+'\\'+old_file_name, f'{path_to_dir}\\{"".join(old_file_name.split(".")[a:b+1])}{new_file_name}{"0"*(number-len(str(num)))}{str(num)}.{extention_new}')


if __name__ == '__main__':
    path_to_dir = 'D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar7\Texts'
    for i in range(len(os.listdir(path_to_dir))):
        print(os.listdir(path_to_dir)[i])
        file_rename(path_to_dir, os.listdir(path_to_dir)[i], 'text_file', 3, i, 'txt', 'rtf', [0,3])
