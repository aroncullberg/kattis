import sys

p1d1, p1d2, p2d1 = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()[1:]]

print(p1d1, p1d2, p2d1)