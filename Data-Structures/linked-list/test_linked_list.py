from linked_list import linked_list, Node
my_list = linked_list()
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
    my_list = linked_list()
    expected = False
    my_list.insert(12)
    actual = my_list.includes(13)
    assert actual == expected
def test_to_string_one():
    expected = '  3 2 1'
    my_list = linked_list()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    actual = my_list.to_string()
    assert actual == expected
def test_to_string_two():
    expected = '  1'
    my_list = linked_list()
    my_list.insert(1)
    actual = my_list.to_string()
    assert actual == expected
def test_insert_one():
    expected = 3
    my_list.insert(3)
    my_list.to_string()
    actual = my_list.head.data
    assert actual == expected
def test_insert_two():
    expected = 5
    my_list.insert(3)
    my_list.insert(4)
    my_list.insert(5)
    my_list.to_string()
    actual = my_list.head.data
    assert actual == expected