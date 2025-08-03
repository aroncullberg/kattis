row, col = map(int, input().split())

A = []
for _ in range(row):
    A.append(list(input()))
print()
for y in range(row):
    for x in range(col):
        if A[y][x] == "0":
            print(y,x)
print(A)