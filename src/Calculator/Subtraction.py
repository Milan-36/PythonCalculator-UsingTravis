def subtraction(a, b):
    try:
        return float(b) - float(a)
    except ValueError as error:
        error = "No valid integer!"
        return error
