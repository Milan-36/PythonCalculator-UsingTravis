def square(a):
    try:
        return float(a) * float(a)
    except ValueError as error:
        print("No valid integer!")
