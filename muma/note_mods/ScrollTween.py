from muma.utils import findsetting
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans


class ScrollTween(BasicMod):
    def __init__(self, notes, bpm, transformation):
        BasicMod.__init__(self, notes, bpm, transformation)
        self.tween = 0

    def mod_setup(self):
        pass

    def tween_setup(self):
        self.tween = muma.note_mods.sbUtils.sbUtils.getwavetween(1)[0]

    def note_to_sb(self, note):
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
        r_string += " MY,{},{},,{}\n".format(self.tween,
                                             note_in,
                                             self.receptor_y())

        r_string += " MX,{},{},{},{},{}\n".format(self.tween,
                                                  note_in,
                                                  note.t,
                                                  self.receptor_x() + playfield_length * (-1 if self.is_reverse else 1),
                                                  self.receptor_x())

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
        r_string += " MY,{},{},,{}\n".format(self.tween,
                                             note_in,
                                             self.receptor_y())

        r_string += " MX,{},{},{},{},{}\n".format(self.tween,
                                                  note_in,
                                                  note.t,
                                                  self.receptor_x() + playfield_length * (-1 if self.is_reverse else 1),
                                                  self.receptor_x())

        r_string += n_trans(note, self.color, note_in, True)

        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        if self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)

        return r_string
