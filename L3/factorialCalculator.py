# Scrie o functie factorial(n) care calculeaza factorialul unui numar
# n. Folositi aceasta functie intr-un program care cere de la tastatura un numar intreg si
# returneaza factorialul acestuia.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


try:
    n = int(input("Introduceti un numar intreg: "))
    if n < 0:
        print("Eroare: Numar negativ")
    else:
        print(f"{n}! = {factorial(n)}")
except ValueError:
    print("Eroare: Introduceti un numar valid")