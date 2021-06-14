T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    count = 0
    movement = 1
    total_movement = 0

    while total_movement < distance:
        count += 1
        total_movement += movement
        if count % 2 == 0:
            movement += 1
    print(count)
    # print(total_movement)
