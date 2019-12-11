class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return value

    def includes(self, value):
        if not self.head:
            return False
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def to_string(self):
        value = " "
        cur = self.head
        while cur.next != None:
            value += " " + str(cur.value)
            cur = cur.next
        value += " " + str(cur.value)
        print(value)
        return value

    def insert_before(self, existing_value, value):

        current = self.head
        if current.value == existing_value:
            new_node = Node(value)
            new_node.next = current
            self.head = new_node
            return True

        while current.next:
            if current.next.value == existing_value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next

    def insert_after(self, existing_value, value):
        current = self.head
        while current:
            if current.value == existing_value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return True

            current = current.next

    def append(self, value):
        if not self.head:
            self.insert(value)
            return
        else:
            current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def kth_from_end(self, k):
        value_list = []
        if self.head:
            current = self.head
            while current.next:
                value_list.append(current.value)
                current = current.next

            value_list.append(current.value)

        if 0 <= k < len(value_list):
            return value_list[-(k + 1)]
        else:
            return "K is out of range"


new_list = LinkedList()

new_list.insert(1)
new_list.insert(2)
new_list.insert(3)
new_list.insert_after(2, 4)
new_list.insert_before(2, 5)
new_list.insert_before(9, 7)
new_list.insert_after(9, 7)
new_list.to_string()
