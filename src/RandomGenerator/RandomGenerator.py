from src.RandomGenerator.Gen_Random_Num_Without_Seed_Decimal import Gen_Random_Num_Without_Seed_Decimal


class RandomGenerator:
    result = 0

    def random_without_seed_decimal(self, start, end):
        self.result = Gen_Random_Num_Without_Seed_Decimal(start, end)
        return self.result
