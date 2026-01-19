import os
import math
import statistics

import file_utils
import analysis

#read
numbers = file_utils.read_numbers('input.txt')

if isinstance(numbers, str):
    print(numbers)
else:
    avg = analysis.average(numbers)
    min_val, max_val = analysis.min_max(numbers)
    even_count = analysis.count_even(numbers)

    std_dev = statistics.stdev(numbers) if len(numbers) > 1 else 0
    sqrt_avg = math.sqrt(avg)
    file_size = os.path.getsize('input.txt')

    results = f"""Rezultate:
Numere citite: {numbers}
Media: {avg:.2f}
Minim: {min_val}
Maxim: {max_val}
Numere pare: {even_count}
Deviatie standard: {std_dev:.2f}
Radacina patrata a mediei: {sqrt_avg:.2f}
Dimensiune fisier input: {file_size} bytes
"""

    #write
    file_utils.write_results('output.txt', results)
    print("Rezultatele au fost scrise in fisier.")
