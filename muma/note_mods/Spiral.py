from muma.utils import findsetting, isfloat
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans
import math


class Spiral(BasicMod):
    def note_to_sb(self, note):
        pass

    def mod_setup(self):
        print("Angle offset (in deg)")
        while True:
            angleoffset = input(">>>")
            if isfloat(angleoffset):
                break
        self.angle = float(angleoffset)
        print("Angle delta")
        while True:
            angledelta = input(">>>")
            if isfloat(angledelta):
                break
        self.angle_diff = float(angledelta)

    def note_to_sb_2(self, note, x):
        r_string = ""
        playfield_length = int(findsetting("PlayfieldLength"))
        note_in = int(note.t - (60000 / self.bpm * (4 / self.scroll)))
        angle = muma.note_mods.sbUtils.sbUtils.convert_deg_to_rad(self.angle + x * self.angle_diff)

        """
        +------+
        | Note |
        +------+
        """
        r_string += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
        r_string += " M,0,{},{},{},{},{},{}\n".format(note_in,
                                                      note.t,
                                                      int(self.receptor_x() + (
                                                          -1 if self.is_reverse else 1) * playfield_length * math.cos(
                                                          angle)),
                                                      int(self.receptor_y() - (
                                                          -1 if self.is_upside_down else 1) * playfield_length * math.sin(
                                                          angle)),
                                                      self.receptor_x(),
                                                      self.receptor_y())
        r_string += muma.note_mods.sbUtils.sbUtils.scale_big(note)
        r_string += n_trans(note, self.color, note_in)

        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        if self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)

        """
        +--------------+
        | Note Overlay |
        +--------------+
        """
        r_string += muma.note_mods.sbUtils.sbUtils.overlay(note, self.color)
        r_string += n_trans(note, self.color, note_in, True)
        r_string += " M,0,{},{},{},{},{},{}\n".format(note_in,
                                                      note.t,
                                                      int(self.receptor_x() + (
                                                          -1 if self.is_reverse else 1) * playfield_length * math.cos(
                                                          angle)),
                                                      int(self.receptor_y() - (
                                                          -1 if self.is_upside_down else 1) * playfield_length * math.sin(
                                                          angle)),
                                                      self.receptor_x(),
                                                      self.receptor_y())

        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        if self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)

        return r_string

    def receptor_x(self):
        return int(findsetting("SplitReceptorX"))

    def make_sb(self):
        out = ""
        rev_note_list = list(reversed(self.note_list))
        for w in range(0, len(rev_note_list)):
            out += self.note_to_sb_2(rev_note_list[w], w)
        return out
