import sys

N = int(sys.stdin.readline())

stack = []
result_list = []

current_num = 1
flag = True

for i in range(N):
    input_num = int(sys.stdin.readline())
    # 입력값을 포함한 stack 먼저 만들기
    while input_num >= current_num:
        stack.append(current_num)
        result_list.append("+")
        current_num += 1
    # while에서 만들어진 stack의 top의 숫자와 입력 숫자 비교
    # 같으면 pop 하고 - 추가
    if stack[-1] == input_num:
        stack.pop()
        result_list.append('-')
    # 다르면 뺄 수가 없으니 no 프린트
    else:
        print('NO')
        flag = False
        break

if flag is True:
    for i in result_list:
        print(i)
