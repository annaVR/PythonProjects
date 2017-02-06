__author__ = 'anna'

class Node(object):

    def __init__(self, data=None, next_node=None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
       return str(self.data)

def print_list(head):
    if head is not None:
        print(head.data)
        next = head.next
        while next is not None:
            print(next.data)
            next = next.next

def Reverse(head):
    current = head
    new_head = head
    while current:
        prev = current.prev
        current.prev = current.next
        current.next = prev
        new_head = current
        current = current.prev
    return new_head



def main():
    node2 = Node(2)
    node4 = Node(4, node2)
    node6 = Node(6, node4)
    node4.prev = node6
    node2.prev = node4
    print_list(node6)
    print()
    print(Reverse(node6))
    print_list(node2)
    print("#2")
    node1, node3 = Node(1), Node(3)
    node1.next = node3
    node3.prev = node1
    print_list(node1)
    print(Reverse(node1))
    print_list(node3)

main()

