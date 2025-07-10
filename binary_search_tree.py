class Node:
    """A node in a binary search tree."""

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """Insert a new key into the BST."""
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def inorder(root):
    """Inorder traversal of the BST."""
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


def search(root, key):
    """Search for a key in the BST."""
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


if __name__ == "__main__":
    # Example usage
    r = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    for key in keys:
        r = insert(r, key)

    print("Inorder traversal of the BST:")
    inorder(r)
    print()

    if search(r, 60):
        print("Found 60 in the tree")
    else:
        print("60 not found in the tree")
