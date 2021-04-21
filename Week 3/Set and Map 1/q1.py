import random


class Map(object):
    def __init__(self):
        self.set = set()

    def insert(self, val):
        self.set.add(val)

    def delete(self, val):
        self.set.discard(val)

    def find(self, val):
        return val in self.set

    def getRandom(self):
        return random.choice(list(self.set))

    def __str__(self) -> str:
        return str(list(self.set))


map = Map()
map.insert(5)
print(map)
map.insert(6)
print(map)
map.insert(100)
print(map)
map.delete(100)
print(map)
map.find(100)
print(map.getRandom())
