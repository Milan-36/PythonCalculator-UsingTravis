from src.Statistics.Mean import calculate_mean
from src.Calculator.Square import square
from src.Calculator.Division import division
from src.Calculator.Subtraction import subtraction


def calculate_variance(data):
    try:
        mean_value = calculate_mean(data)
        total = len(data)
        deviations = [square(subtraction(mean_value, x)) for x in data]
        return division(total, sum(deviations))
    except ValueError:
        print("No valid integer!")
    except IndexError:
        print("It's a empty list.")
