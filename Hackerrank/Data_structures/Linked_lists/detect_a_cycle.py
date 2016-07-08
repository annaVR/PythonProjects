__author__ = 'anna'
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head is None:
        return False
    elif head.next is None:
        return False
    else:
        pnt_1 = head
        pnt_2 = head.next
        while pnt_1 and pnt_2:
            pnt_1 = pnt_1.next
            pnt_2 = pnt_1.next.next
            if pnt_1.data == pnt_2.data:
                return True
        return False
