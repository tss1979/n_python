def convert_seconds_to_dhms(total_seconds):
    # Вычисляем количество дней, часов, минут и остаточных секунд
    days = total_seconds // 86400  # 86400 секунд в дне
    hours = (total_seconds % 86400) // 3600  # 3600 секунд в часе
    minutes = (total_seconds % 3600) // 60  # 60 секунд в минуте
    seconds = total_seconds % 60  # Остаток секунд

    # Форматируем результат
    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

try:
    input_seconds = int(input("Введите количество секунд: "))
    result = convert_seconds_to_dhms(input_seconds)
    print(f"{input_seconds} секунд = {result}")
except ValueError:
    print("Пожалуйста, введите целое число.")