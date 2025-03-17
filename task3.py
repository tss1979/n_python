from fractions import Fraction

# Заданное вещественное число
number = 14.375

# Преобразуем число в дробь
fraction = Fraction(number).limit_denominator()  # наименьшая дробь

# Выводим результат
print(f"{number} = {fraction.numerator}/{fraction.denominator}")