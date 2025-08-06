from collections import Counter
from math import gcd
from functools import reduce
import sys

A, B, C = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()[1:]]

sum_hist = Counter(a+b for a in A for b in B)

C_freq = Counter(C)
c_min = min(C_freq)

unknown_counts = Counter()

while sum_hist:
    s = min(sum_hist)
    k = sum_hist[s]

    m = k // C_freq[c_min]
    d = s-c_min
    unknown_counts[d] += m

    for c, cnt_c in C_freq.items():
        t = c+d
        sum_hist[t] -= cnt_c * m
        if sum_hist[t] == 0:
            del sum_hist[t]


g = reduce(gcd, unknown_counts.values())
result = []
for face, count in unknown_counts.items():
    result.extend([face] * (count // g))

print(len(result))
print(' '.join(map(str, sorted(result))))