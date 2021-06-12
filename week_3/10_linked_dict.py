# 해쉬는 임의의 값을 발급해주지만 간혹 같은 값을 반환하기도 함
# 이를 충돌이라고 함
# 해결책 1. 링크드 리스트 : 노드로 이어줘서 충돌이 일어나도 그 다음 데이터로 받아버리게 처리
#                        키 값을 함께 저장해서 나중에 데이터 찾을 때 유용하게 하자
# 이러한 해결 방식을 체이닝이라고 함
class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append(key, value)

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # []
        # [(key,value)]
        self.items[index].add(key, value)
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # [(key1, value1),(key,value)]
        return self.items[index].get(key)
