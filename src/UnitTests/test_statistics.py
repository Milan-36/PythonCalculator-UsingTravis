# always put test in prefix on the test file name.
import unittest  # to test individual units of source code
# from random import seed, randint
# from numpy import var, std
from src.Statistics.Statistics import Statistics  # where the operations are performed
from src.CsvReader.CSVReader import CsvReader  # to read the csv file
from src.StaticProperties.Static_Variables import StaticVariables


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # seed(5)
        self.statistics = Statistics()
        self.CSVData = CsvReader(StaticVariables.Statistics_csv).data
        self.testData = [int(row[StaticVariables.val1]) for row in self.CSVData]

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        self.assertEqual(self.statistics.mean(self.testData), 30)

    def test_median_calculator(self):
        self.assertEqual(self.statistics.median(self.testData), 20)

    def test_mode_calculator(self):
        self.assertEqual(self.statistics.mode(self.testData), [10])

    def test_variance_calculator(self):
        self.assertEqual(self.statistics.variance(self.testData), 520)

    def test_standardDeviation_calculator(self):
        self.assertEqual(round(self.statistics.standardDeviation(self.testData), 3), 22.804)


if __name__ == '__main__':
    unittest.main()
