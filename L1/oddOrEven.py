# 2. OddOrEven: Creeaza un program care cere userului un numar intreg si afiseaza daca acest numar este par sau impar. (hint, '%' returneaza restul impartirii)

num = int(input("Introduceti numarul: "))

if num % 2 == 0:
    print(f"even")
else:
    print(f"odd")