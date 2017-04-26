from Hitsound import Hitsound
from NoteType import NoteType


class Note:
    def __init__(self, x_pos, y_pos, time, note_type, hitsound, other_params):
        self.x = x_pos
        self.y = y_pos
        self.t = time
        self.note_type = note_type
        self.hs = hitsound
        self.params = other_params

    def __str__(self):
        return "Note\n\tPosition: ({},{})\n\tTime: {}ms\n\tType: {}\n\tHitsounds: {}\n\tOther Parameters:{}".format(
            self.x, self.y, self.t, NoteType(self.note_type), Hitsound(self.hs), self.params)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.x == other.x
                and self.y == other.y
                and self.t == other.t
                and self.note_type == other.note_type
                and self.hs == other.hs
                and self.params == other.params)
