__author__ = 'anna'

class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
   def __str__(self):
       return str(self.data)
#mine
def FindMergeNode(headA, headB):
    if headA.next.data == headB.next.data:
        return headA.next.data
    else:
        pnt_a = headA
        pnt_b = headB
        while pnt_a.next:
            pnt_a = pnt_a.next
            while pnt_b.next:
                if pnt_a.next == pnt_b.next:
                    return pnt_a.next.data
                else:
                    pnt_b = pnt_b.next
# the bes
def FindMergeNode_best(headA, headB):
    pnt_a = headA
    pnt_b = headB
    while pnt_a and pnt_b:
        if pnt_a == pnt_b:
            return pnt_a.data
        pnt_a = pnt_a.next
        pnt_b = pnt_b.next
        if pnt_a is None:
            pnt_a = headB
        elif pnt_b is None:
            pnt_b = headA



def print_list(head):
    if head is not None:
        print(head.data)
        next = head.next
        while next is not None:
            print(next.data)
            next = next.next


def main():
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node_a, node_b = Node(5), Node(6)
    node_a.next = node_b
    node_b.next = node3
    print_list(node1)
    print()
    print_list(node_a)
    print()
    print(FindMergeNode(node1, node_a))

main()

