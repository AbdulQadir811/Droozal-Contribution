class Stack(object):

    def __init__(self):
        self.storage = []

    def push(self, item):
        self.storage.append(item)
        return item

    def pop(self):
        if self.storage:
            return self.storage.pop()
        else:
            return None

    def peek(self):
        return self.storage[-1]


class Queue(Stack):

    def pop(self):
        if self.storage:
            return self.storage.pop(0)
        else:
            return None

stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
stack.pop()
stack.pop()

queue = Queue()
print queue.pop()
super(Queue, queue).push(1)
print super(Queue, queue).peek()
