def subtraction(a, b):
    try:
        return float(b) - float(a)
    except ValueError:
        print("No valid integer!")
