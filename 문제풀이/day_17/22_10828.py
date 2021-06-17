import sys
input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    order = input().split()
    if order[0] == "push":
        stack.append(int(order[1]))
        print(order[1])
    elif order[0] == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif order[0] == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)