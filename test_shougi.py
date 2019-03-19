import koma

def tes_koma1():
    fu = koma.Koma("歩","と",False,[[0,1]])
    assert fu.check([0,-1]) == False
    assert fu.check([0,1]) == True

def tes_koma2():
    fu = koma.Koma("歩","と",True,[[0,1]])
    assert fu.check([0,-1]) == True
    assert fu.check([0,1]) == False

def test_fu1():
    fu = koma.Fu(False)
    assert fu.run([0,-1]) == False
    assert fu.run([0,1]) == True

def test_fu2():
    fu = koma.Fu(True)
    assert fu.run([0,-1]) == True
    assert fu.run([0,1]) == False

def test_kyosya1():
    kyosya = koma.Kyosya(False)
    assert kyosya.run([0,-1]) == False
    assert kyosya.run([0,1]) == True
    assert kyosya.run([1,0]) == False
    assert kyosya.run([0,8]) == True
    assert kyosya.run([0,9]) == False
    kyosya.reverse()
    assert kyosya.run([0,8]) == False
    assert kyosya.run([0,-1]) == True

def test_kyosya2():
    kyosya = koma.Kyosya(True)
    assert kyosya.run([0,-1]) == True
    assert kyosya.run([0,1]) == False
    assert kyosya.run([-1,0]) == False
    assert kyosya.run([0,-8]) == True
    assert kyosya.run([0,-9]) == False

def test_keima1():
    keima = koma.Keima(False)
    assert keima.run([1,2]) == True
    assert keima.run([-1,2]) == True
    assert keima.run([1,-2]) == False
    assert keima.run([-1,-2]) == False
    keima.reverse()
    assert keima.run([1,2]) == False
    assert keima.run([0,-1]) == True

def test_keima2():
    keima = koma.Keima(True)
    assert keima.run([1,2]) == False
    assert keima.run([-1,2]) == False
    assert keima.run([1,-2]) == True
    assert keima.run([-1,-2]) == True

def test_gin():
    gin = koma.Ginsyo(False)
    assert gin.run([0,1]) == True
    assert gin.run([1,1]) == True
    assert gin.run([1,-1]) == True
    assert gin.run([0,-1]) == False
    assert gin.run([1,0]) == False
    gin.reverse()
    assert gin.run([1,-1]) == False
    assert gin.run([0,-1]) == True
    assert gin.run([1,0]) == True

def test_kin():
    kin = koma.Kinsyo(False)
    assert kin.run([0,1]) == True
    assert kin.run([1,0]) == True
    assert kin.run([1,-1]) == False
    assert kin.run([-1,-1]) == False
    kin.reverse()
    assert kin.run([0,1]) == True
    assert kin.run([1,0]) == True
    assert kin.run([1,-1]) == False
    assert kin.run([-1,-1]) == False

def test_kaku():
    kaku = koma.Kakugyo(False)
    assert kaku.run([1,1]) == True
    assert kaku.run([8,8]) == True
    assert kaku.run([9,9]) == False
    assert kaku.run([1,0]) == False
    assert kaku.run([0,1]) == False
    kaku.reverse()
    assert kaku.run([1,1]) == True
    assert kaku.run([8,8]) == True
    assert kaku.run([9,9]) == False
    assert kaku.run([1,0]) == True
    assert kaku.run([0,1]) == True

def test_hiysa():
    hisya = koma.Hisya(False)
    assert hisya.run([1,0]) == True
    assert hisya.run([8,0]) == True
    assert hisya.run([0,1]) == True
    assert hisya.run([0,8]) == True
    assert hisya.run([9,0]) == False
    assert hisya.run([0,9]) == False
    assert hisya.run([1,1]) == False
    hisya.reverse()
    assert hisya.run([1,0]) == True
    assert hisya.run([8,0]) == True
    assert hisya.run([0,1]) == True
    assert hisya.run([0,8]) == True
    assert hisya.run([9,0]) == False
    assert hisya.run([0,9]) == False
    assert hisya.run([1,1]) == True

def test_ou():
    ou = koma.Ousyo(False)
    assert ou.run([0,1]) == True
    assert ou.run([1,1]) == True
    assert ou.run([1,2]) == False
    assert ou.run([2,0]) == False
    ou.reverse()
    assert ou.run([0,1]) == True
    assert ou.run([1,1]) == True
    assert ou.run([1,2]) == False
    assert ou.run([2,0]) == False