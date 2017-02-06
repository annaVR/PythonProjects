"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        return str(self.head)

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        if self.head:
            second = self.head
            self.head = new_element
            self.head.next = second
        else:
            self.head = new_element

    def delete_first(self):
        if self.head:
            to_delete = self.head
            self.head = self.head.next
            return to_delete


    def print_linked_list(self):
        if self.head:
            current = self.head
            print(current.value)
            while current.next:
                current = current.next
                print(current.value)

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)
    def __str__(self):
        return str(self.ll)

    def push(self, new_element):
        if self.ll:
            self.ll.insert_first(new_element)

    def pop(self):
        if self.ll:
            return self.ll.delete_first()
    def print(self):
        if self.ll:
            return self.ll.print_linked_list()

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
stack.print()
print()
print(stack.pop().value)
print(stack.pop().value)

print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)