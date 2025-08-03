import sys
lines = iter(sys.stdin.read().splitlines())

#print(list(lines))

for case_idx, first in enumerate(lines, 1):
    n = int(first)
    if n == 0:
        break

    names = [next(lines) for _ in range(n)]
    names.sort(key=lambda s: s[:2])

    if case_idx > 1:
        print()
    print("\n".join(names))