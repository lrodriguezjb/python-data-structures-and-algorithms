class Node:
    """Instantiation of a node class"""

    def __init__(self, value):
        self.value = value
        """Setting left and right values"""
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, node=None, arr=[]):
        node = node or self.root

        arr.append(node.value)

        if node.left:
            self.pre_order(node.left, arr)
        if node.right:
            self.pre_order(node.right, arr)
        return arr

    def in_order(self, node=None, arr=[]):
        node = node or self.root
        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.in_order(node.right, arr)
        return arr

    def post_order(self, node=None, arr=[]):
        node = node or self.root
        if node.left:
            self.post_order(node.left, arr)
        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)

        return arr


class BinarySearchTree(BinaryTree):
    def add(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return value
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = node
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    return
                current = current.right
