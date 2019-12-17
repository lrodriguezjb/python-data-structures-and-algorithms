from stack_and_node_classes import Stack, Node


class PseudoQueue:
    def __init__(self, stack_a):
        self.stack_a = stack_a
        self.stack_b = Stack()

    def enqueue(self, value):
        new_node = Node(value)
        new_node.next = self.stack_a.top
        self.stack_a.top = new_node

    def dequeue(self):
        while self.stack_a.top:
            value = self.stack_a.pop()
            # new_node = Node(value)
            self.stack_b.push(value)
        result = self.stack_b.pop()
        while self.stack_b.top:
            value = self.stack_b.pop()
            # new_node = Node(value)
            self.stack_a.push(value)
        return result


if __name__ == "__main__":
    stack_a = Stack()
    stack_a.push(20)
    stack_a.push(15)
    stack_a.push(10)
    queue = PsudoQueue(stack_a)
    a = queue.dequeue()
    print(a.value)
