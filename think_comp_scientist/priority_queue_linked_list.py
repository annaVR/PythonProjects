__author__ = 'anna'

import random


class Node(object):
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class LinkedPriorityQueue(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            self.head = node
        elif node.cargo > self.head.cargo:
                node.next = self.head
                self.head = node
        else:
            current = self.head
            while current.next is not None:
                if current.cargo >= node.cargo >= current.next.cargo:
                    next = current.next
                    current.next = node
                    node.next = next
                    break
                current = current.next
            if current.cargo >= node.cargo and current.next is None:
                current.next = node
        print(node)
        self.length += 1

    def remove(self):
        maxi = self.head.cargo
        next = self.head.next
        self.head = next
        self.length -= 1
        return maxi

pq = LinkedPriorityQueue()
for i in range(0, 15):
    pq.insert(random.randrange(0, 100))

# pq.insert(10)
# print('head:', pq.head)
# pq.insert(12)
# print('head:', pq.head, 'head.next:', pq.head.next)
# pq.insert(14)
# print('head:', pq.head, 'head.next:', pq.head.next, 'head.next.next:', pq.head.next.next)
# pq.insert(5)
# print('head:', pq.head, 'head.next:', pq.head.next, 'head.next.next:', pq.head.next.next,
#       'head.next.next.next', pq.head.next.next.next)
# pq.insert(6)
# pq.insert(16)
# pq.insert(1)
print('Dequeue items:')
while not pq.length == 0:
    print(pq.remove())
