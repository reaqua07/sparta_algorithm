top_heights = [6, 9, 5, 7, 4]


# 탑: 수신하는 탑의 순서 / 오른쪽에서 왼쪽으로 레이저 슝슝
# 배열의 초기 값은 0 으로 시작하자
# 맨 뒤의 값이 왼쪽에 있는 값들과 비교된다.
# 비교하여 왼쪽 값이 더 클 경우 그 위치 값을 1,2,3,4-
# 배열에 실행시킨 값의 위치에 저장한다.
# 예 ) 다섯번째 값이 두번째 값에 부딪히면 5가 두번째 자리에 저장됨
# 비교된 왼쪽 값은 없애버린다
# 맨뒤 자료가 없어진다?? 스택을 활용하자

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)  # 배열 초기값
    # heights가 빈 상태가 아닐때까지 돌아라
    while heights:
        # 맨 뒤 자료 뽑기
        height = heights.pop()
        # heights의 현재 길이만큼 돌아라 : 점점 줄어든다
        for idx in range(len(heights) - 1, 0, -1):
            # 레이저가 닿는 순간
            if heights[idx] > height:
                # 위치값을 저장해야 하기 때문에 인덱스 값에 +1 한다
                # 저장 위치는 현재의 길이 위치 값을 넣으면 된다
                answer[len(heights)] = idx + 1
                break

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
