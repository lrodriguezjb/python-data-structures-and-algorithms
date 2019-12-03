from array_shift import insertShiftArray


def test_one():
    expected = [1, 2, 3, 'Test', 4, 5]
    actual = insertShiftArray([1, 2, 3, 4, 5], 'Test')
    assert actual == expected


def test_two():
    expected = [1, 2, 3, 4, 5, 6, 'Test', 7, 8, 9, 10, 11]
    actual = insertShiftArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'Test')
    assert actual == expected
