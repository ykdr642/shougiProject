class koma:
    def __init__(self,name,rename,firstTurn,movability):
        self.name = name
        self.reverseName = rename
        self.xposition = -1
        self.yposition = -1
        self.firstTurn = firstTurn
        self.komaChange = False
        self.movablity = movability

    def check(self,movablity:list):
        for a in self.movablity:
            if self.firstTurn:
                if a[0] == -movablity[0] and a[1] == -movablity[1]:
                    return True
            else:
                if a[0] == movablity[0] and a[1] == movablity[1]:
                    return True
        return False