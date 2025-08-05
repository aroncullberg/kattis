# import random
print("1")
# num = 2
while True:
    num = int(input())
    # print("P1 [ ", num, end='')
    if num == 1:
        pass
    elif num == 97:
        num += 2
    elif num == 98:
        num += 1
    # elif num % 2 == 0:
    #     num += 2
    # else:
    #     num += 1
    else:
        num += (num % 3 if num % 3 != 0 else 2)
    print(num)
    # print("P1", num)
    if num >= 99:
        break
    # num += 1
    # num += min(random.randint(1, 2), 99)

    # print("P2", num)
    # if num >= 99:
    #     break
