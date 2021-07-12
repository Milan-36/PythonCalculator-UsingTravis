from src.Calculator.Addition import addition
from src.Calculator.Division import division


def calculate_mean(data):
    try:
        total_sum = 0.0
        for num in data:
            total_sum = addition(total_sum, num)
        return division(len(data), total_sum)  # division will perform total_sum / len(data)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except ValueError:
        print("No valid integer!")
    except IndexError:
        print("It's a empty list.")
