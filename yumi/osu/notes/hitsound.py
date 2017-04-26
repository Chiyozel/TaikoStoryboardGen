from yumi.utils import getbit


class Hitsound:
    def __init__(self, typehs):
        assert typehs < 16
        self.type = typehs

    def __str__(self):
        str_ret = ""
        if getbit(self.type, 1):
            str_ret += "[Whistle]"
        if getbit(self.type, 2):
            str_ret += "[Finish]"
        if getbit(self.type, 3):
            str_ret += "[Clap]"
        return str_ret

    def __repr__(self):
        return self.__str__()

    def iskat(self):
        return getbit(self.type, 1) or getbit(self.type, 3)

    def isfinish(self):
        return getbit(self.type, 2)