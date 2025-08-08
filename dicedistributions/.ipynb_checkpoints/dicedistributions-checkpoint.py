from collections import Counter
from fractions import Fraction
from math import gcd, lcm
from functools import reduce
import sys

A, B, C = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()[1:]]

sums = Counter()
CA, CB = Counter(A), Counter(B)
for va, ca in CA.items():
    for vb,cb in CB.items():
        sums[va+vb] += ca * cb

known = Counter(C)
kmin = min(known)
kmin_cnt = known[kmin]
known_items = list(known.items())

new_die = Counter()
for s in sorted(sums):
    k = sums.get(s,0)
    if k == 0:
        continue

    mult = Fraction(k, kmin_cnt)
    d = s - kmin
    new_die[d] += mult

    for fv, cnt in known_items:
        t = fv+d
        if t in sums:
            sums[t] -= cnt*mult
            if sums[t] == 0:
                del sums[t]


denom = reduce(lcm, [value.denominator for value in new_die.values()], 1)

face_counts =  {}
for face, v in new_die.items():
    count = int(v* denom)
    if count > 0:
        face_counts[face] = count

g = reduce(gcd, face_counts.values(), 0)

if g > 1:
    face_counts = {face: cnt // g for face, cnt in face_counts.items()}
        
faces2 = []
for face, cnt in face_counts.items():
    faces2.extend([face] * cnt)
faces2.sort()

print(len(faces2))
print(' '.join(map(str, faces2)))
