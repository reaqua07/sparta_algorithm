from sys import stdin

N = int(stdin.readline())

paper = [list(map(int, stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0


def division(x, y, n):
    global white
    global blue

    check_color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check_color != paper[i][j]:
                check_color = -1
                break
    if check_color == -1:
        n //= 2
        division(x, y, n)
        division(x + n, y, n)
        division(x, y + n, n)
        division(x + n, y + n, n)
    elif check_color == 1:
        blue += 1
    elif check_color == 0:
        white += 1


division(0, 0, N)

print(white)
print(blue)
