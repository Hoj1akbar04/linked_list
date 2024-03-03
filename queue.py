from collections import deque


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def empty_queue(self):
        return len(self.items) == 0

    def dequeue_queue(self):
        if not self.empty_queue():
            return self.items.pop(0)

        else:
            print("Queue is empty!")

    def peek_queue(self):
        if not self.empty_queue():
            return self.items[0]

        else:
            print("Queue is empty!")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


queue = Queue()
print(queue)
print(queue.empty_queue())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue)
print("size of the queue: ", queue.size())
print("most item in the queue:", queue.peek_queue())

front_item = queue.dequeue_queue()
print("Deque: ", front_item)
print(queue)




