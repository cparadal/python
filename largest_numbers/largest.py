#!/usr/bin/env python3
# Example: largest.py 5 numbers.txt

from heapq import nlargest
import sys

numbers = int(sys.argv[1])
numbers_file = sys.argv[2]

def to_numbers(it):
    for line in it:
        try:
            yield int(line)
        except ValueError:
            continue

with open(numbers_file) as data:
    largest_numbers = nlargest(3, to_numbers(data))
    print(largest_numbers)