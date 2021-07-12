def square(a):
    try:
        return float(a) * float(a)
    except ValueError:
        print("No valid integer!")
