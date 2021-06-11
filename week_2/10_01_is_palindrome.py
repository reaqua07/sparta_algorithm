input = "소주만병만주소"


# 회문 검사
def is_palindrome(string): # 소주만병만주소
    # # 문자열의 길이
    # n = len(string)
    # # i = 0~n-1까지 반복
    # for i in range(n):
    #     # 문자열의 맨앞 인덱스 0
    #     if string[i] != string[n - 1 - i]:
    #         return False
    #
    # return True

    # 한글자만 있을 경우에는 회문이라고 인식할 수 있기 때문에
    # 길이에 대한 제어는 항상 앞에서
    # 뒤에서 하면 에러가 날 수 있다
    if len(string) <= 1:  # 길이확인먼저 : 하지만 길이는 2 이상이니까 넘어감
        return True
    if string[0] != string[-1]:  # 첫번째 글자 소  / 마지막 글자 소 비교
        return False
    return is_palindrome(string[1:-1])
    # 첫번째 글자와 마지막 글자가 같았다면 string 에서 앞뒤 글자를 잘라서 다시 함수 실행


print(is_palindrome(input))
