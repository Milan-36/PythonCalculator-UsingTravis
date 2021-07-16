# always put test in prefix on the test file name.
import unittest  # to test individual units of source code

import numpy
from numpy import var, std
from src.Statistics.Statistics import Statistics  # where the operations are performed
from src.CsvReader.CSVReader import CsvReader  # to read the csv file
from src.StaticProperties.Static_Variables import StaticVariables
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()
        self.CSVData = CsvReader(StaticVariables.Statistics_csv).data
        self.testData = [int(row[StaticVariables.val1]) for row in self.CSVData]

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean_result = numpy.mean(self.testData)
        self.assertEqual(self.statistics.mean(self.testData), mean_result)
        pprint(mean_result)

    def test_median_calculator(self):
        median_result = numpy.median(self.testData)
        self.assertEqual(self.statistics.median(self.testData), median_result)

    def test_mode_calculator(self):
        self.assertEqual(self.statistics.mode(self.testData), [10])

    def test_variance_calculator(self):
        variance_result = var(self.testData)
        self.assertEqual(self.statistics.variance(self.testData), variance_result)
        pprint(variance_result)

    def test_standardDeviation_calculator(self):
        standard_deviation_result = (std(self.testData))
        self.assertEqual(self.statistics.standardDeviation(self.testData), standard_deviation_result)
        pprint(standard_deviation_result)


if __name__ == '__main__':
    unittest.main()
