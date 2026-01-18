import re


def check_password(password):
    errors = []

    checks = [
        (len(password) >= 8, "Parola trebuie sa aiba cel putin 8 caractere."),
        (re.search(r'[A-Z]', password), "Lipsesc litere majuscule."),
        (re.search(r'[a-z]', password), "Lipsesc litere minuscule."),
        (re.search(r'\d', password), "Lipsesc cifre."),
        (re.search(r'[!@#$%^&*()\-_+=<>?]', password), "Lipsesc caractere speciale."),
        (not re.search(r'\s', password), "Parola nu trebuie sa contina spatii."),
    ]

    for condition, message in checks:
        if not condition:
            errors.append(message)

    return errors


def main():
    password = input("Introduceti parola: ")
    errors = check_password(password)

    if not errors:
        print("Parola dvs. este puternica.")
    else:
        print("Parola dvs. este slaba.")
        for error in errors:
            print(error)


if __name__ == "__main__":
    main()
