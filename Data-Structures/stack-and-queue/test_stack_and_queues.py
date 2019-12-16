from stack_and_queues import Node, Stack, Queue


def test_Node():
    '''Checking if a Node can be created'''
    node = Node('Hi')
    expected = Node
    assert type(node) == expected


def test_push_one():
    '''Can successfully push onto a stack'''
    stack = Stack()
    stack.push('Hola')
    expected = 'Hola'
    actual = stack.top.value
    assert expected == actual


def test_push_multiple():
    '''Can successfully push multiple values onto a stack'''
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    expected = True
    actual = stack.includes('B')
    assert expected == actual


def test_pop_one():
    '''Can successfully pop off the stack'''
    stack = Stack()
    stack.push(1)
    stack.pop()
    expected = None
    actual = stack.top.value
    assert actual == expected


def test_pop_all():
    '''Can successfully empty a stack after multiple pops'''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    expected = None
    actual = stack.top.value
    assert actual == expected


def test_peek():
    '''Can successfully peek the next item on the stack'''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    actual = stack.peek()
    expected = 2
    assert actual == expected


def test_Stack_empty():
    '''Can successfully instantiate an empty stack'''
    stack = Stack()
    actual = stack.top.value
    expected = None
    assert actual == expected


def test_enqueue_one():
    '''Can successfully enqueue into a queue'''
    q = Queue()
    q.enqueue('Hello')
    expected = 'Hello'
    actual = q.front.value
    assert expected == actual


def test_enqueue_multiple():
    '''Can successfully enqueue multiple values into a queue'''
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    expected = 'A'
    actual = q.front.value
    assert expected == actual


def test_dequeue_one():
    '''Can successfully dequeue out of a queue the expected value'''
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.rear.dequeue()
    q.front.dequeue()
    expected = 'B'
    actual = q.front.value
    assert expected == actual


def test_dequeue_all():
    '''Can successfully empty a queue after multiple dequeues'''
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.rear.dequeue()
    q.rear.dequeue()
    q.front.dequeue()
    expected = None
    actual = q.front.value
    assert expected == actual


def test_peek():
    '''Can successfully peek into a queue, seeing the expected value'''
    q = Queue()
    q.peek(1)
    q.peek(2)
    actual = q.peek()
    expected = 2
    assert actual == expected


def test_Queue_empty():
    '''Can successfully instantiate an empty queue'''
    q = Queue()
    actual = q.front.value
    expected = None
    assert actual == expected
