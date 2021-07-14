from numpy import random
from src.RandomGenerator.Gen_Random_Num_Without_Seed_Integer import Gen_Random_Num_Without_Seed_Integer


def Gen_Random_Num_With_Seed_Integer(start, end, seed):
    # The getstate() method of the random module returns an object with the
    # current internal state of the random number generator.
    state = random.get_state()
    random.seed(seed)
    try:
        random_int = Gen_Random_Num_Without_Seed_Integer(start, end)
        return random_int
    finally:
        random.set_state(state)
