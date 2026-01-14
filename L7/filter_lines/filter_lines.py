# Scrie o funcție filter_lines care citește conținutul unui fișier și creează
# un alt fișier care conține doar liniile ce includ un cuvânt cheie specific.
# Fisierul input.txt contine:
# Python este un limbaj versatil.
# Java este popular în dezvoltarea enterprise.
# Python este folosit în știința datelor.
# Python este ușor de învățat.
# Fisierul filtered.txt va contine:
# Python este un limbaj versatil.
# Python este folosit în știința datelor.
# Python este ușor de învățat.


def filter_lines(input_file, output_file, keyword):
    try:
        with open(input_file, "r") as infile:
            lines = infile.readlines()

        filtered = [line for line in lines if keyword in line]

        with open(output_file, "w") as outfile:
            outfile.writelines(filtered)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError as e:
        print({e})


if __name__ == "__main__":
    filter_lines("input.txt", "filtered.txt", "Python")