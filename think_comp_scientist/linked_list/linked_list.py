# "Node" class

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

node = Node("test")
print(node)

node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
print(node1, node2, node3, node4)

node1.next = node2
node2.next = node3
node3.next = node4


def print_list(node):
    print('[', end="")
    while node is not None:
        if node.next is None:
            print(node.cargo, end="")
        else:
            print(node.cargo, end=", ")
        node = node.next

    print(']')
print("Exercise 24.12:")
print_list(node1)
print()
print_list(node2)
print()

def print_backward(list):

    if list is None: return
    head = list #think of "head" as a reference to a single node,
    # and think of "list" as a reference to the first node of a list. It is only in programmer's mind
    tail = list.next
    print_backward(tail)
    print(head, end=" ")

print("backward:")
print_backward(node1)
print()
print_backward(node2)

def remove_second(list):
    if list is None:
        print("You have passed in an empty list. Cannot perform deletion of a second element.")
        return
    elif list.next is None:
        print("There is only one element in a list. Cannot perform deletion of a second element.")
        return
    first = list
    second = list.next
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second

print()
print('#1')
print_list(node1)
print()
removed = remove_second(node1)
print(removed)
print_list(node1)

print()
print('#2')
print_list(node1)
print()
removed2 = remove_second(node1)
print(removed2)
print_list(node1)
print()
print('#3')
removed3 = remove_second(node1)
print(removed3)

print_list(node1)
print()
print('#4')
remove_second(node1)
print(node1)

print()
print('#5')
remove_second(None)




