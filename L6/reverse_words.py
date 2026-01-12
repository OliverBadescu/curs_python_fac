# Scrie o funcție reverse_words care primește o propoziție (un șir de caractere) și
# returnează o propoziție nouă în care ordinea cuvintelor este inversată, dar ordinea literelor în
# fiecare cuvânt rămâne aceeași. Elimină spațiile suplimentare din propoziție dacă există. Ex:
# sentence = "soricel un cu joaca se pisica", OUTPUT: "pisica se joaca cu un soricel"


def reverse_words(sentence):
    try:
        if not isinstance(sentence, str):
            raise TypeError("Input must be a string")

        words = sentence.split()

        reversed_sentence = " ".join(words[::-1])

        return reversed_sentence
    except TypeError as e:
        print(f"Error: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""


if __name__ == "__main__":
    # Test cases
    print(reverse_words("soricel un cu joaca se pisica"))
    print(reverse_words("hello world"))
    print(reverse_words("  extra   spaces  here  "))
    print(reverse_words(""))
    print(reverse_words(123))