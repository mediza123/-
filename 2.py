import random
import math
import statistics


def generate_random_numbers(count=100, min_val=1, max_val=100):
    """Генерирует список случайных чисел в заданном диапазоне."""
    return [random.randint(min_val, max_val) for _ in range(count)]


def calculate_stats(numbers):
    """Вычисляет статистические показатели списка чисел."""
    mean = statistics.mean(numbers)  # Среднее арифметическое
    median = statistics.median(numbers)  # Медиана
    stdev = statistics.stdev(numbers)  # Стандартное отклонение (для выборки)
    sqrt_sum = math.sqrt(sum(numbers))  # Квадратный корень из суммы
    sqrt_sum_rounded = round(sqrt_sum, 2)  # Округление до 2 знаков

    return mean, median, stdev, sqrt_sum_rounded


# Генерируем список из 100 случайных чисел
numbers = generate_random_numbers()

# Вычисляем статистику
mean, median, stdev, sqrt_sum = calculate_stats(numbers)

# Выводим результаты
print(f"Среднее: {mean:.2f}, Медиана: {median}, Стандартное отклонение: {stdev:.2f}, Корень из суммы: {sqrt_sum}")
