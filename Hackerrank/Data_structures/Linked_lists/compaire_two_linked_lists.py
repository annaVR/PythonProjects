__author__ = 'anna'

class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
   def __str__(self):
       return str(self.data)

def CompareLists(headA, headB):
    while headA and headB is not None:
        if headA.data != headB.data and headA.next != headB.next: return 0
        else:
            headA = headA.next
            headB = headB.next
    return 1

def main():
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node_1, node_2, node_3, node_4 = Node(1), Node(2), Node(3), Node(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4


    print(CompareLists(node1, node_1))

main()

