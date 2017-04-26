from yumi.utils import getbit


class NoteType:
    def __init__(self, ntype):
        self.ntype = ntype

    def __str__(self):
        strret = ""
        if getbit(self.ntype, 0):
            strret += "(Note)"
        if getbit(self.ntype, 1):
            strret += "(Slider)"
        if getbit(self.ntype, 2):
            strret += "(New Combo)"
        if getbit(self.ntype, 3):
            strret += "(Spinner)"
        return strret

    def __repr__(self):
        return self.__str__()

    def isspinner(self):
        return getbit(self.ntype, 3)

    def isslider(self):
        return getbit(self.ntype, 1)