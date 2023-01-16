from tagi.vectorization import twoPlus


def test_simple_two_plus():
    """Simple test with random argument values"""
    res = twoPlus(m=1, s=5, deltam=0.2, deltas=0.5)

    assert res
