class Golfer(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '{0:20}: {1}'.format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score

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

tiger = Golfer('Tiger Woods', 50)
phil = Golfer('Phil Mickelson', 75)
hal = Golfer('Hal Sutton', 65)

pq = PriorityQueue()
for golfer in [tiger, phil, hal]:
    pq.insert(golfer)

while not pq.is_empty():
    print(pq.remove())