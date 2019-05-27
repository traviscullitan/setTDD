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

def test_setTDD_append_duplicate_item():
    tmp = setTDD()
    tmp.append(1)
    tmp.append(1)
    assert len(tmp) == 1

def test_setTDD_append_multiple_items():
    tmp = setTDD()
    tmp.append(1)
    tmp.append(2)
    tmp.append(2)
    tmp.append(1)
    assert len(tmp) == 2

def test_setTDD_remove_empty():
    tmp = setTDD()
    with pytest.raises(ValueError, match=r".*No Such Element In Set.*"):
        tmp.remove(1)

def test_setTDD_remove_nonexistant():
    tmp = setTDD()
    tmp.append(2)
    assert len(tmp) == 1
    with pytest.raises(ValueError, match=r".*No Such Element In Set.*"):
        tmp.remove(1)

def test_setTDD_remove_existing():
    tmp = setTDD()
    tmp.append(1)
    assert len(tmp) == 1
    tmp.remove(1)
    assert len(tmp) == 0

def test_setTDD_iterate_empty():
    tmp = setTDD()
    i = iter(tmp)
    assert i != None

def test_setTDD_iterate_item():
    tmp = setTDD()
    tmp.append(1)
    i = iter(tmp)
    assert next(i) == 1
    with pytest.raises(StopIteration):
        next(i)

