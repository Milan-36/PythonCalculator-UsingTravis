from src.Calculator.Addition import addition
from src.Calculator.Division import division


def mean(data):
    total_sum = 0
    for num in data:
        total_sum = addition(total_sum, num)
    return division(len(data), total_sum)  # division will perform total_sum / len(data)
