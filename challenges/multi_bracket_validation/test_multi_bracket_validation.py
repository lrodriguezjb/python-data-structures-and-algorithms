import pytest
from multi_bracket_validation import MultiBracketValidation


def test_a_bracket():
    validation = MultiBracketValidation()
    assert validation.multibracket_validation('(}') == False
    assert validation.multibracket_validation('(') == False


def test_again():
    validation = MultiBracketValidation()
    assert validation.multibracket_validation(
        '(heres)[hoping][trying]') == True


def test_string():
    validation = MultiBracketValidation()
    assert validation.multibracket_validation('yada') == True
    assert validation.multibracket_validation('lol(){yolo}') == True
    assert validation.multibracket_validation('lol(lo}') == False


def test_pairs():
    validation = MultiBracketValidation()
    assert validation.multibracket_validation('()') == True
    assert validation.multibracket_validation('[]') == True
    assert validation.multibracket_validation('{}') == True


def test_multi_pairs():
    validation = MultiBracketValidation()
    assert validation.multibracket_validation('(){}') == True
    assert validation.multibracket_validation('({})') == True
    assert validation.multibracket_validation('([]){}') == True


def test_unbalanced():
    validation = MultiBracketValidation()
    assert validation.multibracket_validation('{{}]') == False
    assert validation.multibracket_validation('[(]]') == False
    assert validation.multibracket_validation('}') == False
