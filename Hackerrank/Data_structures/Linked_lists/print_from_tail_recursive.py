__author__ = 'anna'
"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)

def ReversePrint(head):
    if head is None:
        return None
    else:
        next = head.next
        if next is not None:
            ReversePrint(next)
        print(head.data)

def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=" ")


node1, node2, node3 = Node(1), Node(2), Node(3)
node1.next = node2
node2.next = node3
ReversePrint(node1)
