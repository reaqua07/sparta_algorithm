N = int(input())

dot = []

for i in range(N):
    x, y = map(int, input().split())
    # y 좌표 기준으로 정렬하기 위해
    dot.append([y, x])

sorted_dot = sorted(dot)

for i in range(N):
    print(sorted_dot[i][1], sorted_dot[i][0])

