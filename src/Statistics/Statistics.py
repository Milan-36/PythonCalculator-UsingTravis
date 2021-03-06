from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import calculate_mean
from src.Statistics.Median import calculate_median
from src.Statistics.Mode import calculate_mode
from src.Statistics.Variance import calculate_variance
from src.Statistics.StandardDeviation import calculate_standardDeviation


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

    def mode(self, data):
        self.result = calculate_mode(data)
        return self.result

    def variance(self, data):
        self.result = calculate_variance(data)
        return self.result

    def standardDeviation(self, data):
        self.result = calculate_standardDeviation(data)
        return self.result
