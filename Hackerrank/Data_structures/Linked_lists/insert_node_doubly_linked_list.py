__author__ = 'anna'

class Node(object):

    def __init__(self, data=None, next_node=None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
       return str(self.data)

def print_list(head):
    if head is not None:
        print(head.data)
        next = head.next
        while next is not None:
            print(next.data)
            next = next.next

def SortedInsert(head, data):
    if head is None:
        head = Node(data, None, None)
        return head
    elif head.next is None:
        if data < head.data:
            next = head
            head = Node(data, next, None)
            next.prev = head
        else:
            head.next = Node(data, None, head)
        return head
    elif head.next:
        current = head
        next = head.next
        while next:
            if current.data < data < next.data:
                new_node = Node(data, next, current)
                current.next = new_node
                next.prev = new_node
                break
            elif next.next is None and next.data < data:
                new_node = Node(data, None, next)
                next.next = new_node
            else:
                next = next.next
                current = current.next
        return head



def main():
    head = SortedInsert(None, 2)
    head = SortedInsert(head, 1)
    head = SortedInsert(head, 4)
    head = SortedInsert(head, 3)
    print()
    print_list(head)

main()
