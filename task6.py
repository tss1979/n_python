def calculator():
    print("Добро пожаловать в простой калькулятор!")

    # Запрашиваем у пользователя ввод двух чисел
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # Запрашиваем у пользователя выбор операции
    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    operation = input("Введите номер операции (1/2/3/4): ")

    # Выполняем выбранную операцию
    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif operation == '4':
        if num2 != 0:  # Проверка на деление на ноль
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Ошибка: Деление на ноль невозможно!")

    else:
        print("Неверный ввод. Пожалуйста, выберите операцию от 1 до 4.")

# Запускаем калькулятор
if __name__ == "__main__":
    calculator()
