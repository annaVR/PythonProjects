__author__ = 'anna'

"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
class Node(object):

    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
    def __str__(self):
       return str(self.data)

def print_list(head):
    while head.next is not None:
        print(head.data)
        head = head.next
    print(head)

def Reverse_iterational(head):
    current = head
    previous = None
    while current is not None:
        next = current.next
        current.next = previous
        print('current.next:', current.next)
        previous = current
        current = next
    print(previous)
# def Reverse_recursive(head):
#     if head is None:
#         return None
#     elif
#     else:
#         Reverse_recursive(head.next)






def main():
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

def main_2():
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node5, node6, node7 = Node(5), Node(6), Node(7)
    node5.next = node6
    node6.next = node7


    Reverse_iterational(node1)
    print()
    print_list(node4)
    print()
    Reverse_iterational(node5)
    print()
    print_list(node7)
    print()
main_2()





