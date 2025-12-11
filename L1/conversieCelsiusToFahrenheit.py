# 1. TemperatureConversion: Scrie un program care cere utilizatorului input grade Celsius si le converteste in grade farenheit.
#  Farenheit = Celsius x 9/5 + 32

try:
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"Fahrenheit: {fahrenheit}")
except ValueError:
    print("Eroare: Introduceti un numar valid.")
