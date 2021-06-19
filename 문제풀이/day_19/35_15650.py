from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())

nums = []

for i in range(1, N + 1):
    nums.append(i)

com_list = list(combinations(nums, M))

for i in com_list:
    print(*i, end=' ')
    print()
