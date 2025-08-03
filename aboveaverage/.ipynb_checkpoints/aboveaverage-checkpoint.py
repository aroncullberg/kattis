import sys
import statistics as stat

data = list(map(int, sys.stdin.read().split()))
testcases = data[0]
idx = 1

for _ in range(testcases):
    n = data[idx]
    idx += 1
    grades = data[idx:idx + n]
    idx += n

    avg = stat.mean(grades)
    above = sum(g > avg for g in grades)
    pct = above / n * 100

    print(f"{pct:.3f}%")
