finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 1 : 최솟값
# 16 : 최대값
# 1단계 1-16까지 범위 - 8 : 시도할 값
# 2단계 9-16까지 범위 - 12 : 시도값
# 3단계 13-16까지 범위 - 14 : 시도값

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) -1
    # // 나누기 두번하면 소수점 잘라서 가져옴
    current_guess = (current_min + current_max) // 2
    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        # 이분하여 타겟이 여전히 크다면 up이기 때문에
        # 시도값보다 1이 큰 숫자로 최솟값을 변경하여야 한다.
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)