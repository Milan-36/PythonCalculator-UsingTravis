def division(a, b):
    try:
        return float(b) / float(a)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except ValueError:
        print("No valid integer!")
