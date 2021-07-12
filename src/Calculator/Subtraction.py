def subtraction(a, b):
    try:
        return float(b) - float(a)
    except ValueError as error:
        print("No valid integer!")
