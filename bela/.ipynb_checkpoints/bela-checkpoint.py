import sys

a = sys.stdin.read().splitlines()

dom = a[0].split()[1]
a = a[1:]

key_d = {
"A": 11,
"K": 4,
"Q": 3 ,
"J": 20,
"T": 10,
"9": 14,
"8": 0,
"7": 0,
}
key_nd = {
    "A": 11,
    "K": 4,
    "Q": 3 ,
    "J": 2,
    "T": 10,
    "9": 0,
    "8": 0,
    "7": 0,
}

sum = 0

for thing in a:
    #print(list(thing))
    if list(thing)[1] == dom:
        sum += key_d[list(thing)[0]]
    else:
        sum += key_nd[list(thing)[0]]
        
print(sum)
# print(dom, a)
