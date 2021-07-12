def division(a, b):
    try:
        return float(b) / float(a)
    except ZeroDivisionError as error:
        error = "You can't divide by zero."
        return error
    except ValueError as error:
        error = "No valid integer!"
        return error
