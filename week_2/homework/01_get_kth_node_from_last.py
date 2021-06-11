class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # # 전체 길이를 알아낸 다음
        # # -k 를 하면 k의 위치를 알 수 있다
        #
        # # head 포함함 : 시작 노드의 길이를 세기 위함
        # length = 1
        # # node 를 이동하기 위한 변수
        # cur = self.head
        #
        # # 반복문을 통해 끝까지 돌려준다.
        # while cur.next is not None:
        #     cur = cur.next
        #     # 돌아가는 만큼 length 는 업데이트 됨
        #     length += 1
        # # k의 위치
        # end_length = length - k
        # # cur 변수를 이동시키며 k의 값을 찾자
        # cur = self.head
        #
        # # end_length 만큼 반복할거니까 포문
        # for i in range(end_length):
        #     # end_length 에 도달하게 되면 그 자리가 k의 자리이기때문에
        #     # cur 이 도착하면 값 받아올수있음
        #     cur = cur.next
        #
        # return cur

        #  1. 노드를 두개 잡는다
        #  2. 한 노드를 다른 노드보다 k 만큼 떨어지게 한다.
        #  3. 그리고 계속 한 칸씩 같이 이동한다.
        #  4. 만약 더 빠른 노드가 끝에 도달했다면
        #  5. 느린 노드는 끝에서 k 만큼 떨어진 노드가 되므로 바로 반환

        slow = self.head
        fast = self.head

        for i in range(k):
            # k 만큼 next로 보냄
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow

# 6 7 8
linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
                                    # 뒤에서 두번째
print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!