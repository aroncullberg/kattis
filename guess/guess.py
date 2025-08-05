import sys
max = 1000
min = 1
while True:
    mid = min + (max - min) // 2
    sys.stdout.write(str(mid) + "\n")
    sys.stdout.flush()
    ans = sys.stdin.readline().strip()
    if ans == "lower":
        max = mid
    elif ans == "higher":
        min = mid + 1
    elif ans == "correct":
        exit()
