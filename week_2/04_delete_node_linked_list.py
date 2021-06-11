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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1

        return node

        # index    next_node
        # ["자갈"] ["밀가루"] -> ['우편']
        #         new_node
        #     -> ["흑연"] ->
        # index.next = new_node
        # new_node.next = next_node

    def add_node(self, index, value):
        new_node = Node(value)  # [6]

        # index 값이 0 일 경우도 생각해야 한다.
        # 아래에서 -1 처리를 했기 때문에 에러가 날 수 있으니까
        if index == 0:
            # head를 바로 new_node로 지정하면 안되는 이유 : 이전의 head value가 사라짐
            # next 값으로 미리 넘겨주고 비어있는 head 자리를 채운다.
            new_node.next = self.head # [6] [5]
            self.head = new_node # head= [6] [5]
            return

        node = self.get_node(index - 1) # [5]
        next_node = node.next # [12]
        node.next = new_node # [5] [6]
        new_node.next = next_node # [6] [12]

    # delete
    def delete_node(self, index):
        # head.node를 제거하라는 명령
        if index == 0:
            self.head = self.head.next
            return

        node = self.get_node(index-1)
        node.next = node.next.next

        return ""

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0,3)
linked_list.append(8)
# print(linked_list.get_node(0).data) # -> 5를 들고 있는 노드를 반환해야 합니다!

# index-1를 가져와야 원하는 위치 지정이 될 수 있다.
# [5] [6] [12] [8]
linked_list.add_node(1, 6)
linked_list.print_all()