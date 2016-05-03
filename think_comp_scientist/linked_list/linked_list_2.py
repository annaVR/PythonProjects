class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def __str__(self):
        print('[', end="")
        return str(self.head.print_forward())

    def print_backward(self):
        print('[', end=" ")
        if self.head is not None:
            self.head.print_backward()
            print(']')

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

class Node(object):
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
            print(self.cargo, end=" ")
        elif self.next is None:
            print(self.cargo)

    def print_forward(self):

        if self.next is not None:
            print(self.cargo, end=" ")
            next = self.next
            next.print_forward()
        elif self.next is None:
            print(self.cargo)

l = LinkedList()
node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

print(node4)
print(node4.next)
l.head = node1
print('Printing the list backward:')
l.print_backward()
print('Printing the list forward:')
print(l)
print('Printing node1:')
node1.print_forward()
node2.print_forward()