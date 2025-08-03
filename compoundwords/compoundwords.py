import sys
from itertools import product

lines = sys.stdin.read()
print('\n'.join(sorted({a + b for a, b in product(set(lines.split()), set(lines.split())) if a != b})))

