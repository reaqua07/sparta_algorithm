from math import factorial

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    function = factorial(M) // (factorial(N) * factorial(M-N))

    print(function)

