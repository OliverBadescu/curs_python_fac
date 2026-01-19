# Crearea și utilizarea pachetelor Python
# Descriere:
# Creează un pachet Python numit geometry care conține două module:
# 1. circle.py: funcții pentru aria și circumferința unui cerc.
# 2. rectangle.py: funcții pentru aria și perimetrul unui dreptunghi.
# Apoi creează un script principal care folosește acest pachet.
# Structura directorului
# geometry/
# __init__.py
# circle.py
# rectangle.py
# main.py

from geometry import circle, rectangle

radius = 5
print(f"Cerc cu raza {radius}:")
print(f"  Aria: {circle.area(radius):.2f}")
print(f"  Circumferința: {circle.circumference(radius):.2f}")

length = 10
width = 4
print(f"\nDreptunghi cu lungimea {length} și lățimea {width}:")
print(f"  Aria: {rectangle.area(length, width)}")
print(f"  Perimetrul: {rectangle.perimeter(length, width)}")