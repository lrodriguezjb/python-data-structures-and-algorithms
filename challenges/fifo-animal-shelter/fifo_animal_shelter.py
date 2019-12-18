class Node():
    """
    Class to create a new node.
    """
    def __init__(self, species, name):
        """
        Initialize an instance of node with species, name, and _next attributes.
        """
        self.species = species
        self.name = name
        self._next = None


class Queue():
    """
    Class to generate and modify a new Queue.
    """
    front = None
    rear = None

    def enqueue(self, species, name):
        """
        Method to add a new node at the *rear* of a queue and return the queue's new rear node.
        """
        new_node = Node(species, name)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear._next = new_node
            self.rear = new_node
        return self.rear

    def dequeue(self):
        """
        Method to remove a node from *front* of queue and return that node.
        """
        if self.front is not None:
            current = self.front
            self.front = self.front._next
            current._next = None
            return current
        else:
            return None

    def peek(self):
        """
        Method to return the front node of a queue.
        """
        if self.front is not None:
            return self.front
        else:
            return None


class Animal_shelter():
    """
    Class to instantiate an animal shelter that only takes cats or dogs.
    """
    def __init__(self):
        """
        Method to initialize the shelter with a cat queue and a dog queue.
        """
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, species, name):
        """
        Method to add a new cat or dog to their corresponding queue.
        """
        _species = str(species).lower()
        _name = str(name).lower()

        if _species == 'cat':
            return self.cats.enqueue(_species, _name)
        if _species == 'dog':
            return self.dogs.enqueue(_species, _name)
        return 'Sorry, we only accept cats or dogs.'

    def dequeue(self, pref):
        """
        Method to remove a cat or dog from their corresponding queue.
        """
        _pref = str(pref).lower()
        if _pref == 'cat':
            return self.cats.dequeue()
        if _pref == 'dog':
            return self.dogs.dequeue()
        return None