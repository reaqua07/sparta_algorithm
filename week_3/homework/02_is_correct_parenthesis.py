input = "(())()"
# 1. ( 괄호가 열림
# 2. ( 괄호 또 열림
# 3. ) 괄호가 닫힘, 현재까지 열린 괄호 중 현재 열린 괄호 하나
# 4. ) 괄호가 또 닫힘, 현재 열린 괄호 없음
# 5. ( 괄호가 열림
# 6. ) 괄호가 닫힘, 현재 열린 괄호 없음


def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            # 어떤 값이 들어가도 상관없다
            # ( 가 들어가 있는지만 확인하면 됨
            stack.append(i)
        elif string[i] == ")":
            # 닫는 괄호는 앞에 무조건 열린 괄호가 있어야 하기 때문에
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    # stack 에 남아 있는 자료가 없다면 트루 반환
    if len(stack) == 0:
        return True
    else:
        return False
    return


print(is_correct_parenthesis(input))  # True 를 반환해야 합니다!