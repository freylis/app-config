# coding: utf-8
from appconfig import *
from appconfig.exceptions import BadValueError


def test_some():
    # check strings
    assert get_str('sec', 'a') == '11'
    assert get_str('sec', 'b') == '11'
    assert get_str('sec', 'c') == '1.1'
    assert get_str('sec', 'd') is None
    try:
        get_str('sec', 'd', lazy=False) == None
    except BadValueError:
        assert True
    else:
        assert False

    # check int
    assert get_int('sec', 'a') == 11
    assert get_int('sec', 'b') == 11
    assert get_int('sec', 'c') == 1
    assert get_int('sec', 'd') is None
    assert get_int('sec', 'z') is None
    try:
        assert get_int('sec', 'z', lazy=False)
    except BadValueError:
        assert True
    else:
        assert False

    # check float
    assert get_float('sec', 'a') == 11.0
    assert get_float('sec', 'b') == 11.0
    assert get_float('sec', 'c') == 1.1
    assert get_float('sec', 'd') is None
    assert get_float('sec', 'z') is None
    try:
        assert get_int('sec', 'z', lazy=False)
    except BadValueError:
        assert True
    else:
        assert False

    # check bool
    assert get_bool('bool', 'a')
    assert get_bool('bool', 'b')
    assert get_bool('bool', 'c') is False
    assert get_bool('bool', 'd') is False


if __name__ == '__main__':
    test_some()
