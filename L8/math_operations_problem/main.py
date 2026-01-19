# Scrierea scripturilor Python ca module
# Descriere:
# Scrie un script Python numit math_operations.py care conține funcții pentru următoarele
# operații:
# 1. Adunare
# 2. Scădere
# 3. Înmulțire
# 4. Împărțire
# Apoi, scrie un alt script care importă modulul math_operations și folosește aceste funcții.

import math_operations

print("Adunare: 10 + 5 =", math_operations.add("10", 5))
print("Scadere: 10 - 5 =", math_operations.subtract(10, 5))
print("Inmultire: 10 * 5 =", math_operations.multiply(10, 5))
print("Impartire: 10 / 5 =", math_operations.divide(10, 5))