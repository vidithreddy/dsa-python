class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return not self.items

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack."""
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


class Queue:
    """A simple queue implementation using a Python list."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.items

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.insert(0, item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        return self.items.pop()

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


if __name__ == '__main__':
    # Example usage
    print("Stack demo:")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("Popped:", s.pop())
    print("Top item:", s.peek())
    print("Stack size:", s.size())

    print("\nQueue demo:")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Dequeued:", q.dequeue())
    print("Queue size:", q.size())
