
'''
1. First digit (d = 1)
    cant be 0
    cant be 9
    so 1-8
    8 possibilities

2. Each digit after the first (d > 1)
    cant be 9
    can be 0-8
    9 possibilities
3. ????
4. Formula: n = 8 * 9^(n-1)
'''

# Is based on this https://www.geeksforgeeks.org/fast-exponentiation-in-python/
def optimize(val, power, mod=1000000007):
    result = pow(val, power//2, mod)
    result = (result * result) % mod

    if power % 2 != 0:
        result = (result * val) % mod
    return result

def count(d):
    MOD = 1000000007

    if d == 1:
        return 8

    return (8 * optimize(9, d-1, MOD)) % MOD

T = int(input())
for _ in range(T):
    d = int(input())
    print(count(d))

