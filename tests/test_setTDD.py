from setTDD import setTDD
import pytest

def test_setTDD_init_empty():
    tmp = setTDD()
    assert tmp != None

def test_setTDD_init_empty_check_len():
    tmp = setTDD()
    assert len(tmp) == 0

def test_setTDD_append_new_item():
    tmp = setTDD()
    tmp.append(1)
    assert len(tmp) == 1