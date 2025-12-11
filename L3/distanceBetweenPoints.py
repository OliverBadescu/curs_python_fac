# Scrie o functie distance(x1, y1, x2, y2) ce calculeaza distanta
# euclideana intre doua puncte (x1, y1) si (x2, y2). Foloseste aceasta functie intr-un program
# care cere coordonatele a doua puncte si printeaza distanta intre ele.

import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


try:
    print("Punctul 1:")
    x1 = float(input("  x1: "))
    y1 = float(input("  y1: "))
    print("Punctul 2:")
    x2 = float(input("  x2: "))
    y2 = float(input("  y2: "))

    dist = distance(x1, y1, x2, y2)
    print(f"Distanta: {dist}")
except ValueError:
    print("Eroare: Introduceti numere valide.")