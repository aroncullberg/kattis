from collections import Counter
from fractions import Fraction
from math import gcd, lcm
from functools import reduce
import sys
import heapq
import time


A, B, C = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()[1:]]

t0 = time.perf_counter()


sums = Counter(a+b for a in A for b in B)
# print(sums)
sums_heap = list(sums.keys())
# print(f"sums_heap (before heapify): {sums_heap}")
heapq.heapify(sums_heap)
# print(f"sums_heap (after heapify): {sums_heap}")
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

faces = []

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

dt = time.perf_counter() - t0
print(f"{dt * 1000:.3f}ms\t time to loop OLD")
t0 = time.perf_counter()

print(len(faces2))
print(' '.join(map(str, faces2)))


# (base) aroncull100@23a737045eaa:~/work/kattis/dicedistributions$ python dicedistributions.py < dicedistributions1.in 
# 0.054ms IO
# 0.071ms Setup of vars
# 0.361ms Loop to generate new die faces prototype
# 0.008ms Extracting denominators
# 0.044ms Time for making new faces list:  
# 0.014ms reducing list for uneccessary dupblicates
# 6
# 1 2 3 4 5 6