from collections import deque
import sys

N = int(input())
queue = deque([])


def push(n):
    queue.append(n)


def pop():
    if not queue:
        print(-1)
    else:
        print(queue.popleft())


def size():
    print(len(queue))


def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)


def front():
    try:
        print(queue[0])
    except:
        print('-1')


def back():
    try:
        print(queue[-1])
    except:
        print('-1')


for _ in range(N):
    order = sys.stdin.readline()
    if 'push' in order:
        p, num = order.split()
        num = int(num)
        push(num)
    elif 'pop' in order:
        pop()
    elif 'size' in order:
        size()
    elif 'empty' in order:
        empty()
    elif 'front' in order:
        front()
    elif 'back' in order:
        back()
