T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    # 몫
    ho_num = N // H + 1
    # 나머지
    floor_num = N % H
    if N % H == 0:
        ho_num = N // H
        floor_num = H

    print(f'{floor_num*100+ho_num}')