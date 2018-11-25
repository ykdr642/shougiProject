class koma:
    def __init__(self,movability):
        self.name = ""
        self.reverseName = ""
        self.xposition = -1
        self.yposition = -1
        self.firstTurn = True
        self.komaChange = True
        self.movablity = movability

    def check(self,movablity:list):
        for a in self.movablity:
            if a[0] == movablity[0] and a[1] == movablity[1]:
                return True
        return False