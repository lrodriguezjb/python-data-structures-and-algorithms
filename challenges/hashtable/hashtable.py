class Hashtable:
    """
    Class to create and modify a hashtable.
    """
    def __init__(self):
        """
        Initializes a hashtable array with a linked list bucket in each of the 1024 indices.
        """
        bucket = LinkedList()
        self._array = [bucket] * 1024

    def add(self, key, value):
        """
        Adds a key-value pair to a hashtable.
        """
        index = self.hash(key)
        self._array[index].insert((key, value))

    def get(self, key):
        """
        Takes in a key and returns value of a key-value pair. If there are multiple matches for the key,
        return is a string of the values with each value separated by ' | '.
        """
        index = self.hash(key)
        matches_array = []
        if self._array[index].head:
            current = self._array[index].head
            while current:
                if current.data[0] == key:
                    matches_array.append(current.data[1])
                    current = current._next
                else:
                    current = current._next
        matches_string = ''
        while len(matches_array) > 1:
            for m in matches_array:
                matches_string += str(matches_array.pop()) + ' | '
        matches_string += str(matches_array.pop())

        return matches_string

    def contains(self, key):
        """
        Returns True if key is found in hashtable, False if not.
        """
        index = self.hash(key)
        if self._array[index].head:
            current = self._array[index].head
            while current:
                if current.data[0] == key:
                    return True
                else:
                    current = current._next
        return False

    def hash(self, key):
        """
        Takes in a key and hashes it to produce an array index between 0 and 1024.
        """
        index = int(str(key), 36) * 317 % 1024
        return index


class LinkedList():
    """
    Class to generate and modify linked list.
    """

    head = None

    def insert(self, new_data):
        """
        Method to create a node in the linked list with a .data value of *new_data* at the beginning of the list.
        """
        node = Node(new_data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head._next = current

    def includes(self, lookup):
        """
        Method to see if there is a node in the linked list with a .data value of *lookup*.
        """
        current = self.head
        try:
            while current._next:
                if current.data == lookup:
                    print('included!')
                    return True
                else:
                    current = current._next
            if current.data == lookup:
                print('included!')
                return True
        except:
            print('no ._next')

    def print(self):
        """
        Method to print a string containing the .data value in every node.
        """
        output = ''
        current = self.head
        while current:
            if current == self.head:
                output += current.data
            else:
                output += ', ' + current.data
            current = current._next
        return output

    def append(self, new_data):
        """
        Method to create a node in the linked list with a .data value of *new_data* at the end of the list.
        """
        node = Node(new_data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current._next:
                current = current._next
            current._next = node

    def add_before(self, lookup, new_data):
        """
        Method to create a node in the linked list with a .data value of *new_data* before the node with the .data
        value of *lookup* in the list.
        """
        node = Node(new_data)
        if self.includes(lookup):
            if self.head.data == lookup:
                self.insert(new_data)
            else:
                current = self.head
                while current._next.data != lookup:
                    current = current._next
                node._next = current._next
                current._next = node
        else:
            print('Lookup data not found in list.')

    def add_after(self, lookup, new_data):
        """
        Method to create a node in the linked list with a .data value of *new_data* after the node with the .data
        value of *lookup* in the list.
        """
        node = Node(new_data)
        if self.includes(lookup):
            current = self.head
            while current.data != lookup:
                current = current._next
            node._next = current._next
            current._next = node
        else:
            print('Lookup data not found in list.')

    def k_from_end(self, k):
        """
        Method to return the data of the kth node in a linked list.
        """
        total_nodes = 0
        position = 0
        current = self.head
        while current and current._next:
            total_nodes += 1
            current = current._next
        if current and not current._next:
            total_nodes += 1
        else:
            return 'Empty Linked List'
        if k < total_nodes:
            position = total_nodes - k
        else:
            return 'Exception'
        current = self.head
        for i in range(1, position):
            current = current._next
        return current.data


class Node():
    def __init__(self, data):
        """
        Initializes an instance of a node with a .data value equal to *data*.
        """
        self.data = data
        self._next = None


if __name__ == "__main__":
    ht = Hashtable()
    ht.add('potato', 'bagel')
    ht.add('soup', 'dumpling')
    ht.add('soup', 'pickles')

    print('get "soup": ', ht.get('soup'))

    print(ht.contains('soup'))