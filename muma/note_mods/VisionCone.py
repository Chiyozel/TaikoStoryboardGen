from muma.utils import findsetting, isfloat
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans
import math


class VisionCone(BasicMod):
    def mod_setup(self):
        print("Frequency (Rounded to integers)")
        while True:
            freq_str = raw_input(">>>")
            if isfloat(freq_str):
                break
        self.freq = max(float(freq_str), 1)

        print("Amplitude")
        while True:
            amp_str = raw_input(">>>")
            if isfloat(amp_str):
                break
        self.amp = 50 * float(amp_str)

    def note_to_sb_2(self, note, initial_t):
        r_string = ""
        playfield_length = int(findsetting("PlayfieldLength"))
        note_in = int(note.t - (60000 / self.bpm * (4 / self.scroll)))
        note_y = (self.amp * (-1 if self.is_upside_down else 1)) * math.sin(
            (note.t - initial_t) / ((2 * 60000 / self.bpm) / self.freq) * math.pi) + self.receptor_y()

        # Note
        r_string += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
        r_string += " MY,0,{},{},{},{}\n".format(note_in, note.t, note_y, self.receptor_y())
        r_string += " MX,0,{},{},{},{}\n".format(note_in, note.t,
                                                 self.receptor_x() + playfield_length * (-1 if self.is_reverse else 1),
                                                 self.receptor_x())
        r_string += muma.note_mods.sbUtils.sbUtils.scale_big(note)
        r_string += n_trans(note, self.color, note_in)

        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        elif self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)

        # Note Overlay
        r_string += muma.note_mods.sbUtils.sbUtils.overlay(note, self.color)
        r_string += n_trans(note, self.color, note_in, True)
        r_string += " MY,0,{},{},{},{}\n".format(note_in, note.t, note_y, self.receptor_y())
        r_string += " MX,0,{},{},{},{}\n".format(note_in, note.t,
                                                 self.receptor_x() + playfield_length * (-1 if self.is_reverse else 1),
                                                 self.receptor_x())

        return r_string

    def make_sb(self):
        out = ""
        rev_note_list = list(reversed(self.note_list))
        for i in range(0, len(rev_note_list)):
            out += self.note_to_sb_2(rev_note_list[i], self.note_list[0].t)
        return out
