from numpy import random


def Gen_Random_List_With_Seed_Decimal(start, end, length, seed):
    # The getstate() method of the random module returns an object with the
    # current internal state of the random number generator.
    state = random.get_state()
    random.seed(seed)
    try:
        random_int_list = random.uniform(start, end, length)
        return random_int_list
    finally:
        random.set_state(state)
