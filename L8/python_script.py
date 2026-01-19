# 1: Importarea modulelor și utilizarea acestora
# Descriere:
# Creează un script Python care folosește modulul math pentru a calcula:
# 1. Rădăcina pătrată a unui număr dat.
# 2. Factorialul unui număr întreg.
# 3. Valoarea sinusului unui unghi dat în grade.
# Input: num = 25 angle = 30
# Output:
# Rădăcina pătrată a 25 este 5.0
# Factorialul lui 25 este 15511210043330985984000000
# Sinusul unghiului de 30 grade este 0.5

import math

num = 25
angle = 30

try:
    sqrt_result = math.sqrt(num)
    print(f"Radacina patrata a {num} este {sqrt_result}")
except (TypeError, ValueError):
    print("Error: Invalid input")

try:
    factorial_result = math.factorial(num)
    print(f"Factorialul lui {num} este {factorial_result}")
except (TypeError, ValueError):
    print("Error: Invalid input")

try:
    sin_result = math.sin(math.radians(angle))
    print(f"Sinusul unghiului de {angle} grade este {round(sin_result, 1)}")
except (TypeError, ValueError):
    print("Error: Invalid input")