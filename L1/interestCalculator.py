# 3. InterestCalculator: Scrie un program ce calculeaza dobanda. Programul va cere utilizatorului principalul, rata anuala a dobanzii (ex 5, 6, 10) si timpul in ani. Formula:
# Interest = (Principal x Rate x Time)/100

try:
    principal = float(input("Principal: "))
    rate = float(input("Rata anuala (%): "))
    time = float(input("Timp (ani): "))

    interest = (principal * rate * time) / 100
    print(f"Dobanda: {interest}")
except ValueError:
    print("Eroare: Introduceti un numar valid.")