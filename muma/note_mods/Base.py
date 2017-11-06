import abc
from muma.utils import isfloat, findsetting


class BasicMod:
    def __init__(self, notes, bpm, transformation):
        self.note_list = notes
        self.bpm = bpm
        self.color = transformation
        self.scroll = self.is_reverse = self.is_upside_down = self.is_mirror = None
        self.setup()
        self.mod_setup()

    @abc.abstractmethod
    def mod_setup(self):
        """Implement the mod-specific setups"""
        return

    def setup(self):
        print("Scroll Speed Multiplier")
        while True:
            speed_str = input(">>>")
            if isfloat(speed_str):
                break
        self.scroll = max(float(speed_str), 0.001)

        print("Reverse?\t0=No\t1=Yes")
        while True:
            r_ = input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_reverse = False if int(r_) == 0 else True

        print("Upside down?\t0=No\t1=Yes")
        while True:
            r_ = input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_upside_down = False if int(r_) == 0 else True

        print("Mirror notes?\t0=No\t1=Yes")
        while True:
            r_ = input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_mirror = False if int(r_) == 0 else True

    @abc.abstractmethod
    def note_to_sb(self, note):
        """Implement the SB structure of the mod for each note."""
        return

    def make_sb(self):
        out = ""
        rev_note_list = list(reversed(self.note_list))
        for i in range(0, len(rev_note_list)):
            out += self.note_to_sb(rev_note_list[i])
        return out

    def receptor_x(self):
        return int(findsetting("ReversedReceptor_X")) if self.is_reverse else int(findsetting("Receptor_X"))

    def receptor_y(self):
        return int(findsetting("UpsideDownReceptor_Y")) if self.is_upside_down else int(findsetting("Receptor_Y"))
