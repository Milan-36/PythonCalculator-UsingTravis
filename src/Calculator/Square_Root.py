def square_root(a):
    try:
        return float(a) ** (1 / 2)
    except ValueError as error:
        error = "No valid integer!"
        return error
