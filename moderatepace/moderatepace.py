from statistics import median
import sys

n = int(input())
stat1 = map(int, input().split())
stat2 = map(int, input().split())
stat3 = map(int, input().split())
for t in zip(stat1,stat2,stat3):
    print(median(t))
