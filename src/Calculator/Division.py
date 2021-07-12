def division(a, b):
    try:
        return round((float(b) / float(a)), 9)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except ValueError:
        print("No valid integer!")
