class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 현재 tail 뒤에 추가
    # 아무것도 없는 경우 에러 발생
    def enqueue(self, value):
        new_node = Node(value)
        # 노드에 데이터가 없다면 새로 들어가는 데이터가 head 이면서 tail 값으로 들어가야 함
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node
        return

    # 선입선출 : 빼는 값은 head 데이터부터 빠진다
    # 뺄 head 값을 없애기 전 변수에 미리 저장
    # 노드가 비어있으면 에러발생
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    # head 데이터 반환함
    # 비어있으면 예외처리
    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    # head 데이터가 있는지 없는지 반환
    # 없으면 True
    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())