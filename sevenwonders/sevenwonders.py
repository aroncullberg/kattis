import sys



line = list(sys.stdin.read().strip())

d = {
    "T": 0,
    "C": 0,
    "G": 0,
}

for letter in line:
    d[letter] += 1

sum = 0
for p in d.values():
    sum += p ** 2

while True:
    if d["T"] > 0 and d["G"] > 0 and d["C"] > 0:
        sum += 7
        d["G"] -= 1
        d["C"] -= 1
        d["T"] -= 1
        continue
    break
    
print(sum)
