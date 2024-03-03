class Stack:
    def __init__(self):
        self.items = []

    def empty_stack(self):
        return len(self.items) == 0

    def push_stack(self, item):
        self.items.append(item)

    def pop_stack(self):
        if not self.empty_stack():
            return self.items.pop()

        else:
            print("Stack is empty!")

    def peek_stack(self):
        if not self.empty_stack():
            return self.items[-1]
        else:
            print("Stack is empty!")

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.empty_stack())
stack.push_stack(23)
stack.push_stack(2)
stack.push_stack(16)
stack.push_stack(19)
#print(stack.items[-1::-1])

#print(stack.pop_stack())
#print(stack.items)

print(stack.peek_stack())