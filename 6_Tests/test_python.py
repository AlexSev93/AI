import math

lis = [-4, 5, 10, -2]


def rem_0(n):
    if n < 0:
        return False
    else:
        return True


def test_list_():
    assert list(map(abs, lis)) == [4, 5, 10, 2], 'map err'
    assert list(sorted(lis)) == [-4, -2, 5, 10], 'sorted err'
    assert list(filter(rem_0, lis)) == [5, 10], 'filter err'


def test_math():
    assert math.pi == 3.141592653589793, 'pi err'
    assert round(math.pi, 2) == 3.14, 'pi err'
    assert math.sqrt(25) == 5, 'sqrt err'
    assert math.pow(4, 2) == 16, 'pow err'
    assert math.hypot(3, 4) == 5, 'hypol err'
