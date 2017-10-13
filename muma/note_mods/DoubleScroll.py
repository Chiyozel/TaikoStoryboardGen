from muma.utils import findsetting, isfloat
from muma.note_mods import BasicMod
from muma.osu.notes import Hitsound, NoteType
import muma.note_mods.sbUtils
import math
from muma.sbmods.transformations import note_transform as n_trans


class DoubleScroll(BasicMod):
    def mod_setup(self):
        print("(Don) Angle in Degrees")
        while True:
            d_angle_str = raw_input(">>>")
            if isfloat(d_angle_str):
                break
        self.d_angle = muma.note_mods.sbUtils.sbUtils.convert_deg_to_rad(float(d_angle_str))
        print("(Kat) Angle in Degrees")
        while True:
            k_angle_str = raw_input(">>>")
            if isfloat(d_angle_str):
                break
        self.k_angle = muma.note_mods.sbUtils.sbUtils.convert_deg_to_rad(float(k_angle_str))

    def note_to_sb(self, note):
        r_string = ""
        playfield_length = int(findsetting("PlayfieldLength"))
        note_in = int(note.t - (60000 / self.bpm * (4 / self.scroll)))
        hitsound = Hitsound(note.hs)
        note_type = NoteType(note.note_type)

        # Note/Don
        r_string += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
        r_string += " M,0,{},{},{},{},{},{}\n".format(note_in,
                                                      note.t,
                                                      int(self.receptor_x() + playfield_length * (
                                                          -1 if self.is_reverse else 1) * math.cos(
                                                          self.k_angle if hitsound.iskat() or note_type.isspinner() else self.d_angle)),
                                                      int(self.receptor_y() + playfield_length * (
                                                          -1 if self.is_upside_down else 1) * math.sin(
                                                          self.k_angle if hitsound.iskat() or note_type.isspinner() else self.d_angle)),
                                                      self.receptor_x(),
                                                      self.receptor_y())
        r_string += " R,0,{},,{}\n".format(note.t,
                                           self.k_angle if hitsound.iskat() or note_type.isspinner() else self.d_angle)
        r_string += muma.note_mods.sbUtils.sbUtils.scale_big(note)
        r_string += n_trans(note, self.color, note_in)

        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        elif self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)

        # Note Overlay
        r_string += muma.note_mods.sbUtils.sbUtils.overlay(note)
        r_string += " M,0,{},{},{},{},{},{}\n".format(note_in,
                                                      note.t,
                                                      int(self.receptor_x() + playfield_length * (
                                                          -1 if self.is_reverse else 1) * math.cos(
                                                          self.k_angle if hitsound.iskat() or note_type.isspinner() else self.d_angle)),
                                                      int(self.receptor_y() + playfield_length * (
                                                          -1 if self.is_upside_down else 1) * math.sin(
                                                          self.k_angle if hitsound.iskat() or note_type.isspinner() else self.d_angle)),
                                                      self.receptor_x(),
                                                      self.receptor_y())
        r_string += " R,0,{},,{}\n".format(note.t,
                                           self.k_angle if hitsound.iskat() or note_type.isspinner() else self.d_angle)
        r_string += muma.note_mods.sbUtils.sbUtils.scale_big(note)
        r_string += n_trans(note, self.color, note_in, True)

        return r_string

    def __init__(self, notes, bpm, transformation):
        BasicMod.__init__(self, notes, bpm, transformation)
