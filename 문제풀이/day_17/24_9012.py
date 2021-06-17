T = int(input())

for i in range(T):
    V = list(input())

    # V에 포함된 괄호가 0이 되기 전까지 반복해야 하니까 while
    while len(V) != 0:
        if V[0] == ')':
            print('1=NO')
            break
        # ( 로 시작할때
        else:
            # ) 가 포함되어 있다면
            # 한 세트를 지워야 하기 때문에
            if ')' in V:
                # 닫는 괄호 먼저 지우고
                V.remove(')')
                # 여는 괄호를 지운다
                V.remove('(')
            # 닫는 괄호가 안나온다면?
            else:
                print('2=NO')
                break
    # v 에 아무것도 남지 않았을때 - 세트가 맞는 것
    if len(V) == 0:
        print('3=YES')



