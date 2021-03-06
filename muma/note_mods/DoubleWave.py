from muma.note_mods import VerticalWave


class DoubleWave(VerticalWave):
    def make_sb(self):
        out = ""
        rev_note_list = list(reversed(self.note_list))
        for i in range(0, len(rev_note_list)):
            out += self.note_to_sb(rev_note_list[i])
        self.amp = -self.amp
        for i in range(0, len(rev_note_list)):
            out += self.note_to_sb(rev_note_list[i])
        return out
