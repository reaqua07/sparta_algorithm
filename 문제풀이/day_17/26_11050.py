# 이항계수 : 경우의 수 구하기

from math import factorial

N, K = map(int, input().split())

function = factorial(N) // (factorial(K) * factorial(N-K))

print(function)
