from collections import Counter
from fractions import Fraction
from math import gcd
from functools import reduce
import sys

import time

t0 = time.perf_counter()

A, B, C = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()[1:]]

dt = time.perf_counter() - t0
print(f"{dt * 1000:.3f}ms\tIO")
t0 = time.perf_counter()

sums = Counter(a+b for a in A for b in B)
known_die = Counter(C)
min_known = min(known_die)
new_die = Counter()

dt = time.perf_counter() - t0
print(f"{dt * 1000:.3f}ms\tSetup of vars")
t0 = time.perf_counter()

while sums:
    s = min(sums)
    k = sums[s]

    multiplier = Fraction(sums[s], known_die[min(known_die)])
    d = s - min(known_die)
    new_die[d] += multiplier

    for face_val, cnt in known_die.items():
        t = face_val + d
        if t in sums:
            sums[t] -= cnt * multiplier
            if sums[t] == 0:
                del sums[t]

dt = time.perf_counter() - t0
print(f"{dt * 1000:.3f}ms\tLoop to generate new die faces prototype")
t0 = time.perf_counter()

denom = 1
for value in new_die.values():
    denom = denom * value.denominator // gcd(denom, value.denominator)

dt = time.perf_counter() - t0
print(f"{dt * 1000:.3f}ms\tExtracting denominators")
t0 = time.perf_counter()

faces = []
for face, v in new_die.items():
    faces.extend([face] * int(v * denom))

dt = time.perf_counter() - t0
print(f"{dt * 1000:.3f}ms\tTime for making new faces list:  ")
t0 = time.perf_counter()



g = 0
for cnt in Counter(faces).values():
    g = gcd(g, cnt)
if g > 1:
        face_counts = Counter(faces)

        reduced = []
        for face, cnt in face_counts.items():
            reduced.extend([face] * (cnt // g))

        faces = sorted(reduced)

dt = time.perf_counter() - t0
print(f"{dt * 1000:.3f}ms\treducing list for uneccessary dupblicates")
t0 = time.perf_counter()

print(len(faces))
print(' '.join(map(str, faces)))


# (base) aroncull100@23a737045eaa:~/work/kattis/dicedistributions$ python dicedistributions.py < dicedistributions1.in 
# 0.054ms IO
# 0.071ms Setup of vars
# 0.361ms Loop to generate new die faces prototype
# 0.008ms Extracting denominators
# 0.044ms Time for making new faces list:  
# 0.014ms reducing list for uneccessary dupblicates
# 6
# 1 2 3 4 5 6