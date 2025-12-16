# Scrie un program ce primeste a input o lista de numere separate de
# virgula, inlatura duplicatele si afiseaza lista cu valori unice in aceeasi ordine in care au aparut
# prima data.
# ex: 1, 1, 2, 3, 4, 4, 5, 4
# output: 1, 2, 3, 4, 5

try:
    user_input = input("Introduceti numere separate de virgula: ")
    numbers = [int(x.strip()) for x in user_input.split(",")]

    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)

    print(", ".join(str(x) for x in unique))
except ValueError:
    print("Eroare: Introduceti doar numere intregi valide.")