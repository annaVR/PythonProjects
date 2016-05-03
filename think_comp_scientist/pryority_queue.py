import random


class PriorityQueue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items [maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

q = PriorityQueue()
for i in range(0, 15):
    q.insert(random.randrange(0, 100))
while not q.is_empty():
    print(q.remove())
