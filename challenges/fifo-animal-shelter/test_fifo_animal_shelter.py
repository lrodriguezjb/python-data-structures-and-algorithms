from fifo_animal_shelter import Animal_shelter
import pytest


def test_class_exists():
    assert Animal_shelter


def test_class_has_animal_queues():
    fife = Animal_shelter()
    assert fife.dogs
    assert fife.cats


def test_enqueue_one_cat():
    brooklyn = Animal_shelter()
    brooklyn.enqueue('cat', 'Oatmeal')

    assert brooklyn.cats.peek().name == 'oatmeal'


def test_enqueue_multiple_cats():
    bremerton = Animal_shelter()
    bremerton.enqueue('cat', 'Oatmeal')
    bremerton.enqueue('cat', 'JERRY')
    bremerton.enqueue('cat', 'Apple')

    assert bremerton.cats.peek().name == 'oatmeal'


def test_enqueue_one_dog():
    mtvernon = Animal_shelter()
    mtvernon.enqueue('dog', 'Lion')

    assert mtvernon.dogs.peek().name == 'lion'


def test_enqueue_multiple_dogs():
    bellevue = Animal_shelter()
    bellevue.enqueue('dog', 'Steve')
    bellevue.enqueue('dog', 'Ruff')
    bellevue.enqueue('dog', 'Pickles')

    assert bellevue.dogs.peek().name == 'steve'


def test_enqueue_cat_then_dog():
    kent = Animal_shelter()
    kent.enqueue('cat', 'Prissy')
    kent.enqueue('dog', 'Ruff')
    kent.enqueue('dog', 'Pickles')

    assert kent.dogs.peek().name == 'ruff'


def test_enqueue_dog_then_cat():
    renton = Animal_shelter()
    renton.enqueue('dog', 'spike')
    renton.enqueue('dog', 'Ruff')
    renton.enqueue('cat', 'BLAH')

    assert renton.cats.peek().name == 'blah'


def test_dequeue_dog():
    tacoma = Animal_shelter()
    tacoma.enqueue('dog', 'spike')
    tacoma.enqueue('dog', 'Ruff')
    tacoma.enqueue('cat', 'BLAH')

    assert tacoma.dequeue('dog').name == 'spike'


def test_dequeue_cat():
    auburn = Animal_shelter()
    auburn.enqueue('dog', 'spike')
    auburn.enqueue('dog', 'Ruff')
    auburn.enqueue('cat', 'BLAH')

    assert auburn.dequeue('cat').name == 'blah'


def test_dequeue_nonexistent_cat():
    convington = Animal_shelter()
    convington.enqueue('dog', 'spike')
    convington.enqueue('dog', 'Ruff')

    assert convington.dequeue('cat') is None


def test_dequeue_nonexistent_dog():
    tukwila = Animal_shelter()
    tukwila.enqueue('cat', 'Petunia')
    tukwila.enqueue('cat', 'Polly')

    assert tukwila.dequeue('dog') is None


def test_enqueue_bunny():
    brier = Animal_shelter()
    brier.enqueue('cat', 'Petunia')
    brier.enqueue('cat', 'Polly')

    assert brier.enqueue('bunny', 'Flops') == 'Sorry, we only accept cats or dogs.'


def test_dequeue_bunny():
    sumner = Animal_shelter()
    sumner.enqueue('cat', 'Petunia')
    sumner.enqueue('cat', 'Polly')

    assert sumner.dequeue('bunny') is None