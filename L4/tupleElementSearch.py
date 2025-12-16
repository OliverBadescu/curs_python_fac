# Scrie un program care creeaza o tupla din inputul primit de la
# tastatura (valori separate prin virgula). Apoi, cere utilizatorului sa introduca o valoare care sa
# fie cautata in tupla. Printeaza daca valoarea se regaseste in tupla sau nu, iar daca da, printeaza
# indexul la care se gaseste aceasta.
# ex: input: 1, 2
# search for: 2
# tupla: (1, 2)
# output: 2 se regaseste in tupla la indexul 1.

try:
    user_input = input("Introduceti valori separate de virgula: ")
    tupla = tuple(int(x.strip()) for x in user_input.split(","))
    print(f"Tupla: {tupla}")

    search_value = int(input("Cautati valoarea: "))

    if search_value in tupla:
        index = tupla.index(search_value)
        print(f"{search_value} se regaseste in tupla la indexul {index}.")
    else:
        print(f"{search_value} nu se regaseste in tupla.")
except ValueError:
    print("Eroare: Introduceti doar numere intregi valide.")