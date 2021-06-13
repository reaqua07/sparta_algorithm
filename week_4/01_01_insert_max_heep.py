class MaxHeap:
    def __init__(self):
        # 완전 이진 트리를 구성하기 위해서는 초기값 None 값이 들어가야 한다
        self.items = [None]

    # 힙에 삽입
    # 1. 새 노드를 맨 끝에 추가한다.
    # 2. 지금 넣은 새 노드를 부모 노드와 비교한다. 만약 부모보다 크다면 교체
    # 3. 이 과정을 꼭대기까지 반복한다.

    def insert(self, value):
        # 새 값 넣기
        self.items.append(value)
        # 새 값이 들어가는 마지막 노드의 index 위치를 알아야 하기 때문에
                    # 현재 길이에서 -1
        cur_index = len(self.items) - 1
        # 꼭대기에 도달할 때까지 반복
        # 현재 index가 1 이 되면 멈춤
        while cur_index > 1:
            # 부모 인덱스 가져오는 방법
            parent_index = cur_index // 2
            # 현재 인덱스의 값이 부모 인덱스의 값보다 크다면
            if self.items[cur_index] > self.items[parent_index]:
                # 두 값을 바꿔라
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                # cur_idx 값이 위로 올라가게 된다
                cur_index = parent_index
            else:
                # 값을 비교했는데 현재 인덱스 값이 더 작으면 끝남
                break

        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!