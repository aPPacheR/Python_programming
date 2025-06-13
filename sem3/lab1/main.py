def calculate(x, y, op):
    """
    Реализация простого калькулятора

    Параметры:
        x (int) - Первое число
        y (int) - Второе число
        op (string) - Операция
    Возращает:
        (int) - Вычисленное число
    """
    match op:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y
        case _:
            print('Invalid input operation')

def gues_number(num, first, last):
    """
    Угадывает число x с помощью бинарного поиска в заданном диапазоне

    Параметры:
        num (int) - Число, которое нужно угадать
        first (int) - Начало интервала
        last (int) - Конец интервала
    Возращает:
        (string) - Угаданное число и кол-во сравнений
    """
    numberOfCompare = 0
    middle = 0
    while first <= last:
        middle = (first + last) // 2
        if middle == num:
            numberOfCompare += 1 # Сравнение для проверки искомого числа
            return f"Your number is {middle} for {numberOfCompare} comparisons" # Вывод, если число было найдено
        elif middle < num:
            numberOfCompare += 2 # Сравнение для проверки, +2 так как до этого мы сравнивали с middle
            first = middle + 1
        else:
            numberOfCompare += 3 # Сравнение для проверки, +3 так как до этого мы сравнивали с middle и middle < num
            last = middle - 1
    return f"The number was not found" # Вывод, если число не было найдено

# Задача 3.1
print("Сalculator:")
x = int(input("Please, enter the first number - "))
y = int(input("Please, enter the second number - "))
op = input("Please, enter the operation - ")
print("")
if op not in ('+', '-', '/', '*'):
    print("Invalid input operation")
else:
    print(f"{x} {op} {y} = {calculate(x, y, op)}")

print("")

# Задача 3.2
print("Guess number:")
num = int(input("Please, enter the number - "))
first = int(input("Please, enter the beginning of the interval - "))
last = int(input("Please, enter the end of the interval - "))
print("")
print(gues_number(num, first, last))


