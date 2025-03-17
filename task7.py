def temperature_converter():
    print("Добро пожаловать в конвертер температур!")

    # Запрашиваем у пользователя выбор шкалы
    choice = input(
        "Введите 'C' для преобразования из Цельсия в Фаренгейт или 'F' для преобразования из Фаренгейта в Цельсий: ").strip().upper()

    if choice == 'C':
        celsius = float(input("Введите температуру в градусах Цельсия: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius} °C равно {fahrenheit} °F")

    elif choice == 'F':
        fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit} °F равно {celsius} °C")

    else:
        print("Ошибка: неверный ввод. Пожалуйста, введите 'C' или 'F'.")


# Запускаем конвертер температур
if __name__ == "__main__":
    temperature_converter()