# Scrie o functie unique_pair_sum care primeste o lista de numere intregi si
# o valoare tinta. Functia returneaza o multime de perechi unice de numere care adunate
# dau valoarea tinta. Fiecare pereche trebuie sa fie reprezentata ca un tuplu (a, b)
# unde a <= b.
# Ex:
# Input:
# numbers = [1, 2, 3, 4, 3, 5, 6]
# target = 7
# Output:
# {(1, 6), (2, 5), (3, 4)}


def unique_pair_sum(numbers, target):
    pairs = set()
    seen = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)

    return pairs


user_input = input("Introduceti numere separate de virgula: ")
numbers = [int(x.strip()) for x in user_input.split(",")]
target = int(input("Introduceti valoarea tinta: "))

result = unique_pair_sum(numbers, target)
print(result)
