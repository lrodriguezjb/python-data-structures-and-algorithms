class Node:
    """
    An instance of a node
    Has a value and a pointer to the next node
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

class Stack:
    """
    An instance of a Stack
    Has a top property that points to the top Node
    push method adds a Node to the top of the stack
    pop method removes a Node from the top of the stack, returns its value
    peek method returns the value of the top node in the stack
    is_empty method returns True or False if the stack is empty
    """        
    def __init__(self, top=None):
        self.top = top

    def __repr__(self):
        return 'This is an instance of a Stack'

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        try:
            top_node = self.top
            self.top = top_node.next
            top_node.next = None
            return top_node.value
        except AttributeError:
            return None
    
    def peek(self):
        try:
            return self.top.value
        except AttributeError:
            return None

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False