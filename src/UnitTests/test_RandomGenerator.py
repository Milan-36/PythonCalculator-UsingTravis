import unittest
from pprint import pprint
from src.RandomGenerator.RandomGenerator import RandomGenerator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = RandomGenerator()
        self.start = 1
        self.end = 100
        self.length = 3
        self.seed = 5
        self.num_val = 3

    def test_instantiate_calculator_self(self):
        self.assertIsInstance(self.random, RandomGenerator)

    def test_random_without_seed_decimal(self):
        decimal_random = self.random.random_without_seed_decimal(self.start, self.end)
        pprint(decimal_random)
        self.assertEqual(isinstance(self.random.random_without_seed_decimal(self.start, self.end), float), True)


if __name__ == '__main__':
    unittest.main()
