from itertools import permutations

MAX_CASES = 4001
casecount = 0
try:
    while casecount <= MAX_CASES:
        flag = True
        try:
            casecount += 1
            lst = input().split()

            n = int(lst[0])
            if n == 0:
                break

            numbers = []
            for i in range(n):
                numbers.append(int(lst[i + 1]))

            result = int(lst[n + 1])

            expression = input()

            letters = [chr(i) for i in range(97, 97 + n)]

            for perm in permutations(numbers, n):
                exp = expression
                count = 0
                for i, char in enumerate(expression):
                    if char.isalpha():
                        exp = exp[:i] + str(perm[count]) + exp[i + 1:]
                        count += 1

                if int(eval(exp)) == result:
                    print("YES")
                    flag = False
                    break
            if flag:
                print("NO")
        except:
            if flag:
                print("NO")
except EOFError:
    pass

