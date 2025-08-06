from collections import Counter
from fractions import Fraction
from math import gcd
from functools import reduce
import sys
import time

start_time = time.time()

A, B, C = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()[1:]]

sum_hist = Counter(a+b for a in A for b in B)

C_freq = Counter(C)
# print(f"Known die: C_freq: {C_freq}")
c_min = min(C_freq)
# print(f"Smallest element in known dice: c_min = {c_min}")
# print(f"How many of smallest element in known die? C_freq[c_min] = {C_freq[c_min]}")

unknown_counts = Counter()

while sum_hist and time.time() - start_time < 5:
    s = min(sum_hist)
    # print(f"Smallest number in what we need to make? s = min(sum_hist) = {min(sum_hist)}")
    k = sum_hist[s]
    # print(f"How many of that number do we have? k = sum_hist[s] = {sum_hist[s]}")

    # m = k // C_freq[c_min]
    m = Fraction(sum_hist[s], C_freq[c_min])
    # print(f"Can we use this number multiple times? {m}")
    d = s-c_min
    # print(f"What will the new die face be? d: {d}")
    unknown_counts[d] += m

    # print(f"\tsum_hist: {sum_hist}")
    for c, cnt_c in C_freq.items():
        # print(f"\tlooking at {c} in known die, there are {cnt_c} of it (count)")
        t = c+d
        # print(f"\t\tsum of known die and new die face? => {c} + {d} = {t}")
        # print(f"\t\tsum_hist[{t}] = {sum_hist[t]} => {sum_hist[t]} - {cnt_c} * {m} = {sum_hist[t] - cnt_c * m} (sum for number minus new number sum * count")
        if t in sum_hist:
            sum_hist[t] -= cnt_c * m
            if sum_hist[t] == 0:
                del sum_hist[t]

    # print('----------------------')

#print(unknown_counts)


denom = 1
for v in unknown_counts.values():
    denom = denom * v.denominator // gcd(denom, v.denominator)

faces = []
for face, v in unknown_counts.items():
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
