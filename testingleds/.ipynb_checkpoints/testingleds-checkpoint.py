import sys

try:
    print(sorted([parts for parts in (line.split() for line in sys.stdin.read().splitlines()[1:]) if len(parts) > 0 and parts[1] == "0"], key=lambda x: int(x[0]))[0][0])
except:
    print("-1")
