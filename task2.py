# Задаем список чисел
numbers = [1, 2, 3, 4, 5, 6, 237, 8, 10, 12]

# Проходим по каждому числу в списке
for number in numbers:
    # Проверяем, если число равно 237, то останавливаем выполнение
    if number == 237:
        print("Встречено число 237, остановка.")
        break
    # Проверяем, является ли число чётным
    if number % 2 == 0:
        print(number)