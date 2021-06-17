N, M = map(int, input().split())

Trees = list(map(int, input().split()))

left = 1
right = max(Trees)

while left <= right:
    mid = (left + right) // 2
    tree_sum = 0
    for i in Trees:
        if i > mid:
            tree_sum += (i - mid)
    if tree_sum >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)