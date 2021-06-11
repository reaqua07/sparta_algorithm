def count_down(number):
    # 재귀함수는 탈출 조건을 달아줘야한다.
    # 탈출 조건이 없을 경우 무한 로딩
    if number < 0:
        return
    print(number)  # number를 출력하고
    count_down(number - 1)  # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)
