jack, jill = map(int, input().split())

d = [False] * 1000001

for _ in range(jack):
    d[int(input())] = True

similar = 0
for _ in range(jill):
    if d[int(input())]:
        similar += 1

print(similar)

