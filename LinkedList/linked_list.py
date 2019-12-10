class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = Node()

    def insert(self, desired_location):
        new_node = Node(desired_location)
        new_node.next = self.head
        self.head = new_node
        return desired_location

    def includes(self, data):
        if not self.head:
            return False
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def to_list(self):
        value = " "
        cur = self.head
        while cur.next != None:
            value += " " + str(cur.data)
            cur = cur.next
        print(value)
        return value

    def append(self, val):
        current = self.head
        while current:
            if current.next == None:
                current.next = Node(val)
                return self.__str__()
            else:
                current = current.next
                self.head = Node(val)
                return self.__str__()

    def insert_before(self, value, new_val):
        if self.includes(value):
            new_node = Node(new_val)
            current = self.head
            while current.next:
                if current.next.value == value:
                    new_node = current.next
                    current.next = new_node.next
                    return self.__str__()
                else:
                    current = current.next
                    return self.__str__()

    def insert_after(self, existing, val):
        if self.includes(existing):
            current = self.head
            while current:
                if current.val == existing:
                    new_node = current.next
                    new_node.next = current.next
                    return self.__str__()
                else:
                    current = current.next
                    return self.__str__()
