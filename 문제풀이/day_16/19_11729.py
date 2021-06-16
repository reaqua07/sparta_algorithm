K = int(input())


def hanoi(K, start, end):
    if K == 1:
        print(start, end)
        return
    else:
        hanoi(K - 1, start, 6 - start - end)
        print(start, end)
        hanoi(K - 1, 6 - start - end, end)


print(2 ** K - 1)
hanoi(K, 1, 3)
