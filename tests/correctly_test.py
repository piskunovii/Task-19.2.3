import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc_correctly(self):
        assert self.calc.multiply(self, 4, 4) == 16

    def test_division_calc_correctly(self):
        assert self.calc.division(self, 16, -2) == -8

    def test_subtraction_calc_correctly(self):
        assert self.calc.subtraction(self, 4, 8) == -4

    def test_adding_calc_correctly(self):
        assert self.calc.adding(self, 4, 2) == 6