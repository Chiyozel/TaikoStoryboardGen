import math

import muma.note_mods.sbUtils
from muma.note_mods.Base import BasicMod
from muma.sbmods.transformations import note_transform as n_trans
from muma.utils import findsetting, isfloat


class Clock(BasicMod):
    def note_to_sb(self, note):
        pass

    def __init__(self, notes, bpm, transformation):
        self.beat_len = self.clock_rad = None
        BasicMod.__init__(self, notes, bpm, transformation)

    def setup(self):
        print("Length of a Clock revolution in beats")
        while True:
            len_str = raw_input(">>>")
            if isfloat(len_str):
                break
        self.beat_len = min(float(len_str), 32)

        print("Radius of the clock")
        while True:
            rad_srt = raw_input(">>>")
            if rad_srt.isdigit():
                break
        self.clock_rad = int(rad_srt)

        print("Reverse?\t0=No\t1=Yes")
        while True:
            r_ = raw_input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_reverse = False if int(r_) == 0 else True

        print("Mirror notes?\t0=No\t1=Yes")
        while True:
            r_ = raw_input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_mirror = False if int(r_) == 0 else True

    def note_to_sb_clock(self, note, n_in):
        note_in = n_in.t
        r_string = ""
        note_out = int(note_in + (60000 / self.bpm * self.beat_len))
        note_beat = (note.t - note_in) / (60000 / self.bpm)

        if float(note_beat) < (float(self.beat_len) - 0.125):
            note_y = 360 + self.clock_rad * math.sin(
                (note_beat / ((-1 if self.is_reverse else 1) * self.beat_len)) * (2 * math.pi) - 0.5 * math.pi)
            note_x = 320 + self.clock_rad * math.cos(
                (note_beat / ((-1 if self.is_reverse else 1) * self.beat_len)) * (2 * math.pi) - 0.5 * math.pi)
            note_x, note_y = int(note_x), int(note_y)

            # Note
            r_string += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
                "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
            r_string += " MY,0,{},{},{}\n".format(note_in, note_out, note_y)
            r_string += " MX,0,{},{},{}\n".format(note_in, note_out, note_x)

            r_string += muma.note_mods.sbUtils.sbUtils.scale_big_clock(note)
            r_string += n_trans(note, self.color, note_in)
            if self.is_mirror:
                r_string += " P,0,{},,H\n".format(note_in)

            # Note Overlay
            r_string += muma.note_mods.sbUtils.sbUtils.overlay_clock(note)
            r_string += " MY,0,{},{},{}\n".format(note_in, note_out, note_y)
            r_string += " MX,0,{},{},{}\n".format(note_in, note_out, note_x)
            r_string += n_trans(note, self.color, note_in, True)
            if self.is_mirror:
                r_string += " P,0,{},,H\n".format(note_in)

        return r_string

    def make_sb(self):
        out = ""
        rev_note_list = list(reversed(self.note_list))
        for i in range(0, len(rev_note_list)):
            out += self.note_to_sb_clock(rev_note_list[i], self.note_list[0])
        return out
