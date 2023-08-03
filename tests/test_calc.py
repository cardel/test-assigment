import pytest

from app.calc import Calculator

class TestCalculator:
    def test_addition(self):
        calc = Calculator()
        result = calc.add(2, 2)
        assert result == 4

    def test_subtraction(self):
        calc = Calculator()
        result = calc.subtract(4, 2)
        assert result == 2

    def test_multiplication(self):
        calc = Calculator()
        result = calc.multiply(2, 2)
        assert result == 4

    def test_division(self):
        calc = Calculator()
        result = calc.divide(4, 2)
        assert result == 2

    def test_square(self):
        calc = Calculator()
        result = calc.square(2)
        assert result == 4

    def test_square_root(self):
        calc = Calculator()
        result = calc.square_root(4)
        assert result == 2


