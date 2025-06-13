import pytest
from Calculator import calculate

def test_addition():  # Тест сложения
    assert calculate(99, 1, '+') == 100

def test_subtraction():  # Тест вычитания
    assert calculate(1000, 1, '-') == 999

def test_multiplication():  # Тест умножения
    assert calculate(1000, 1, '*') == 1000

def test_division():  # Тест деления
    assert calculate(1000, 1, '/') == 1000

def test_divisionByZero():  # Тест деления на ноль
    with pytest.raises(ZeroDivisionError):
        calculate(5, 0, '/')

def test_invalidOperation():  # Тест неверной операции
    assert calculate(1, 2, '^'), "Invalid input operation"
