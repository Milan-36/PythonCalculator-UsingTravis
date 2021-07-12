def multiplication(a, b):
    try:
        return float(a) * float(b)
    except ValueError as error:
        error = "No valid integer!"
        return error
