import unittest
from pprint import pprint
from src.RandomGenerator.RandomGenerator import RandomGenerator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = RandomGenerator()
        # Assigning start and end range of numbers to perform random function.
        self.start = 1
        self.end = 1000
        self.length = 5  # no of random number to append in List.
        self.seed = 5  # Seed function is used to save the state of a random function.

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

    def test_random_list_with_seed_integer(self):
        test_int_list = self.random.random_list_with_seed_integer(self.start, self.end, self.length, self.seed)
        pprint(test_int_list)
        for x in test_int_list:
            test_data = int(x)
            self.assertEqual(isinstance(test_data, int), True)

    def test_random_list_with_seed_decimal(self):
        test_decimal_list = self.random.random_list_with_seed_decimal(self.start, self.end, self.length, self.seed)
        pprint(test_decimal_list)
        for x in test_decimal_list:
            test_data = float(x)
            self.assertEqual(isinstance(test_data, float), True)


if __name__ == '__main__':
    unittest.main()
