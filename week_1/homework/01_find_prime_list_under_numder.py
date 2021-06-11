input = 20

# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는
# 반드시 N의 제곱근 이하
def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1): # n의 범위 : 2부터 number까지
        # n 이 20 이라고 했을 때
        # i 를 2 3 5 (7 13 17 19)
        # 2 ~ n - 1 중에서 소수인 친구들만 
        
        for i in prime_list: # i의 범위 : 2부터 n-1 까지
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)