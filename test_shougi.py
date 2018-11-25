from koma import koma

def test_move():
    fu = koma("歩","と",False,[[0,1]])
    assert fu.check([0,-1]) == False
    assert fu.check([0,1]) == True

def test_move2():
    fu = koma("歩","と",True,[[0,1]])
    assert fu.check([0,-1]) == True
    assert fu.check([0,1]) == False
