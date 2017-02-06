# stacks implementation through Python lists

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

s = Stack()


while not s.is_empty():
    print(s.pop(), end = ', ')
print()


def eval_postfix(expr):
    import re
    token_list = re.split('([^0-9])', expr)
    stack = Stack()
    for token in token_list:
        if token == '' or token == " ":
            continue
        if token == "+":
            summ = stack.pop() + stack.pop()
            stack.push(summ)
        elif token == '-':
            difference = int()
            subtrahend = stack.pop()
            minuend = stack.pop()
            difference = minuend - subtrahend
            stack.push(difference)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        elif token == '/':
            quotient = int()
            divisor = stack.pop()
            divident = stack.pop()
            quotient = divident // divisor
            stack.push(quotient)
        else:
            stack.push(int(token))
    return stack.pop()

print(eval_postfix("2   5 + 4 *"))
print(eval_postfix("56 47 + 2 *"))
print(eval_postfix('101  2 - 3/'))
print(eval_postfix('2 3 * 1 +'))

