from tree import BinaryTree, BinarySearchTree, Node


def test_tree_instance():
    '''Can successfully instantiate an empty tree'''
    tree = BinaryTree()
    assert tree.root is None


def test_tree_one():
    '''Can successfully instantiate a tree with a single root node'''
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree.root.value == 'apples'


def test_tree_five():
    '''Can successfully add a left child and right child to a single root node'''
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(9)
    tree.add(20)
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15
    assert tree.root.left.right.value == 9
    assert tree.root.right.right.value == 20


def test_preorder():
    '''Can successfully return a collection from a preorder traversal'''
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    expected = [10, 5, 15]
    actual = tree.pre_order()
    assert expected == actual


def test_inorder():
    '''Can successfully return a collection from an inorder traversal'''
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(11)
    tree.add(22)
    tree.add(56)
    expected = [5, 10, 11, 15, 22, 56]
    actual = tree.in_order()
    assert expected == actual


def test_postorder():
    '''Can successfully return a collection from a postorder traversal'''
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(11)
    tree.add(22)
    tree.add(56)
    expected = [5, 11, 56, 22, 15, 10]
    actual = tree.post_order()
    assert expected == actual
