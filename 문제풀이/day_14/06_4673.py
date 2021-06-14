number_set = set(range(1, 10000))

# 생성자
removed_set = set()

for num in number_set:
    for i in str(num):
        # 자기자신 + 자릿수별 값 더하기
        num += int(i)
    removed_set.add(num)

self_number_set = number_set - removed_set
# print(self_number_set)
                # 정렬
for self_num in sorted(self_number_set):
    print(self_num)
