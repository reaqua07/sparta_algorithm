import sys

N, M, V = map(int, sys.stdin.readline().split())

# 행렬을 N +1(인덱스 맞추기 위해) 만들어서 길이 연결된 곳을 표시
matrix = [[0] * (N + 1) for _ in range(N + 1)]

# 방문 표시
visited = [0] * (N + 1)

# 길이 연결된 곳을 1 표시
for _ in range(M):
    line = list(map(int, sys.stdin.readline().split()))
    # 양방향이기때문에 둘다 표시
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1


def DFS(v_start):
    # 방문함
    visited[v_start] = 1
    print(v_start, end=' ')
                # N 만큼 반복
    for i in range(1, N + 1):
            # 방문한적 없음       # 연결 다리 있음
        if visited[i] == 0 and matrix[v_start][i] == 1:
            DFS(i)


def BFS(v_start):
    # 시작번호로 큐만들기
    queue = [v_start]
    # dfs를 돌면서 방문지가 1로 변환되었기 때문에
    visited[v_start] = 0
    while queue:
        # 첫번째 큐로 저장된 숫자를 시작 번호로 다시 만듦
        v_start = queue.pop(0)
        print(v_start, end=' ')
        for i in range(1, N + 1):
                #  방문한 적 없음
            if visited[i] == 1 and matrix[v_start][i] == 1:
                queue.append(i)
                # 방문한 적 있음으로 바꿔줌
                visited[i] = 0


DFS(V)
print()
BFS(V)