import pytest

@pytest.mark.parametrize("a,b,c", [
    (2,2,4),
    (3,3,6),
    (1,2,3)
])
def test_add(a,b,c):
    assert a+b == c, "Hello"

def test_mul():
    assert 2*2 == 4, "False"
