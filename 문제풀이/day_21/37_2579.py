from sys import stdin

N = int(stdin.readline())

# 계단의 점수 저장
input_score = []
# i 번째 계단까지의 최대값 저장
dp = []

for _ in range(N):
    input_score.append(int(stdin.readline()))

if N == 1:
    print(input_score[0])
    exit()
elif N == 2:
    print(max(input_score[0]+input_score[1], input_score[1]))
    exit()

# 포문에서 i-3 이 있기 때문에 이 값이 0 이 되는 경우까지는 값을 넣어준다.
# 1번 계단 밟았을 때까지의 최대값
dp.append(input_score[0])
# 2번 계단 밟았을 때까지의 최대값
dp.append(max(dp[0]+input_score[1], input_score[1]))
# 3번 계단 밟았을 때까지의 최대값
dp.append(max(dp[0]+input_score[2], input_score[1]+input_score[2]))

# N번 계단의 3 전부터 생각해야함
for i in range(3, N):
                    # 1칸 올라와야 할때 / 2칸 올라와야 할때
    dp.append(max(dp[i-3]+input_score[i]+input_score[i-1], dp[i-2]+input_score[i]))

# 가장 마지막으로 저장된 노드
print(dp[-1])