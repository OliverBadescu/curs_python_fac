def area(length, width):
    try:
        return length * width
    except TypeError:
        return "Error: Invalid input"

def perimeter(length, width):
    try:
        return 2 * (length + width)
    except TypeError:
        return "Error: Invalid input"
