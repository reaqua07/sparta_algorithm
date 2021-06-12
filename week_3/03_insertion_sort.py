input = [4, 6, 2, 9, 1]
# 삽입 정렬
# 4 6 2 9 1
#  -
# 4 6 2 9 1
#  - -
# 2 4 6 9 1
#  - - -
# 2 4 6 9 1
#  - - - -
# 1 2 4 6 9

# 가장 첫번째 숫자 자리는 이미 비교되어 있다고 생각하기 때문에
#             1에서 시작작
# for i in range(1, 5):
    # i 번째 일수록 늘어감
    # for j in range(i):
    #     print(i - j)

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            # 앞에 있는 숫자가 뒤에 있는 숫자와 비교한다
            if array[i - j -1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j] , array[i - j - 1]
            # 비교했을 때 이미 뒤에 있는 숫자가 크다면
            # 버블 정렬과 선택 정렬과 다른 점 : 이미 정렬되어 있는 경우 break를 통해 나와버림
            # 즉 첫 포문만 돌게 됨(정렬이 된지는 확인을 해야 하니까)
            # 거의 정렬이 된 데이터의 경우 효과적이다
            else :
                break
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!