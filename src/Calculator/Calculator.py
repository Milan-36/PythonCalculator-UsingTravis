from src.Calculator.Addition import addition
from src.Calculator.Subtraction import subtraction
from src.Calculator.Multiplication import multiplication
from src.Calculator.Division import division
from src.Calculator.Square import square
from src.Calculator.Square_Root import square_root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiple(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def sq(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = square_root(a)
        return self.result
