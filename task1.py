def calculate_expression(n):
    nn = str(n) * 2  # Делаем строку из n, повторяя её 2 раза
    nnn = str(n) * 3  # Делаем строку из n, повторяя её 3 раза
    return n + int(nn) + int(nnn)  # Считаем n + nn + nnn

# Запрашиваем у пользователя ввод числа
try:
    number = int(input("Введите целое число n: "))
    result = calculate_expression(number)
    print(f"Результат вычисления {number} + {str(number) * 2} + {str(number) * 3} = {result}")
except ValueError:
    print("Пожалуйста, введите целое число.")