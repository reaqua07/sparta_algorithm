# 숫자 입력
a = int(input())
# index 를 사용해서 위치 정보를 주기 위해 문자열로 둔다
b = input()

print(
    a * int(b[2]),
    a * int(b[1]),
    a * int(b[0]),
    a * int(b)
)
