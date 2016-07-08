__author__ = 'anna'

class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
   def __str__(self):
       return str(self.data)


def RemoveDuplicates(head):
    if head is None:
        return None
    elif not head.next:
        return head

    elif head.data == head.next.data:
        next = head.next
        while head.data == next.data:
            head.next = next.next
            next = next.next
            if next is None:
                return head
    else:
        next = head.next
    while next.next.next:
        after_next = next.next
        if next.data == after_next.data:
            next.next = after_next.next
            after_next = after_next.next
        else:
            next = after_next
            after_next = next.next
    return head

def print_list(head):
    if head is not None:
        print(head.data)
        next = head.next
        while next is not None:
            print(next.data)
            next = next.next


def main():
    node1, node2, node_2, node3, node_3, node4 = Node(1), Node(2), Node(2), Node(3), Node(3), Node(4)
    node1.next = node2
    node2.next = node_2
    node_2.next = node3
    node3.next = node_3
    node_3.next = node4
    print_list(node1)
    print()
    print(RemoveDuplicates(node1))
    print('After:')
    print_list(node1)
    print()
    nodea, nodeb, nodec, noded = Node(1), Node(1), Node(1), Node(1)
    nodea.next = nodeb
    nodeb.next = nodec
    nodec.next = noded
    print_list(nodea)
    print()
    print(RemoveDuplicates(nodea))
    print('After:')
    print_list(nodea)




main()

