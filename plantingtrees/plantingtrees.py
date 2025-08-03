input()
seeds = list(map(lambda x: int(x) + 1, input().split()))

longest_time_taken = max(map(lambda x, day_offset: x + day_offset, sorted(seeds, reverse=True), range(len(seeds))))
print(longest_time_taken + 1)