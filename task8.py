import random

# Задаем диапазон
min_value = int(input("Введите минимальное значение диапазона: "))
max_value = int(input("Введите максимальное значение диапазона: "))

# Генерируем случайное число
random_number = random.randint(min_value, max_value)

# Выводим результат
print(f"Случайное число в диапазоне от {min_value} до {max_value}: {random_number}")