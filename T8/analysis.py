def average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except (TypeError, ZeroDivisionError):
        return "Error: Invalid input"

def min_max(numbers):
    try:
        return min(numbers), max(numbers)
    except (TypeError, ValueError):
        return "Error: Invalid input"

def count_even(numbers):
    try:
        return sum(1 for n in numbers if n % 2 == 0)
    except TypeError:
        return "Error: Invalid input"
