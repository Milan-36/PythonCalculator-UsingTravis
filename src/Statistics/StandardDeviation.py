from src.Calculator.Square_Root import square_root
from src.Statistics.Variance import calculate_variance


def calculate_standardDeviation(data):
    try:
        return square_root(calculate_variance(data))
    except ValueError:
        print("No valid integer!")
    except IndexError:
        print("It's a empty list.")