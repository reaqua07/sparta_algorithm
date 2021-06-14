input_num = int(input())

# 이후 변화할 값을 저장하는 변수 지정
num = input_num
count = 0

while True:     # 몫
    sum_num = (num // 10) + (num % 10)
                                # 합한 값의 가장 오른쪽(나머지)
    new_num = ((num % 10) * 10) + (sum_num % 10)
    count += 1

    if new_num == input_num:
        break

    num = new_num

print(count)
