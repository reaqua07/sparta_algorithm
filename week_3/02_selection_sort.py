input = [4, 6, 2, 9, 1]
# 선택 정렬 : 최솟값을 찾아 정렬한다.
# 4 6 2 9 1
# - - - - -
# 1 6 2 9 4
#   - - - -
# 1 2 6 9 4
#     - - -
# 1 2 4 9 6
#       - -
                # 마지막에는 비교하지 않는다 그래서 하나 빠짐
# for i in range(5-1):
    # 비교가 점점 하나씩 줄어가니까
    # for j in range(5 - i):
    #     print(i+j)


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            # min_index 보다 더 작은 값이 나오면
            # 현재 실행된 인덱스  / 지금까지 가장 최솟값
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i] , array[min_index] = array[min_index], array[i]

    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!