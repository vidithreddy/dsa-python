class Node:
    """A node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A simple implementation of a singly linked list."""

    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first occurrence of key in the list."""
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                return

        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    def print_list(self):
        """Print all elements in the list."""
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # Example usage
    llist = LinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    print("Initial list:")
    llist.print_list()

    llist.delete(2)
    print("After deleting 2:")
    llist.print_list()
