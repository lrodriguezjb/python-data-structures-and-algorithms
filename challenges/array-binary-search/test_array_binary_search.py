from array_binary_search import binary_search


def test_one():
    expected = 11
    actual = binary_search([2, 4, 5, 10, 12, 18, 21, 30, 32, 54, 70, 76], 76)
    assert actual == expected


def test_two():
    expected = 3
    actual = binary_search([2, 4, 5, 10, 12, 18, 21, 30, 32, 54, 70, 76], 10)
    assert actual == expected


def test_three():
    expected = 1
    actual = binary_search([2, 4, 5, 10, 12, 18, 21, 30, 32, 54, 70, 76], 4)
    assert actual == expected
