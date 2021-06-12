# stack : ctrl + z 같이 최근에 생성된 값에 접근하여 삭제하거나
# 삭제 후 그 값을 다시 불러올 수 있다.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # 한 값만 기억하고 있다
        self.head = None

    # 매소드 : 추가
    def push(self, value):
        # 새로 넣어줄 값
        new_head = Node(value)
        # 기존에 저장된 head
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현 : 현재 head 값을 없애기
    # 삭제 한 데이터를 항상 반환해야 한다.
    def pop(self):
        # 예외 처리
        # 만약 스택이 비어있다면 = 삭제 데이터를 가지고 있지 않다면
        if self.is_empty():
            return "Stack is Empty"
        # 삭제 될 데이터
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    # head 값 반환
    def peek(self):
        # 예외 처리
        # 만약 스택이 비어있다면 = 삭제 데이터를 가지고 있지 않다면
        if self.is_empty():
            return "Stack is Empty"
        # self.head 까지만 하면 노드가 오니까 그 값을 정확히 보려고 data
        return self.head.data

    # isEmpty 기능 구현 : head 값이 none 인지 확인하면 비어있는지 확인할 수 있다.
    def is_empty(self):
        # 비어있으면 True 반환
        return self.head is None


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.pop())
print(stack.is_empty())

