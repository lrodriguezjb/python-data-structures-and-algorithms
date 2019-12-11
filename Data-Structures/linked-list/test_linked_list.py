import pytest
from linked_list import LinkedList, Node


my_list = LinkedList()


def test_make_node():
    expected = Node
    actual = Node(3)
    assert type(actual) == expected


def test_includes_true():
    expected = True
    my_list.insert(12)
    actual = my_list.includes(12)
    assert actual == expected


def test_includes_false():
    my_list = LinkedList()
    expected = False
    my_list.insert(12)
    actual = my_list.includes(13)
    assert actual == expected


def test_to_string_one():
    expected = "  3 2 1"
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    actual = my_list.to_string()
    assert actual == expected


def test_to_string_two():
    expected = "  1"
    my_list = LinkedList()
    my_list.insert(1)
    actual = my_list.to_string()
    assert actual == expected


def test_insert_one():
    expected = 3
    my_list.insert(3)
    my_list.to_string()
    actual = my_list.head.value
    assert actual == expected


def test_insert_two():
    expected = 5
    my_list.insert(3)
    my_list.insert(4)
    my_list.insert(5)
    my_list.to_string()
    actual = my_list.head.value
    assert actual == expected


def test_append_one():
    my_list = LinkedList()
    expected = 1
    my_list.append(1)
    assert my_list.includes(1) == True


def test_append_two():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.append(3)
    assert my_list.includes(3) == True


def test_insert_after_one():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    my_list.insert_after(2, 4)
    assert my_list.to_string() == "  3 2 4 1"


def test_insert_after_two():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    my_list.insert_after(1, 4)
    assert my_list.to_string() == "  3 2 1 4"


def test_insert_before_one():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    my_list.insert_before(2, 7)
    assert my_list.to_string() == "  3 7 2 1"


def test_insert_before_two():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    my_list.insert_before(3, 7)
    assert my_list.to_string() == "  7 3 2 1"


def test_k_is_greater_than_length():
    my_list = LinkedList()
    my_list.insert(2)
    my_list.insert(8)
    my_list.insert(3)
    my_list.insert(1)
    assert my_list.kth_from_end(20) == "K is out of range"


def test_k_is_same_length():
    my_list = LinkedList()
    assert my_list.kth_from_end(6) == "K is out of range"


def test_k_is_negative():
    my_list = LinkedList()
    assert my_list.kth_from_end(-4) == "K is out of range"


def test_k_is_in_list_of_one():
    my_list = LinkedList()
    my_list.insert(2)
    assert my_list.kth_from_end(0) == 2


def test_happy_k():
    my_list = LinkedList()
    my_list.insert(2)
    my_list.insert(8)
    my_list.insert(3)
    my_list.insert(1)
    assert my_list.kth_from_end(2) == 3


@pytest.fixture(autouse=True)
def clean():
    my_list = []
