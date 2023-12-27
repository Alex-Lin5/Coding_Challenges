import pytest
def inc(x):
    return x + 1

def test_inc():
    assert 4==5
    assert inc(3) == 5

test_inc()