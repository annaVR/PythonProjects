__author__ = 'anna'
#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    if head is None:
        return None
    if not head.next:
        return head.data
    else:
        next = head.next
        length = 2
        while next.next:
            next = next.next
            length += 1
        node = head
        for i in range((length-1) - position):
            node = node.next
        return node.data
