import random
from datetime import datetime, timedelta
from array import array


def generate_random_date(start_date, end_date):
    """Генерирует случайную дату в заданном диапазоне"""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


def generate_dates_array(count=10):
    """Генерирует массив случайных дат за последние 5 лет"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5 * 365)  # 5 лет назад

    # Создаем массив для хранения timestamp'ов дат
    dates_array = array('l')  # 'l' - тип для хранения long integers

    for _ in range(count):
        random_date = generate_random_date(start_date, end_date)
        # Сохраняем дату как timestamp (количество секунд с epoch)
        dates_array.append(int(random_date.timestamp()))

    return dates_array


def calculate_differences(dates_array):
    """Вычисляет разницы между соседними датами в массиве"""
    differences = []
    for i in range(len(dates_array) - 1):
        # Преобразуем timestamp обратно в datetime
        date1 = datetime.fromtimestamp(dates_array[i])
        date2 = datetime.fromtimestamp(dates_array[i + 1])

        # Вычисляем абсолютную разницу в днях
        delta = abs(date2 - date1)
        differences.append(delta.days)

        # Выводим результат
        print(f"Разница между {date1.date()} и {date2.date()}: {delta.days} дней")

    return differences


# Генерируем массив дат
dates = generate_dates_array()

# Вычисляем и выводим разницы
print("\nРазницы между соседними датами:")
calculate_differences(dates)
