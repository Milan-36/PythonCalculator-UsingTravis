from numpy.random import uniform


def Gen_Random_Num_Without_Seed_Decimal(start, end):
    rand = uniform(start, end)
    # round up upto two decimal place digit
    rounded_decimal = round(rand, 2)
    return rounded_decimal
