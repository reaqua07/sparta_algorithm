import math

A, B = map(int, input().split())

N = {x for x in range(A, B + 1) if x == 2 or x % 2 == 1}

for del_num in range(3, int(math.sqrt(B + 1)), 2):
    N -= {i for i in range(2 * del_num, B + 1, del_num)}

for i in sorted(N):
    # A 가 1을 포함 할 수 있는데, 1은 소수가 아님
    if i > 1:
        print(i)