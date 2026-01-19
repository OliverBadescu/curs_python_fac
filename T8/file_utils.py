def read_numbers(filename):
    try:
        with open(filename, 'r') as f:
            numbers = [int(line.strip()) for line in f if line.strip()]
        return numbers
    except (FileNotFoundError, ValueError):
        return "Error: Invalid input"

def write_results(filename, results):
    try:
        with open(filename, 'w') as f:
            f.write(results)
        return True
    except IOError:
        return "Error: Cannot write file"
