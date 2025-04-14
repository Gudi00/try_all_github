class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            print(self.items.pop())
        else:
            print("stack is empty")


top = Stack()
top.push(1)
top.push(3)
top.push(4)
top.push(5)
top.pop()
top.pop()
top.pop()
top.pop()
top.pop()

