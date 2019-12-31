class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = _Node(value)
        if not self.root:
            self.root = node
        else:
            current = self.root
            q = Queue()
            q.enqueue(current)
            while not q.is_empty():
                current = q.dequeue()
                if not current.left:
                    current.left = node
                    return
                else:
                    q.enqueue(current.left)
                if not current.right:
                    current.right = node
                    return
                else:
                    q.enqueue(current.right)

    def breadth_first(self):
        if not self.root:
            return None
        q, new_list = Queue(), []

        q.enqueue(self.root)
        while not q.is_empty():
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
            new_list.append(current.value)
        return new_list


class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.front = None
        self.end = None

    def enqueue(self, value):
        if isinstance(value, _Node):
            node = value
        else:
            node = _Node(value)

        if not self.front:
            self.front = node
            self.end = node
            return

        if self.end:
            self.end.next = node
            self.end = node

    def dequeue(self):
        if not self.front:
            return None
        node = self.front
        self.front = node.next
        return node

    def is_empty(self):
        if not self.front:
            return True
        return False
