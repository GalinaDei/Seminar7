# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
from pathlib import Path

__all__ = ['sort_file',]


def sort_file(path_to_dir: str):
    for file_name in os.walk(path_to_dir):
        for file in file_name[-1]:
            if file.split('.')[-1] in ['txt', 'rtf', 'docx', 'html', ]:
                try:
                    p = Path(Path(path_to_dir).parents[0]) / 'Texts'
                    p.mkdir()
                    os.replace(os.path.join(path_to_dir, file), p / file)
                except:
                    p = Path(Path(path_to_dir).parents[0]) / 'Texts'
                    os.replace(os.path.join(path_to_dir, file), p / file)
            elif file.split('.')[-1] in ['m4a', 'wma', 'WAW', 'MP3', 'mp3', 'wav', 'WMA', ]:
                try:
                    p = Path(Path(path_to_dir).parents[0]) / 'Audio'
                    p.mkdir()
                    os.replace(os.path.join(path_to_dir, file), p / file)
                except:
                    p = Path(Path(path_to_dir).parents[0]) / 'Audio'
                    os.replace(os.path.join(path_to_dir, file), p / file)
            elif file.split('.')[-1] in ['mp4', 'MP4', 'ASF', 'asf', 'FLV', 'flv', 'MKV', 'mkv']:
                try:
                    p = Path(Path(path_to_dir).parents[0]) / 'Video'
                    p.mkdir()
                    os.replace(os.path.join(path_to_dir, file), p / file)
                except:
                    p = Path(Path(path_to_dir).parents[0]) / 'Video'
                    os.replace(os.path.join(path_to_dir, file), p / file)
            elif file.split('.')[-1] in ['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG', 'tiff', ]:
                try:
                    p = Path(Path(path_to_dir).parents[0]) / 'Image'
                    p.mkdir()
                    os.replace(os.path.join(path_to_dir, file), p / file)
                except:
                    p = Path(Path(path_to_dir).parents[0]) / 'Image'
                    os.replace(os.path.join(path_to_dir, file), p / file)


if __name__ == '__main__':
    sort_file("D:\Galina\DATA_Analyst_GeekBrains\Tecknological_specialization\Data_ingineer\Python\Seminar7\Common_files")
