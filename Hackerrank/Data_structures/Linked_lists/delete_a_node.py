__author__ = 'anna'
"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Delete(head, position):
    if position == 0:
        head = head.next
    elif position > 0:
        current = head
        next = head.next
        after_next = next.next
        for i in range(position - 1):
            current = next
            next = next.next
            after_next = next.next
        current.next = after_next
    return head
