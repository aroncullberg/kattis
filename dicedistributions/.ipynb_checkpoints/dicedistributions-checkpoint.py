from collections import Counter
from fractions import Fraction
from math import gcd, lcm
from functools import reduce
import sys
import heapq


A, B, C = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()[1:]]

sums = Counter(a+b for a in A for b in B)
sums_heap = list(sums.keys())
heapq.heapify(sums_heap)
known_die = Counter(C)
min_known = min(known_die)
new_die = Counter()
known_die_min = min(known_die)

while sums_heap:
    s = heapq.heappop(sums_heap)
    if s not in sums or sums[s] == 0:
        continue
        
    k = sums[s]

    multiplier = Fraction(sums[s], known_die[known_die_min])
    d = s - known_die_min
    new_die[d] += multiplier

    for face_val, cnt in known_die.items():
        t = face_val + d
        if t in sums:
            sums[t] -= cnt * multiplier
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
