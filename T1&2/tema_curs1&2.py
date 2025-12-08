# Scrieti un program care citeste de la tastatura litere, pe rand, atat timp cat nu se introduce o cifra sau un caracter special.
# La introducerea unei cifre sau a unui caracter special, sa se afiseze un mesaj de eroare.
# Ex: a t e y u f r o 5
# Eroare!

while True:
    caracter = input("Introduceti un caracter: ")
    if not caracter.isalpha():
        print("Eroare!")
        break