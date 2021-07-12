def addition(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        print("No valid integer!")
