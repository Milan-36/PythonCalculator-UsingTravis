from numpy.random import randint


def Gen_Random_Num_Without_Seed_Integer(start, end):
    random_no_seed_int = randint(start, end)  # uniform() is a method specified in the random library
    return random_no_seed_int
