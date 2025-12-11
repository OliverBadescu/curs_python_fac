# NumberGuessing: Creează un joc simplu de ghicit un număr, unde programul alege un
# număr aleator între 1 și 20. Utilizatorul are 5 încercări pentru a ghici numărul. După fiecare
# încercare, programul va oferi feedback ("Prea mare", "Prea mic", sau "Corect!"

import random

numar_secret = random.randint(1, 20)
incercari = 5
ghicit = False

print("Am ales un numar intre 1 si 20. Ai 5 incercari!")

while incercari > 0 and not ghicit:
    try:
        ghicire = int(input(f"Incercarea {6 - incercari}/5: "))

        if ghicire == numar_secret:
            print("Corect!")
            ghicit = True
        elif ghicire > numar_secret:
            print("Prea mare")
            incercari -= 1
        else:
            print("Prea mic")
            incercari -= 1
    except ValueError:
        print("Eroare: Introduceti un numar valid")

if not ghicit:
    print(f"Ai pierdut! Numarul era {numar_secret}.")