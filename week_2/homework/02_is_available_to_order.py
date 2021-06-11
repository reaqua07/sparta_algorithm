shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 존재 여부만 확인할 때는 정렬을 할 필요가 없다 - 집합 활용(중복 허용 안함)

# O(N * logN) + O(M * logN) - 시간 복잡도의 수식이 복잡할수록 안좋은함수
def is_available_to_order(menus, orders):
    # # 이분 탐색을 하기 전! 정렬 먼저
    # # 정렬의 시간 복잡도 : 배열의 길이를 N이라고 한다면 O(N * logN)
    # shop_menus.sort()
    # for order in orders: # O(M)  // O(M * logN)
    #     if not is_existing_target_number_binary(order, shop_menus): # O(logN)
    #         # 겹치는 메뉴가 없다
    #         return False
    # return True

    # 집합
    # O(M + N)
    menus_set = set(menus) # O(N)
    for order in orders: # M 번 반복 - 상수
        if order not in menus_set: # O(1)
            return False

    return True


# 이분 탐색 코드
def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    # // 나누기 두번하면 소수점 잘라서 가져옴
    current_guess = (current_min + current_max) // 2


    while current_min <= current_max:

        if array[current_guess] == target:

            return True
        # 이분하여 타겟이 여전히 크다면 up이기 때문에
        # 시도값보다 1이 큰 숫자로 최솟값을 변경하여야 한다.
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
