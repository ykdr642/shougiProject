from koma import koma

def test_move():
    fu = koma([[0,1]])
    assert fu.check([1,1]) == False
    assert fu.check([0,1]) == True
