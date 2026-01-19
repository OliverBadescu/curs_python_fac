import math

def area(radius):
    try:
        return math.pi * radius ** 2
    except TypeError:
        return "Error: Invalid input"

def circumference(radius):
    try:
        return 2 * math.pi * radius
    except TypeError:
        return "Error: Invalid input"
