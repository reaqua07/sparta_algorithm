from sys import stdin

N = int(stdin.readline())

num = 0

for i in range(1, N + 1):
    sum_part = list(map(int, str(i)))
    num = i + sum(sum_part)
    # 분해합이 된다면 생성자이다
    if num == N:
        print(i)
        break
    # 입력값과 같다면 생성자가 없다
    if i == N:
        print(0)