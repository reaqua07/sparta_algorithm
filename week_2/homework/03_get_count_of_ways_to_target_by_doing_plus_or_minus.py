numbers = [1, 1, 1, 1, 1]
target_number = 3

# 모든 경우의 수를 담을 변수
# result = []

# target을 출력하기까지 나올 수 있는 모든 경우의 수를 추출하는 함수
# 새로운 index 즉 마지막 달라지는 가지, 이부분으로 인해 경우의 수가 2개 추가
# def get_all_ways_to_by_doing_plus_or_minus(
#         array, current_index, current_sum, all_ways):
#     if current_index == len(numbers):
#         all_ways.append(current_sum)
#         return
#
#     get_all_ways_to_by_doing_plus_or_minus(
#         array, current_index + 1, current_sum + numbers[current_index], all_ways
#     )
#     get_all_ways_to_by_doing_plus_or_minus(
#         array, current_index + 1, current_sum - numbers[current_index], all_ways
#     )
#
# print(get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result))
# print(result)

# 몇번될지 모르니까 카운팅 하자
result_count = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index, current_sum):
    if current_index == len(numbers):
        if current_sum == target:
            # index값이 무조건 끝에 도달했다고 추가되는 것이 아니라
            # target하는 숫자와 같을때 넣어야 한다.
            # 함수 안에서 함수 밖에 선언한 변수를 변환하고 싶을 때는 global
            global result_count
            result_count += 1
        return
    
    # 재귀 함수
    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum + numbers[current_index]
    )
    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum - numbers[current_index]
    )


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0))  # 5를 반환해야 합니다!
print(result_count)