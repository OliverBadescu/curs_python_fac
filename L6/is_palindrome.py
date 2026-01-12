# Scrie o funcție is_palindrome care primește un șir de caractere și verifică dacă
# este un palindrom, ignorând literele mari și spațiile. Un șir este un palindrom dacă este
# identic atunci când este citit de la stânga la dreapta și de la dreapta la stânga. Ex: text = "A
# man a plan a canal Panama", output: True


def is_palindrome(text):
    try:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        cleaned = text.replace(" ", "").lower()

        return cleaned == cleaned[::-1]
    except TypeError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


if __name__ == "__main__":
    # Test cases
    print(is_palindrome("A man a plan a canal Panama"))
    print(is_palindrome("hello"))
    print(is_palindrome("race car"))
    print(is_palindrome(""))
    print(is_palindrome(123))