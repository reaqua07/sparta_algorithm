array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]
# merge 병합 정렬
# 두 집합을 합할 때 요소를 비교하며 새로운 임의의 집합에 합하여 넣음

def merge(array1, array2):
    # 합친 요소를 넣어 줄 집합
    array3 = []
    # index 값을 저장해줄 변수
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            array3.append(array1[array1_index])
            array1_index += 1
        else :
            array3.append(array2[array2_index])
            array2_index += 1
    # 만약 비교후 한쪽에 요소가 남을 경우
    # 1번 집합이 끝났다는 것은 2번 집합이 남았다는 것
    if array1_index == len(array1):
        while array2_index < len(array2):
            array3.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            array3.append(array1[array1_index])
            array1_index += 1

    return array3


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!