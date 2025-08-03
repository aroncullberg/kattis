row, col = map(int, input().split())

A = []
for _ in range(row):
    A.append(list(input()))
print()
ohno = 0
for y in range(row):
    for x in range(col):
        if A[y][x] == "0":
            if y - 1 > 0:
                if A[y - 1][x] != "0":
                    continue
                elif 
            if y - 1 > 0:
                if A[y - 1][x] != "0":
                    continue

            ohno += 1
            print(y,x)
            
print(A)