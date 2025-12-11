# MultiplesFinder: Scrie un program care cere utilizatorului să introducă două numere, x și y,
# și afișează toate multiplurile lui x care sunt mai mici decât y.

try:
    x = int(input("Introduceti x: "))
    y = int(input("Introduceti y: "))

    if x <= 0:
        print("Eroare: x trebuie sa fie un numar pozitiv.")
    else:
        multiplu = x
        while multiplu < y:
            print(multiplu)
            multiplu += x
except ValueError:
    print("Eroare: Introduceti numere intregi valide.")
