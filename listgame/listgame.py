from math import floor

n = int(input())

factors = []

# 2 divisibles
while n % 2 == 0:
    factors.append(2)
    n = floor(n / 2)

# odd numbers
for i in range(3, int(n ** 0.5) + 1, 2):
    while n % i == 0:
        factors.append(i)
        n = floor(n / i)

# if prime at end
if n > 2:
    factors.append(n)


print(len(factors))
#print(factors)
