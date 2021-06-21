from sys import stdin
import math

T = int(stdin.readline())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())
    # 원의 방정식
    distance = math.sqrt((x1 -x2) ** 2 + (y1 - y2) ** 2)
    # 동심원이면서 반지름이 같다 = 같은 원
    if distance == 0 and r1 == r2:
        print(-1)
                    # 내접원                       # 외접원
    elif distance == abs(r1 - r2) or distance == abs(r1 + r2):
        print(1)
        # 두점
    elif abs(r1 - r2) < distance < abs(r1 + r2):
        print(2)
        # 동심원이면서 반지름이 다르면 만날 수가 없다
    else:
        print(0)

