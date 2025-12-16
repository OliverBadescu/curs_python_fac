# Scrie un program care cere de la tastatura o lista de numere
# separate de virgula. Programul trebuie sa converteasca inputul intr-o lista de numere intregi si
# sa afiseze maximul si minimul din lista.

try:
    user_input = input("Introduceti numere separate de virgula: ")
    numbers = [int(x.strip()) for x in user_input.split(",")]

    if not numbers:
        print("Lista este goala.")
    else:
        print(f"Maximum: {max(numbers)}")
        print(f"Minimum: {min(numbers)}")
except ValueError:
    print("Eroare: Introduceti doar numere")