from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())

card = list(map(int, stdin.readline().split()))
result = 0


for i in combinations(card, 3):
    temp = sum(i)
                    # 넘지 않는거니까 포함해도 됨
    if result < temp <= M:
        result = temp


print(result)