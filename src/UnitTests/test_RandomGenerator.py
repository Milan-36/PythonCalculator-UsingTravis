import unittest
from pprint import pprint
from src.RandomGenerator.RandomGenerator import RandomGenerator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = RandomGenerator()
        self.start = 1
        self.end = 1000
        self.length = 3
        self.seed = 5
        self.num_val = 3

    def test_instantiate_calculator_self(self):
        self.assertIsInstance(self.random, RandomGenerator)

    def test_random_without_seed_integer(self):
        test_int_random = self.random.random_num_without_seed_integer(self.start, self.end)
        pprint(test_int_random)
        self.assertEqual(isinstance(self.random.random_num_without_seed_integer(self.start, self.end), int), True)

    def test_random_without_seed_decimal(self):
        test_decimal_random = self.random.random_num_without_seed_decimal(self.start, self.end)
        pprint(test_decimal_random)
        self.assertEqual(isinstance(self.random.random_num_without_seed_decimal(self.start, self.end), float), True)

    def test_random_with_seed_integer(self):
        test_seed_int_random = self.random.random_num_with_seed_integer(self.start, self.end, self.seed)
        pprint(test_seed_int_random)
        self.assertEqual(self.random.random_num_with_seed_integer(self.start, self.end, self.seed),
                         test_seed_int_random)

    def test_random_with_seed_decimal(self):
        test_seed_decimal_random = self.random.random_num_with_seed_decimal(self.start, self.end, self.seed)
        pprint(test_seed_decimal_random)
        self.assertEqual(self.random.random_num_with_seed_decimal(self.start, self.end, self.seed),
                         test_seed_decimal_random)


if __name__ == '__main__':
    unittest.main()
