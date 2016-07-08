"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""

#from hackerrank
def insert_recursive(head, data):
    if head is None:
        return Node(data, None)
    else:
        if head.next is None:
            head.next = Node(data, None)
        else:
            insert_recursive(head.next, data)
        return head

#mine
def insert_non_recursive(head, data):
    if head is None:
        return Node(data, None)
    else:
        if head.next is None:
            head.next = Node(data, None)
        else:
            next = head.next
            while next.next is not None:
                next = next.next
            next.next = Node(data, None)
        return head





