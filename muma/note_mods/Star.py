from muma.utils import findsetting, isfloat
import math
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans


class Star(BasicMod):
    def note_to_sb(self, note):
        pass

    def mod_setup(self):
        self.directions = [0, 3, 4, 1]

    def note_to_sb_2(self, note, direction, no_note):
        r_string = ""
        note_in = int(note.t - (60000 / self.bpm * (4 / self.scroll)))
        playfield_length = int(findsetting("PlayfieldLength"))

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
                                                          (no_note % 4) * math.pi / 4)),
                                                      int(self.receptor_y() - (
                                                          -1 if self.is_upside_down else 1) * playfield_length * math.sin(
                                                          (no_note % 4) * math.pi / 4)),
                                                      self.receptor_x(),
                                                      self.receptor_y())
        r_string += " R,0,{},,{}\n".format(note.t, direction * math.pi / 4)
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
                                                          (no_note % 4) * math.pi / 4)),
                                                      int(self.receptor_y() - (
                                                          -1 if self.is_upside_down else 1) * playfield_length * math.sin(
                                                          (no_note % 4) * math.pi / 4)),
                                                      self.receptor_x(),
                                                      self.receptor_y())
        r_string += " R,0,{},,{}\n".format(note.t, direction * math.pi / 4)

        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        if self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)

        return r_string

    def make_sb(self):
        out = ""
        rev_note_list = list(reversed(self.note_list))
        for w in range(0, len(rev_note_list)):
            out += self.note_to_sb_2(rev_note_list[w], self.directions[w % 4], w)
        return out

    def receptor_x(self):
        return int(findsetting("SplitReceptorX"))
