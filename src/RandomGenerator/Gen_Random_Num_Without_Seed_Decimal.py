from numpy.random import uniform


def Gen_Random_Num_Without_Seed_Decimal(start, end):
    random = uniform(start, end)  # uniform() is a method specified in the random library
    random_no_seed_decimal = round(random, 4)      # rounding the number upto 4 decimal places
    return random_no_seed_decimal
