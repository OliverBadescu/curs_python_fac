# Scrie o functie is_palindrome(word) ce verifica daca un cuvant
# dat este palindrom (se citeste la fel si de la stanga la dreapta, dar si de la dreapta la stanga).
# Functia trebuie sa returneze True cand cuvantul dat este palindrom si False cand nu este
# palindrom. Folositi functia definita intr-un program ce preia de la tastatura un cuvant dat si il
# verifica.


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


cuvant = input("Introduceti un cuvant: ")

if is_palindrome(cuvant):
    print(f"'{cuvant}' este palindrom.")
else:
    print(f"'{cuvant}' nu este palindrom.")