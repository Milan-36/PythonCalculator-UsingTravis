from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean
# from src.CsvReader.CSVReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        # self.data = CsvReader(filepath)
        super().__init__()
        pass

    def mean(self, data):
        self.result = mean(data)
        return self.result
