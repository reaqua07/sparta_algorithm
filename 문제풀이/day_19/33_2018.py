from sys import stdin
from collections import Counter

N = int(stdin.readline())

# 인덱스 주려고
nums = []

# 입력값 하나씩 담아줌
for _ in range(N):
    nums.append(int(stdin.readline()))

# mean
print(round(sum(nums) / len(nums)))

# mid
nums.sort()
            # 몫
print(nums[N // 2])

# 최빈값 - 딕{문자 : 개수}
count_nums = Counter(nums).most_common()
# 최빈값이 두가지인 경우
if len(count_nums) > 1 and count_nums[0][1] == count_nums[1][1]:
    # 두번째로 작은 값 : 앞에서 오름차순으로 정리됨
    print(count_nums[1][0])
else:
    print(count_nums[0][0])

# 범위 : 최대 - 최소
print(max(nums) - min(nums))