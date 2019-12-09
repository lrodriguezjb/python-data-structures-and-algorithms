class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return data

    def includes(self, data):
        if not self.head:
            return False
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def to_string(self):
        value = " "
        cur = self.head
        while cur.next != None:
            value += " " + str(cur.data)
            cur = cur.next
        print(value)
        return value


my_list = linked_list()
my_list.insert("HELLO")
my_list.includes("HELLO")
my_list.to_string()
