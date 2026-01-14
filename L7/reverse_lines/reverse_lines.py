# Scrie o funcție reverse_lines care citește conținutul unui fișier și creează
# un alt fișier unde fiecare rând este scris invers (caracterele din rând sunt inversate).
# Ex:
# Fisierul input.txt contine:
# Python este grozav.
# Îmi place să lucrez cu fișiere.
# Fisierul output.txt va contine:
# .vazorg etse nohtyP
# .ereșiif uc zercul să ecalp îmÎ


def reverse_lines(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            lines = infile.readlines()

        reversed_lines = [line.rstrip('\n')[::-1] + '\n' for line in lines]

        with open(output_file, "w") as outfile:
            outfile.writelines(reversed_lines)

        print(f"Reverse lines written to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError as e:
        print({e})


if __name__ == "__main__":
    reverse_lines("input.txt", "output.txt")