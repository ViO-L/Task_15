# Задание 1. Логирование с использованием нескольких файлов.

import logging

logger = logging.getLogger('multi_file_logger')
logger.setLevel(logging.DEBUG)

# Обработчик для debug и info
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.addFilter(lambda record: record.levelno <= logging.INFO)

# Обработчик для warning и errors
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")

# Задача 2. Работа с текущим временем и датой

from datetime import datetime
import pandas as pd

now = datetime.now()

print(f"Сегодня: {now.date()}")
print(f"Время: {now.time().strftime('%H:%M:%S')}")
print(f"День недели: {pd.Timestamp(now).day_name()}")
print(f"Номер недели в году: {now.isocalendar()[1]}")

# Задача 3. Планирование задач

from datetime import datetime, timedelta


def future_date(days):
    now = datetime.now().date()
    return now + timedelta(days=days)


# Примеры:
print(future_date(5))
print(future_date(10))
print(future_date(-5))

# Задача 4. Опции и флаги

import argparse

parser = argparse.ArgumentParser(description="Скрипт принимает число и строку")

parser.add_argument('num', type=int, help='Число(целое)')
parser.add_argument('string', type=str, help='Строка')
parser.add_argument('--verbose', action='store_true', help='Дополнительная информация')
parser.add_argument('--repeat', type=int, default=1, help='Сколько раз повторить строку (по умолчанию 1)')

args = parser.parse_args()

if args.verbose:
    print(f"[INFO] Число: {args.num}")
    print(f"[INFO] Строка: {args.string}")
    print(f"[INFO] Повторение строки {args.repeat} раз(а)")

for i in range(args.repeat):
    print(f"{i+1}: {args.string}")

