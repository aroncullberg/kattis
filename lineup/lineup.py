import sys

data = sys.stdin.read().strip().split()
n = int(data[0])
names = data[1:]

if names == sorted(names):
    print("INCREASING")
elif names == sorted(names, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")