# Scrie o funcție run_length_encoding care primește un șir de caractere și
# returnează o versiune comprimată a șirului folosind codificarea tip Run-Length Encoding
# (RLE). Aceasta înlocuiește grupurile consecutive de caractere identice cu caracterul și
# numărul de apariții consecutive. Ex: text = "aaabbbbcccdde" output: "a3b4c3d2e1"


def run_length_encoding(text):
    try:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        if len(text) == 0:
            return ""

        result = ""
        current_char = text[0]
        count = 1

        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result += current_char + str(count)
                current_char = text[i]
                count = 1

        result += current_char + str(count)

        return result
    except TypeError as e:
        print(f"Error: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""


if __name__ == "__main__":
    # Test cases
    print(run_length_encoding("aaabbbbcccdde"))
    print(run_length_encoding("aaa"))
    print(run_length_encoding("abc"))
    print(run_length_encoding(""))
    print(run_length_encoding(123))