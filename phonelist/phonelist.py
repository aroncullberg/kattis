t = int(input())


def overlap(strings):
    sorted_strings = sorted(strings)

    for i in range(len(sorted_strings) - 1):
        current = sorted_strings[i]
        next_str = sorted_strings[i + 1]

        if next_str.startswith(current):
            return True

    return False


for _ in range(t):
    n = int(input())
    numbers = []
    for i in range(n):
        number = input()
        numbers.append(number)

    print("NO" if overlap(numbers) else "YES")
