import logging

# Настройка базового уровня логирования
logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    """
    Декоратор: принимает другую функцию в качестве аргумента, добавляет к ней
        дополнительное поведение и возвращает измененную функцию

    Параметры:
        func - функция к которой применяется декоратор
    """
    def wrapper(x, y, op):
        """
        Внутреннее замыкание: добавляет дополнительные действия перед и после вызова func()

        Параметры:
            x (int), y(int), op(string) - параметры исходной функции calculate
        """
        logging.info(f"На вход функции поступают значения: {x, y}, а также операция: {op}")
        result = func(x, y, op)
        logging.info(f"Результаты функции calculate: {x} {op} {y} = {result}\n")
        return result
    return wrapper

@log_decorator #обернули функцию calculate в декоратор:
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
            if y == 0:
                raise ZeroDivisionError("Division by zero is prohibited!")
            return x / y
        case _:
            return 'Invalid input operation'

# Основная функция
def main():
    x = int(input("Please, enter the first number - "))
    y = int(input("Please, enter the second number - "))
    op = input("Please, enter the operation - ")
    print("")
    if op not in ('+', '-', '/', '*'):
        print("Invalid input operation")
    else:
        # обработка исключений
        try:
            print(f"{x} {op} {y} = {calculate(x, y, op)}")
        except ZeroDivisionError:
            print("Division by zero is prohibited!")

if __name__ == "__main__":
    main()