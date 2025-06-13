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
    def wrapper(action, *args, tolerance = 1e-6):
        """
        Внутреннее замыкание: добавляет дополнительные действия перед и после вызова func()

        Параметры:
            action(string), *args (int), tolerance (float) - параметры исходной функции calculate
        """
        logging.info(f"На вход функции поступают значения: {args}, а также операция: {action}")
        result = func(action, *args, tolerance = tolerance)
        logging.info(f"Результаты функции calculate: {result}\n")
        return result
    return wrapper

@log_decorator #обернули функцию calculate в декоратор:
def calculate(action, *args, tolerance = 1e-6):
    """
    Реализация простого калькулятора

    Параметры:
        action (string) - Операция
        *args (int) - Числа для вычисления
        tolerance (float) - Значение точности для округления результата
    Возращает:
        (int) - Вычисленное число
    """
    if len(args) < 2:
        raise ValueError("At least 2 arguments are needed")

    precision = convert_precision(tolerance)  # Вычисляем порядок точности
    averageValue = sum(args) / len(args) # Среднее значение

    match action:
        case '+': # Сложение
            return round(sum(args), precision)

        case '-': # Вычитание
            result = args[0]
            for number in args[1:]:
                result -= number
            return round(result, precision)

        case '*': # Умножение
            result = args[0]
            for number in args[1:]:
                result *= number
            return round(result, precision)

        case '/': # Деление
            result = args[0]
            for number in args[1:]:
                if number == 0:
                    raise ZeroDivisionError("Division by zero is prohibited!")
                result /= number
            return round(result, precision)

        case 'medium': # Среднее значение
            return round(averageValue, precision)

        case 'variance': # Дисперсия
            result = sum((x - averageValue) ** 2 for x in args) / len(args)
            return round(result, precision)

        case 'std_deviation': # Стандартное отклонение
            variance = sum((x - averageValue) ** 2 for x in args) / len(args)
            return round(variance ** 0.5, precision)

        case 'median': # Медиана
            sorted_args = sorted(args)
            if len(sorted_args) % 2 == 0:
                result = (sorted_args[len(sorted_args) // 2 - 1] + sorted_args[len(sorted_args) // 2]) / 2
            else:
                result = sorted_args[len(sorted_args) // 2]
            return round(result, precision)

        case 'IQR': # Межквартильный размах
            sorted_args = sorted(args)
            quantity = len(sorted_args)

            if quantity % 2 == 0:
                lowerHalf = sorted_args[:quantity // 2]
                upperHalf = sorted_args[quantity // 2:]

                if len(lowerHalf) % 2 == 1:
                    Q1 = lowerHalf[len(lowerHalf) // 2]
                    Q3 = upperHalf[len(upperHalf) // 2]
                else:
                    Q1 = (lowerHalf[len(lowerHalf) // 2 - 1] + lowerHalf[len(lowerHalf) // 2]) / 2
                    Q3 = (upperHalf[len(upperHalf) // 2 - 1] + upperHalf[len(upperHalf) // 2]) / 2
            else:
                lowerHalf = sorted_args[:quantity // 2]
                upperHalf = sorted_args[quantity // 2 + 1:]
                Q1 = (lowerHalf[len(lowerHalf) // 2 - 1] + lowerHalf[len(lowerHalf) // 2]) / 2
                Q3 = (upperHalf[len(upperHalf) // 2 - 1] + upperHalf[len(upperHalf) // 2]) / 2

            return round(Q3 - Q1, precision)

        case _:
            raise ValueError('Invalid input operation')

def convert_precision(n: float):
    """
    Вычисляет порядок точности для переданного значения

    Параметры:
        n (float) - значение, указывающие на требуемую точность
    Возращает:
        tolerance (int)- порядок точности
    """
    tolerance = 0
    number = n

    if number > 1:
        return None

    while 0 < number < 1:
        number *= 10
        tolerance += 1

    return tolerance

# Основная функция
def main():
    numbers = input("Please, enter numbers separated by spaces - ")
    args = list(map(float, numbers.split())) # Преабразуем введнные числа в список типа float
    action = input("Please, enter the operation (+, -, *, /, medium, variance, std_deviation, median, IQR)- ")
    print("")

    # обработка исключений
    try:
        result = calculate(action, *args, tolerance=1e-6)
        print(f"Result: {result}")
    except ValueError as error:
        print(f"Error: {error}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()