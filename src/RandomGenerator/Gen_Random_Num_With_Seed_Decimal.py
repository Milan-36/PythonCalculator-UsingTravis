from numpy import random
from src.RandomGenerator.Gen_Random_Num_Without_Seed_Decimal import Gen_Random_Num_Without_Seed_Decimal


def Gen_Random_Num_With_Seed_Decimal(start, end, seed):
    # The getstate() method of the random module returns an object with the
    # current internal state of the random number generator.
    state = random.get_state()
    random.seed(seed)
    try:
        random_decimal = Gen_Random_Num_Without_Seed_Decimal(start, end)
        return random_decimal
    finally:
        random.set_state(state)
