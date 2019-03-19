

class Koma:
    def __init__(self,name,rename,first,movability):
        self.name = name
        self.reverseName = rename
        self.xposition = -1
        self.yposition = -1
        self.first = first
        self.komaChange = False
        self.movablity = movablity

    def check(self,movablity:list):
        for a in self.movablity:
            if self.first:
                if a[0] == -movablity[0] and a[1] == -movablity[1]:
                    return True
            else:
                if a[0] == movablity[0] and a[1] == movablity[1]:
                    return True
        return False


class Fu:
    def __init__(self,first):
        self.name = "歩"
        self.reverseName = "と"
        self.xposition = None
        self.yposition = None
        self.first = first
        self.komaChange = False
        self.movablity = [[0,1]]
        self.reMovablity = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1]]

    def run(self,pos):
        if not self.komaChange:
            return self.check(pos)
        else:
            return self.reCheck(pos)

    def check(self,pos):
        for a in self.movablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reCheck(self,pos):
        for a in self.reMovablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reverse(self):
        if self.komaChange:
            self.komaChange = False
        else:
            self.komaChange = True

class Kyosya:
    def __init__(self,first):
        self.name = "香車"
        self.reverseName = "成香"
        self.xposition = None
        self.yposition = None
        self.first = first
        self.komaChange = False
        self.movablity = [[0,1],[0,2],[0.3],[0,4],[0,5],[0,6],[0,7],[0,8]]
        self.reMovablity = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1]]

    def run(self,pos):
        if not self.komaChange:
            return self.check(pos)
        else:
            return self.reCheck(pos)

    def check(self,pos):
        for a in self.movablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reCheck(self,pos):
        for a in self.reMovablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reverse(self):
        if self.komaChange:
            self.komaChange = False
        else:
            self.komaChange = True

class Keima:
    def __init__(self,first):
        self.name = "桂馬"
        self.reverseName = "成桂"
        self.xposition = None
        self.yposition = None
        self.first = first
        self.komaChange = False
        self.movablity = [[1,2],[-1,2]]
        self.reMovablity = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1]]

    def run(self,pos):
        if not self.komaChange:
            return self.check(pos)
        else:
            return self.reCheck(pos)

    def check(self,pos):
        for a in self.movablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reCheck(self,pos):
        for a in self.reMovablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reverse(self):
        if self.komaChange:
            self.komaChange = False
        else:
            self.komaChange = True

class Ginsyo:
    def __init__(self,first):
        self.name = "銀将"
        self.reverseName = "成銀"
        self.xposition = None
        self.yposition = None
        self.first = first
        self.komaChange = False
        self.movablity = [[0,1],[1,1],[1,-1],[1,-1],[-1,-1]]
        self.reMovablity = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1]]

    def run(self,pos):
        if not self.komaChange:
            return self.check(pos)
        else:
            return self.reCheck(pos)

    def check(self,pos):
        for a in self.movablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reCheck(self,pos):
        for a in self.reMovablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reverse(self):
        if self.komaChange:
            self.komaChange = False
        else:
            self.komaChange = True

class Kinsyo:
    def __init__(self,first):
        self.name = "金将"
        self.reverseName = None
        self.xposition = None
        self.yposition = None
        self.first = first
        self.komaChange = False
        self.movablity = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1]]
        self.reMovablity = None

    def run(self,pos):
        if not self.komaChange:
            return self.check(pos)
        else:
            return self.reCheck(pos)

    def check(self,pos):
        for a in self.movablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reCheck(self,pos):
        for a in self.reMovablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reverse(self):
        pass

class Kakugyo:
    def __init__(self,first):
        self.name = "角行"
        self.reverseName = "龍馬"
        self.xposition = None
        self.yposition = None
        self.first = first
        self.komaChange = False
        self.movablity = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8]]
        self.reMovablity =[[1,0],[-1,0],[0,1],[0,-1],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],[8,-8],[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8]]

    def run(self,pos):
        if not self.komaChange:
            return self.check(pos)
        else:
            return self.reCheck(pos)

    def check(self,pos):
        for a in self.movablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reCheck(self,pos):
        for a in self.reMovablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reverse(self):
        if self.komaChange:
            self.komaChange = False
        else:
            self.komaChange = True

class Hisya:
    def __init__(self,first):
        self.name = "飛車"
        self.reverseName = "龍王"
        self.xposition = None
        self.yposition = None
        self.first = first
        self.komaChange = False
        self.movablity = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8]]
        self.reMovablity =[[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0],[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8]]

    def run(self,pos):
        if not self.komaChange:
            return self.check(pos)
        else:
            return self.reCheck(pos)

    def check(self,pos):
        for a in self.movablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reCheck(self,pos):
        for a in self.reMovablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reverse(self):
        if self.komaChange:
            self.komaChange = False
        else:
            self.komaChange = True

class Ousyo:
    def __init__(self,first):
        self.name = "王将"
        self.reverseName = None
        self.xposition = None
        self.yposition = None
        self.first = first
        self.komaChange = False
        self.movablity = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        self.reMovablity = None

    def run(self,pos):
        if not self.komaChange:
            return self.check(pos)
        else:
            return self.reCheck(pos)

    def check(self,pos):
        for a in self.movablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reCheck(self,pos):
        for a in self.reMovablity:
            if self.first:
                if a[0] == -pos[0] and a[1] == -pos[1]:
                    return True
            else:
                if a[0] == pos[0] and a[1] == pos[1]:
                    return True
        return False

    def reverse(self):
        pass
