import pytest
from Calculator import calculate, convert_precision

def test_normal_tolerance(): # Тест нормального порядка точности
    assert convert_precision(0.000001) == 6
    assert convert_precision(0.0001) == 4

def test_bigger_than_one_tolerance():
    assert convert_precision(1.01) is None

def test_addition():  # Тест сложения
    assert calculate('+', 99, 1) == 100
    assert calculate('+', 1.11111111, 2.222222222, tolerance = 1e-6) == 3.333333
    assert calculate('+', 1, 2, 3, 4) == 10

def test_subtraction():  # Тест вычитания
    assert calculate('-', 1000, 1) == 999
    assert calculate('-', 3.7654321, 1.654321, tolerance = 1e-5) == 2.11111
    assert calculate('-', 10, 3, 2, 1) == 4

def test_multiplication():  # Тест умножения
    assert calculate('*', 1000, 1) == 1000
    assert calculate('*', 4.543534, 2, tolerance = 1e-4) == 9.0871
    assert calculate('*', 1, 2, 3, 4) == 24

def test_division():  # Тест деления
    assert calculate('/', 1000, 1) == 1000
    assert calculate('/', 4.2352352, 1.4324245, tolerance = 1e-3) == 2.957
    assert calculate('/', 10, 2, 5) == 1

def test_divisionByZero():  # Тест деления на ноль
    with pytest.raises(ZeroDivisionError):
        calculate('/', 5, 0)
        calculate('/', 1, 2, 0)

def test_invalidOperation():  # Тест неверной операции
    with pytest.raises(ValueError):
        calculate('^', 1, 2)

def test_incorrect_number_of_arguments(): # Тест на неверное кол-во аргументов
    with pytest.raises(ValueError):
        calculate('+', 1)

def test_medium(): # Тест среднего значения
    assert calculate('medium', 1, 2, 3, 4, 5) == 3
    assert calculate('medium', 10, 20, 30, 40) == 25
    assert calculate('medium', 1.5, 2.5, 3.5) == 2.5

def test_variance(): # Тест дисперсии
    assert calculate('variance', 1, 2, 3, 4, 5) == 2
    assert calculate('variance', 10, 20, 30, 40) == 125
    assert calculate('variance', 1.5, 2.5, 3.5) == 0.666667

def test_std_deviation(): # Тест стандартного отклонения
    assert calculate('std_deviation', 1, 2, 3, 4, 5) == 1.414214
    assert calculate('std_deviation', 10, 20, 30, 40) == 11.180340
    assert calculate('std_deviation', 1.5, 2.5, 3.5) == 0.816497

def test_median(): # Тест медианы
    assert calculate('median', 1, 2, 3, 4, 5) == 3
    assert calculate('median', 1, 2, 3, 4) == 2.5
    assert calculate('median', 7, 1, 3, 4, 2) == 3

def test_IQR(): # Тест межквартильного размаха
    assert calculate('IQR', 1, 2, 3, 4, 5, 6, 7, 8, 9) == 5
    assert calculate('IQR', 1, 1, 1, 1, 1, 1) == 0
    assert calculate('IQR', 5, 7, 8, 12, 15, 18) == 8



