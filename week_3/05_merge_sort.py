array = [5, 3, 2, 1, 6, 8, 7, 4]
# 병합정렬
# 재귀 이용 = 탈출 조건 꼭 써주기

def merge_sort(array):
    # 탈출조건 1보다 작거나 같을 때
    if len(array) <= 1:
        # 바로 출력해라
        return array
    # 데이터를 반으로 쪼갠다
    mid = len(array) // 2
    # 왼쪽의 데이터 값
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(left_array, right_array)


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!