import unittest
from Calculator import calculate

class TestCalculate(unittest.TestCase):
    def test_addition(self): # Тест сложения
        self.assertEqual(calculate(99, 1, '+'), 100)

    def test_subtraction(self): # Тест вычитания
        self.assertEqual(calculate(1000, 1, '-'), 999)

    def test_multiplication(self): # Тест умножения
        self.assertEqual(calculate(1000, 1, '*'), 1000)

    def test_division(self): # Тест деления
        self.assertEqual(calculate(1000, 1, '/'), 1000)

    def test_divisionByZero(self): # Тест деления на ноль
        with self.assertRaises(ZeroDivisionError):
            calculate(5, 0, '/')

    def test_invalidOperation(self): # Тест неверной операции
        self.assertEqual(calculate(1, 2, '^'), "Invalid input operation")