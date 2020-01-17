from hashtable import Hashtable


def test_Hashtable_exists():
    assert Hashtable


def test_add_exists():
    ht = Hashtable()
    assert ht.add


def test_get_exists():
    ht = Hashtable()
    assert ht.get


def test_contains_exists():
    ht = Hashtable()
    assert ht.contains


def test_hash_exists():
    ht = Hashtable()
    assert ht.hash


def test_has_array_of_1024():
    ht = Hashtable()
    assert len(ht._array) == 1024


def test_add_one():
    ht = Hashtable()
    ht.add('test', 'object')
    assert ht._array[ht.hash('test')].head.data == ('test', 'object')


def test_add_two_to_same_index():
    ht = Hashtable()
    ht.add('test', 'object')
    ht.add('test', 'array')
    assert ht._array[ht.hash('test')].head.data == ('test', 'array')
    assert ht._array[ht.hash('test')].head._next.data == ('test', 'object')


def test_hash_is_same_each_time():
    ht = Hashtable()
    assert ht.hash('test') == ht.hash('test')


def test_contains_true():
    ht = Hashtable()
    ht.add('test', 'object')
    assert ht.contains('test') is True


def test_contains_false():
    ht = Hashtable()
    ht.add('potato', 'object')
    assert ht.contains('test') is False


def test_get_one_key():
    ht = Hashtable()
    ht.add('test', 'object')
    assert ht.get('test') == 'object'


def test_get_three_of_same_key():
    ht = Hashtable()
    ht.add('test', 'object')
    ht.add('test', 'thingy')
    ht.add('test', 'bobcat')
    assert ht.get('test') == 'object | thingy | bobcat'


def test_get_three_of_same_key_integer_values():
    ht = Hashtable()
    ht.add('test', 1)
    ht.add('test', 2)
    ht.add('test', 3)
    assert ht.get('test') == '1 | 2 | 3'