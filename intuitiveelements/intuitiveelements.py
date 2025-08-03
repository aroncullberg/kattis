n = int(input())

for _ in range(n):
    a = set(input())
    b = set(input())
    print("YES" if b.issubset(a) else "NO")