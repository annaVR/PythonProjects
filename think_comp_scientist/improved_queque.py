class Node(object):
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class ImprovedQueue(object):
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

new_queue = ImprovedQueue()
# new_queue.insert("a")
# new_queue.insert("b")
# new_queue.insert('c')
# new_queue.insert('d')
#
# print(new_queue.is_empty())
# print(new_queue.length)
#
# print(new_queue.remove())
# print(new_queue.length)
# print()
# print(new_queue.remove())
# print(new_queue.length)
#
# while not new_queue.is_empty():
#     print(new_queue.remove())

for num in range(15):
    new_queue.insert(num)

while not new_queue.is_empty():
    print(new_queue.remove())

