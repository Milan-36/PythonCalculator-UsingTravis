def addition(a, b):
    try:
        return float(a) + float(b)
    except ValueError as error:
        print("No valid integer!")
