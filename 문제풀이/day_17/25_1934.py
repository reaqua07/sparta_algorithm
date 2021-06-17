# 유클리드 호제법
# 큰수를 작은수로 0이 될때까지 나누면 그때의 큰수가 최대공약수

T = int(input())


# 최대공약수
def gcd(A, B):
    # 큰수 작은수 위치 잡기
    if B > A:
        A, B = B, A
    # 작은수가 0이 되기 전까지
    while B != 0:
        A, B = B, A % B
    # 작은수가 0이 되면
    return A

# 최소공배수
def lcm(A, B):
    return (A * B) // gcd(A, B)


for i in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))
