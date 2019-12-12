class Node:

        def __init__(self, value, next_node=None):
            self.value = str(value)
            self.next_node = next_node

        def __repr__(self):
            return self.value


class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return

    def __str__(self):
        values = self.return_list()
        return f"The values is {values}. A total of {len(values)}."

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return value

    def return_list(self):
        current = self.head
        collection_of_values = ''
        while current:
            collection_of_values += current.value
            current = current.next_node
        return collection_of_values


def mergeLists(list1, list2):
    new_ll = LinkedList(list1.head)
    pointer_one = list1.head
    pointer_two = list2.head

    while pointer_one and pointer_two:
        one_next = pointer_one.next
        two_next = pointer_two.next

        pointer_one.next = pointer_two
        if one_next == None:
            break
        pointer_two.next = one_next

        pointer_one = one_next
        pointer_two = two_next

    return new_ll
