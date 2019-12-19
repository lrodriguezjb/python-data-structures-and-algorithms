class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)
        return self.top

    def pop(self):
        if self.top.value != None:
            place_holder = self.top.value
            self.top = self.top.next
            return place_holder
        else:
            raise ValueError('This is an empty stack!')

    def peek(self):
        top = self.top
        if not top:
            return None
        else:
            return top.value


class MultiBracketValidation():
    def __init__(self):
        self.validity = Stack()

    def multibracket_validation(self, str):
        open = ['[', '{', '(']

        for i in str:
            if i in open:
                self.validity.push(i)

            if i == ')':
                if self.validity:
                    if self.validity.peek() == '(':
                        self.validity.pop()
                    else:
                        return False

            if i == '}':
                if self.validity.top:
                    if self.validity.peek() == '{':
                        self.validity.pop()
                    else:
                        return False
                else:
                    return False

            if i == ']':
                if self.validity.top:
                    if self.validity.peek() == '[':
                        self.validity.pop()
                    else:
                        return False

        if self.validity.peek():
            return False
        else:
            return True


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
