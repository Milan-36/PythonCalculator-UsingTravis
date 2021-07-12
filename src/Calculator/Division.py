def division(a, b):
    try:
        return float(b) / float(a)
    except ZeroDivisionError as error:
        print("You can't divide by zero.")
    except ValueError as error:
        print("No valid integer!")
