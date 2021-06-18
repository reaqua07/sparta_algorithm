N, M = map(int, input().split())
target_queue = list(map(int, input().split()))
queue = [i for i in range(1, N + 1)]

result = 0


def push_front(N):
    queue.insert(0, N)


def push_back(N):
    queue.append(N)


def pop_front():
    return queue.pop(0)


def pop_back():
                    # 인덱스 값은 -1
    return queue.pop(len(queue) - 1)


for num in target_queue:
    # 뽑으려는 수의 위치 인덱스
    target_position = queue.index(int(num))
    # 앞에서 뽑을지 뒤에서 뽑을지 최소값 찾기
    # 뽑으려는 위치가 앞쪽에서 가까운 경우
    if target_position < len(queue) - target_position:
        # 뽑으려는 위치까지 포문을 돌아서
        for _ in range(target_position):
            # 앞에서 뽑은 숫자를 뒤에 붙인다
            push_back(pop_front())
            # 움직인만큼을 count
            result += 1
        # 뽑으려는 수
        pop_front()
    # 뽑으려는 위치가 뒤쪽에서 가까운 경우
    else:
        for _ in range(len(queue) - target_position):
            push_front(pop_back())
            result += 1
        pop_front()

print(result)

# https://hooongs.tistory.com/102