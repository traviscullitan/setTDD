from setTDD import setTDD
import pytest

def test_setTDD_init_empty():
    tmp = setTDD()
    assert tmp != None

def test_setTDD_init_empty_check_len():
    tmp = setTDD()
    assert len(tmp) == 0
