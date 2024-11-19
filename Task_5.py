import os
import logging
from collections import namedtuple
import argparse

logging.basicConfig(filename='logs.txt',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])


# Функция для сбора информации о директории
def collect_directory_info(directory_path):
    logging.info(f'Сбор информации о содержимом директории: {directory_path}')
    items = []

    try:
        for entry in os.scandir(directory_path):
            name, extension = os.path.splitext(entry.name) if entry.is_file() else (entry.name, None)

            parent_dir = os.path.basename(os.path.dirname(entry.path))
            file_info = FileInfo(name=name, extension=extension, is_dir=entry.is_dir(), parent_dir=parent_dir)
            logging.info(f'Найден объект: {file_info}')
            items.append(file_info)

    except Exception as e:
        logging.error(f'Ошибка при сборе информации: {e}')

    return items


# Функция для работы с аргументами командной строки
def main():
    parser = argparse.ArgumentParser(description="Скрипт для сбора информации о содержимом директории.")
    parser.add_argument('directory', type=str, help='Путь к директории')

    args = parser.parse_args()

    # Проверка существования директории
    if not os.path.isdir(args.directory):
        logging.error(f'Указанный путь не является директорией: {args.directory}')
        print(f'Ошибка: Указанный путь не является директорией.')
        return

    # Сбор информации о содержимом директории
    directory_info = collect_directory_info(args.directory)

    # Вывод информации в консоль
    for item in directory_info:
        print(item)


if __name__ == '__main__':
    main()
