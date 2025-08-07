from collections import Counter
from fractions import Fraction
from math import gcd
from functools import reduce
import sys

A, B, C = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()[1:]]

sums = Counter(a+b for a in A for b in B)

known_die = Counter(C)
min_known = min(known_die)

new_die = Counter()

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

print(new_die)
print(f"number\toccurence")
for key in new_die.keys():
    print(f"{key}\t{new_die[key]}")

print("")
denom = 1
for v in new_die.values():
    denom = denom * v.denominator // gcd(denom, v.denominator)

faces = []
for face, v in new_die.items():
    faces.extend([face] * int(v * denom))

g = 0
for cnt in Counter(faces).values():
    g = gcd(g, cnt)
if g > 1:
        face_counts = Counter(faces)

        reduced = []
        for face, cnt in face_counts.items():
            reduced.extend([face] * (cnt // g))

        faces = sorted(reduced)


print(len(faces))
print(' '.join(map(str, faces)))
