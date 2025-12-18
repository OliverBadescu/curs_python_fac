# Scrie o functie word_frequency care primeste un sir de caractere si
# returneaza un dictionar ce contine frecventa fiecarui cuvant din text. Ignora
# majusculele si semnele de punctuatie.
# Ex: Input
# text = "Ana si Maria au plecat la mare. Maria are rau de mare."
# Output
# {'ana': 1, 'si': 1, 'maria': 2, 'au': 1, 'plecat': 1, 'la': 1, 'mare': 2, 'are': 1, 'rau': 1, 'de': 1}

import string


def word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


text = input("Introduceti textul: ")
result = word_frequency(text)
print(result)
