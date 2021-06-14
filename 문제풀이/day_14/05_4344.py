# 입력값
num = int(input())

# 입력받은만큼 포문이 돌아야 하기 때문에 _
for _ in range(num):
    nums = list(map(int, input().split()))
    # 평균
    # nums[0] : 학생수 , nums[1:] : 점수
    average = sum(nums[1:]) / nums[0]
    count = 0
    for score in nums[1:]:
        # 평균 이상이면
        if score > average:
            # 평균 이상인 학생 수를 count
            count += 1
    # 전체 학생 중 몇 퍼센트인지 확인
    rate = count / nums[0] * 100
    print(f'{rate:.3f}%')
