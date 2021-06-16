N = int(input())

target_num = "666"
start_num = 666
count = 0
while N != 0:
    if target_num in str(start_num):
        count += 1
    if count == N:
        print(start_num)
        break

    start_num += 1
