n, m = map(int, input().split())
plain = list(map(ord, input()))
cipher = list(map(ord, input()))
# print(plain)
plain = [ord(" ") for _ in range(m - n)] + plain
# print([ord(" ") for _ in range(m - n)])
# print(plain)
# print("".join(map(chr, plain)))
# print(cipher)

for i in range(m - 1, n - 1, -1):
    #print(i - n, chr(cipher[i]), chr(plain[i]), chr(ord("a") + (26 + cipher[i] - plain[i]) % 26))
    plain[i - n] = ord("a") + (26 + cipher[i] - plain[i]) % 26

print("".join(map(chr, plain)))
