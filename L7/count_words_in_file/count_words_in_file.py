# Scrie o funcție count_words_in_file care citește conținutul unui fișier text
# și returnează numărul total de cuvinte din fișier.
# Ex: fisierul example.txt contine:
# Salut tuturor. Aceasta este o demonstratie de lucru cu fisiere.
# Output: 12


def count_words_in_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except IOError as e:
        print({e})
        return 0


if __name__ == "__main__":
    word_count = count_words_in_file("example.txt")
    print(f"Output: {word_count}")