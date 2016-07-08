__author__ = 'anna'
"""
 Insert Node at the end of a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if head is None:
        return Node(data, None)
    else:
        if position == 0:
            next = head
            head = Node(data, None)
            head.next = next
        elif position > 0:
            current = head
            next = head.next
            for i in range(position - 1):
                current = next
                next = next.next
            new_node = Node(data, None)
            current.next = new_node
            new_node.next = next
        return head
