__author__ = 'anna'

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)



def MergeLists(headA, headB):
    if headA is None:
        return headB
    elif headB is None:
        return headA
    else:
        if headA.data < headB.data:
            head = headA
            nextA = headA.next
            nextB = headB
        elif headB.data < headA.data:
            head = headB
            nextA = headA
            nextB = headB.next
        print('head:', head)
        current = head
        while nextA and nextB:
            if nextA.data < nextB.data:
                current.next = nextA
                nextA = nextA.next
                current = current.next
            elif nextB.data < nextA.data:
                current.next = nextB
                nextB = nextB.next
                current = current.next
            if head.next is None:
                head.next = current
        while nextA:
            if current is None:
                head.next = nextA
            else:
                current.next = nextA
                nextA = nextA.next
                current = current.next
        while nextB:
            if current is None:
                head.next = nextB
            else:
                current.next = nextB
                nextB = nextB.next
                current = current.next
    return head

def merge_list_recursive(heada, headb):
    if heada is None:
        return headb
    if headb is None:
        return heada
    if heada.data < headb.data:
        smaller_node = heada
        smaller_node.next = merge_list_recursive(heada.next, headb)
    else:
        smaller_node = headb
        smaller_node.next = merge_list_recursive(heada, headb.next)
    return smaller_node

def print_list(head):
    if head is not None:
        print(head.data)
        next = head.next
        while next is not None:
            print(next.data)
            next = next.next


node1, node3, node5, node6 = Node(1), Node(3), Node(5), Node(6)
node1.next = node3
node3.next = node5
node5.next = node6

node2, node4, node7 = Node(2), Node(4), Node(7)
node2.next = node4
node4.next = node7

print('Before:')
print_list(node1)
print()
print_list(node2)
print('The merge:')
print(merge_list_recursive(node1, node2))
print('After the merge:')
print_list(node1)
print()
print_list(node2)

node12 = Node(12)
node15 = Node(15)
print(MergeLists(node12, node15))

node_none = Node()
node_1, node_2 = Node(1), Node(2)
node_1.next = node_2
print(MergeLists(None, node_1))
print(MergeLists(None, None))

