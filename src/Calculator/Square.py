def square(a):
    try:
        return float(a) * float(a)
    except ValueError as error:
        error = "No valid integer!"
        return error
