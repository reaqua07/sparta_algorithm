from sys import stdin

N = int(stdin.readline())

result = 0

col, right_line, left_line = [False] * N, [False] * (2 * N - 1), [False] * (2 * N - 1)


def promising(x):
    global result
    # 퀸이 이미 각 행에 있는 경우
    if x == N:
        result += 1
        return
    for y in range(N):
        # 이 자리에 없으면
        if not (col[y] or right_line[x + y] or left_line[x - y + N - 1]):
            # 이 자리에 퀸이 있어도 된다
            col[y] = right_line[x + y] = left_line[x - y + N - 1] = True
            # 다음 행으로 이동
            promising(x+1)
            # 초기화
            col[y] = right_line[x + y] = left_line[x - y + N - 1] = False


# 첫번째 행부터 살펴봐야 하니까
promising(0)
print(result)
