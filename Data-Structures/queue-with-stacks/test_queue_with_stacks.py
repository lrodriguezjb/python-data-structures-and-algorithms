import pytest
from queue_with_stacks import PseudoQueue
from stack_and_node_classes import Stack, Node

@pytest.fixture()
def empty_stack():
    new_stack = Stack()
    return new_stack

@pytest.fixture()
def stack_of_one():
    new_stack = Stack()
    new_stack.push('one')
    return new_stack

@pytest.fixture()
def stack_of_four_nodes():
    new_stack = Stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    new_stack.push(4)
    return new_stack

def test_pseudo_queue_instance(stack_of_four_nodes):
    assert PseudoQueue(stack_of_four_nodes)

def test_pseudo_queue_enqueue_one(empty_stack):
    new_queue = PseudoQueue(empty_stack)
    new_queue.enqueue('one')
    assert new_queue.stack_a.peek() == 'one'


def test_pseudoqueue_enqueue_many(stack_of_four_nodes):
    new_queue = PseudoQueue(stack_of_four_nodes)
    assert new_queue.stack_a.peek() == 4
    new_queue.enqueue('sunshine')
    assert new_queue.stack_a.peek() == 'sunshine'
    new_queue.enqueue('mangosteen')
    new_queue.enqueue(8)
    assert new_queue.stack_a.peek() == 8

def test_pseudoqueue_dequeue_none(empty_stack):
    new_queue = PseudoQueue(empty_stack)
    new_queue.dequeue()
    assert new_queue.stack_a.peek() == None

def test_pseudo_queue_dequeue_one(stack_of_four_nodes):
    new_queue = PseudoQueue(stack_of_four_nodes)
    assert new_queue.dequeue() == 1
    

def test_pseudo_queue_dequeue_many(stack_of_four_nodes):
    new_queue = PseudoQueue(stack_of_four_nodes)
    assert new_queue.stack_a.peek() == 4
    assert new_queue.dequeue() == 1
    assert new_queue.dequeue() == 2
    assert new_queue.stack_a.peek() == 4
    assert new_queue.dequeue() == 3
    assert new_queue.dequeue() == 4
    assert new_queue.stack_a.peek() == None    
