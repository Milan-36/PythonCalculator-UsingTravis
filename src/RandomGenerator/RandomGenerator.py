from src.RandomGenerator.Gen_Random_Num_Without_Seed_Integer import Gen_Random_Num_Without_Seed_Integer
from src.RandomGenerator.Gen_Random_Num_Without_Seed_Decimal import Gen_Random_Num_Without_Seed_Decimal
from src.RandomGenerator.Gen_Random_Num_With_Seed_Integer import Gen_Random_Num_With_Seed_Integer
from src.RandomGenerator.Gen_Random_Num_With_Seed_Decimal import Gen_Random_Num_With_Seed_Decimal
from src.RandomGenerator.Gen_Random_List_With_Seed_Integer import Gen_Random_List_With_Seed_Integer
from src.RandomGenerator.Gen_Random_List_With_Seed_Decimal import Gen_Random_List_With_Seed_Decimal


class RandomGenerator:
    result = 0

    def random_num_without_seed_integer(self, start, end):
        self.result = Gen_Random_Num_Without_Seed_Integer(start, end)
        return self.result

    def random_num_without_seed_decimal(self, start, end):
        self.result = Gen_Random_Num_Without_Seed_Decimal(start, end)
        return self.result

    def random_num_with_seed_integer(self, start, end, seed):
        self.result = Gen_Random_Num_With_Seed_Integer(start, end, seed)
        return self.result

    def random_num_with_seed_decimal(self, start, end, seed):
        self.result = Gen_Random_Num_With_Seed_Decimal(start, end, seed)
        return self.result

    def random_list_with_seed_integer(self, start, end, length, seed):
        self.result = Gen_Random_List_With_Seed_Integer(start, end, length, seed)
        return self.result

    def random_list_with_seed_decimal(self, start, end, length, seed):
        self.result = Gen_Random_List_With_Seed_Decimal(start, end, length, seed)
        return self.result
