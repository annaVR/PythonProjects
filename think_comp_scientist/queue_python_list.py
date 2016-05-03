__author__ = 'anna'

class QueuePythonList(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)

ql = QueuePythonList()
# for num in range(0, 11):
#     ql.insert(num)
# print("Dequeueing items:")
# while not ql.is_empty():
#     print(ql.remove())
# print(ql.is_empty())
#
# l = list('Masha')
# for item in l:
#     ql.insert(item)
# print("Dequeueing items:")
# while not ql.is_empty():
#     print(ql.remove())

for num in range(15):
    ql.insert(num)
while not ql.is_empty():
    print(ql.remove())


