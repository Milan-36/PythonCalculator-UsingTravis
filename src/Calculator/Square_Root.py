def square_root(a):
    try:
        return float(a) ** (1 / 2)
    except ValueError:
        print("No valid integer!")
