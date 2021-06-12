# 해쉬는 임의의 값을 발급해주지만 간혹 같은 값을 반환하기도 함
# 이를 충돌이라고 함
# 해결책 1. 링크드 리스트 : 노드로 이어줘서 충돌이 일어나도 그 다음 데이터로 받아버리게 처리
#                        키 값을 함께 저장해서 나중에 데이터 찾을 때 유용하게 하자
class Dict:
    def __init__(self):
        self.items = [None] * 8

    # 딕셔너리에 새로운 키와 데이터를 넣는다.
    def put(self, key, value):
        # key 값을 임의의 값으로 받아서 / 딕셔너리의 최대값으로 나눈다.
        index = hash(key) % len(self.items)
        # index는 1에서 7사이의 값이 될 것이다.
        self.items[index] = value

    # 딕셔너리에서 키값으로 데이터를 찾아올때때
    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
