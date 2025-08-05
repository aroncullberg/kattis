s = input().strip()

MOD = 1000000007
n = len(s)
s = list(s)
k = s.count('?')


prefix_ones = [0] * (n + 1)
suffix_zeros = [0] * (n + 1)
suffix_questions = [0] * (n + 1)

for i in range(n):
    prefix_ones[i + 1] = prefix_ones[i] + (1 if s[i] == '1' else 0)


for i in range(n-1, -1, -1):
    suffix_zeros[i] = suffix_zeros[i + 1] + (1 if s[i] == '0' else 0)
    suffix_questions[i] = suffix_questions[i + 1] + (1 if s[i] == '?' else 0)


fixed_inv = 0
for i in range(n):
    if s[i] == '0':
        fixed_inv = (fixed_inv + prefix_ones[i]) % MOD

result = fixed_inv * pow(2, k, MOD)

for i in range(n):
    if s[i] == '?':
        # When this ? becomes 1:
        # It creates inversions with zeros and half of questions after it
        contribution = (suffix_zeros[i+1] * pow(2, k-1, MOD)) % MOD
        contribution = (contribution + (suffix_questions[i+1] * pow(2, k-2, MOD))) % MOD
        result = (result + contribution) % MOD

print(result)
