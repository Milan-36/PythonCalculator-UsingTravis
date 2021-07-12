# reference: https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
from collections import Counter


def calculate_mode(data):
    try:
        total = len(data)
        count = Counter(data)
        get_mode = [k for k, v in count.items() if v == count.most_common(1)[0][1]]
        if total == len(get_mode):
            return "Mode not found."
        else:
            return get_mode
    except ValueError:
        print("No valid integer!")
    except IndexError:
        print("It's a empty list.")
