from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import calculate_mean
from src.Statistics.Median import calculate_median


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = calculate_mean(data)
        return self.result

    def median(self, data):
        self.result = calculate_median(data)
        return self.result
