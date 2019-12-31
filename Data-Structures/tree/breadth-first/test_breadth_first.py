import pytest
from breadth_first import BinaryTree

def test_add_one_to_tree():
    new_tree = BinaryTree()
    new_tree.add(2)
    assert new_tree.root.value == 2

def test_add_three_to_tree():
    new_tree = BinaryTree()
    new_tree.add(2)
    assert new_tree.root.value == 2
    new_tree.add(7)
    assert new_tree.root.left.value == 7
    new_tree.add(5)
    assert new_tree.root.right.value == 5

def test_breadth_first_three():
    new_tree, expected = BinaryTree(), [2,7,5]
    new_tree.add(2)
    new_tree.add(7)
    new_tree.add(5)
    assert new_tree.breadth_first() == expected

def test_breadth_first_nine():
    new_tree = BinaryTree()
    expected = [2,7,5,2,6,9,5,11,4]
    new_tree.add(2)
    new_tree.add(7)
    new_tree.add(5)
    new_tree.add(2)
    new_tree.add(6)
    new_tree.add(9)
    new_tree.add(5)
    new_tree.add(11)
    new_tree.add(4)
    assert new_tree.breadth_first() == expected