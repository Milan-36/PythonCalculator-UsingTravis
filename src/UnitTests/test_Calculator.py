import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.CSVReader import CsvReader
from src.StaticProperties.StaticVariables import StaticVariables


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        # fetch the data from csv and place in test_addition_data
        test_addition_data = CsvReader(StaticVariables.Addition_csv).data
        for row in test_addition_data:
            self.assertEqual(self.calculator.add(row[StaticVariables.val1], row[StaticVariables.val2]),
                             int(row[StaticVariables.result]))
            self.assertEqual(self.calculator.result, int(row[StaticVariables.result]))
