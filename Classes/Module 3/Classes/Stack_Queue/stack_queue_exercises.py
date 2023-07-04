class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

'''Stack Reversal  

Write a function that takes a stack as input and returns a new stack with the items reversed. The original stack should remain unchanged. 

 '''

def reverse_stack(stack):
    new_stack = Stack()
    while not stack.is_empty():
        new_stack.push(stack.pop())
    return new_stack

def reverse_queue(queue):
    new_queue = Queue()
    while not queue.is_empty():
        new_queue.enqueue(queue.dequeue())
    return new_queue

def bracket_match(string):
    stack = Stack()
    open_brackets= ['(','[','{']
    close_brackets= [')',']','}']

    for char in string:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if stack.is_empty():
                return False
            if open_brackets.index(stack.peek())== close_brackets.index(char):
                stack.pop()
            else:
                return False
    return stack.is_empty()


class BrowserHistory:
    def __init__(self):
        self.history = []

    def visit(self, url):
        self.history.append(url)

    def go_back(self):
        if self.history:
            return self.history.pop()
        else:
            return None

class SupermarketCheckout:
    def __init__(self):
        self.queue = []

    def join_queue(self, customer):
        self.queue.append(customer)

    def serve_customer(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None
    


# Testing Stack Implementation
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.is_empty())  # Output: False

# Testing Queue Implementation
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2
print(queue.is_empty())  # Output: False

print(bracket_match("({})[]"))
print(bracket_match("({)[]"))