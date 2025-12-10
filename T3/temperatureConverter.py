# Scrieti un program care face conversie a unei valori de temperatura data, dintr-o unitate de masura in alta (Celsius, Fahrenheit, Kelvin).
#
# De exemplu:
#    10° Celsius in Kelvin.
# Trebuie sa folositi functii si, in functie de nevoie, notiunile invatate pana acum (if, for, while, variabile globale, etc).
# Exemple de apel:
#    convert_temperature(100, "C", "F")  # Output: 212.0
#    convert_temperature(212, "F", "K")  # Output: 373.15
#    convert_temperature(0, "K", "C")      # Output: -273.15


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return None

    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        return None


print(convert_temperature(100, "C", "F"))
print(convert_temperature(212, "F", "K"))
print(convert_temperature(0, "K", "C"))