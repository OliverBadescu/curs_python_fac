# Scrie o functie inverted_index care primeste o lista de siruri de caractere
# (fiecare sir reprezentand un document) si returneaza un dictionar. Dictionarul trebuie
# sa asocieze fiecarui cuvant unic un set de indici ai documentelor in care apare acel cuvant.
# Ex:
# Input:
# documents = [
#     "pisica a stat pe covor",
#     "cainele a stat in ceata",
#     "pisica si cainele s-au jucat impreuna"
# ]
# Output:
# {
#     'pisica': {0, 2},
#     'a': {0, 1},
#     'stat': {0, 1},
#     'pe': {0},
#     'covor': {0},
#     'cainele': {1, 2},
#     'in': {1},
#     'ceata': {1},
#     'si': {2},
#     's-au': {2},
#     'jucat': {2},
#     'impreuna': {2}
# }


def inverted_index(documents):
    index = {}

    for doc_index, document in enumerate(documents):
        words = document.split()
        for word in words:
            if word in index:
                index[word].add(doc_index)
            else:
                index[word] = {doc_index}

    return index


print("Introduceti documente:")
documents = []
while True:
    line = input()
    if line == "":
        break
    documents.append(line)

result = inverted_index(documents)
print(result)
