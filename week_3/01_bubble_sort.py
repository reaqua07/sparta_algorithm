input = [4, 6, 2, 9, 1]
# 4 6 2 9 1
# 4 2 6 1 9
# 2 4 1 6 9
# 2 1 4 6 9
# 1 2 4 6 9

            # 마지막 한 번은 정렬하지 않아도 되기 때문에 -1
# for i in range(5-1):
                # i 만큼의 횟수 정렬은 이미 정렬됐기 때문에 뺄 수 있다
    # for j in range(5-i-1):
    #     print(j)

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1): # n의 길이만큼 반복
        for j in range(n - i - 1):  # n의 길이만큼 반복
            # 값 비교 후 교체 작업
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]

    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!