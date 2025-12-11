# 2. OddOrEven: Creeaza un program care cere userului un numar intreg si afiseaza daca acest numar este par sau impar. (hint, '%' returneaza restul impartirii)

try:
    num = int(input("Introduceti numarul: "))
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
except ValueError:
    print("Eroare: Introduceti un numar valid")