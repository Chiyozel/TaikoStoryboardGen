import muma.note_mods.sbUtils
from muma.note_mods import BasicMod
from muma.osu.notes import Hitsound, NoteType
from muma.sbmods.transformations import note_transform as n_trans
from muma.utils import findsetting


class Split(BasicMod):
    def mod_setup(self):
        pass

    def note_to_sb(self, note):
        r_string = ""
        note_in = int(note.t - (60000 / self.bpm * 4))
        playfield_length = int(findsetting("PlayfieldLength"))

        # Note
        r_string += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")

        r_string += " MY,0,{},,{}\n".format(note_in,
                                            self.receptor_y())

        if Hitsound(note.hs).iskat() or NoteType(note.note_type).isspinner():
            r_string += " MX,0,{},{},{},{}\n".format(note_in,
                                                     note.t,
                                                     self.receptor_x() - playfield_length * (-1 if self.is_reverse else 1),
                                                     self.receptor_x())
        else:
            r_string += " MX,0,{},{},{},{}\n".format(note_in,
                                                     note.t,
                                                     self.receptor_x() + playfield_length * (-1 if self.is_reverse else 1),
                                                     self.receptor_x())

        r_string += muma.note_mods.sbUtils.sbUtils.scale_big(note)
        r_string += n_trans(note, self.color, note_in)

        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        elif self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)

        # Note Overlay
        r_string += muma.note_mods.sbUtils.sbUtils.overlay(note)
        r_string += n_trans(note, self.color, note_in, True)
        r_string += " MY,0,{},,{}\n".format(note_in,
                                            self.receptor_y())
        if Hitsound(note.hs).iskat() or NoteType(note.note_type).isspinner():
            r_string += " MX,0,{},{},{},{}\n".format(note_in,
                                                     note.t,
                                                     self.receptor_x() - playfield_length * (-1 if self.is_reverse else 1),
                                                     self.receptor_x())
        else:
            r_string += " MX,0,{},{},{},{}\n".format(note_in,
                                                     note.t,
                                                     self.receptor_x() + playfield_length * (-1 if self.is_reverse else 1),
                                                     self.receptor_x())

        return r_string

    def receptor_x(self):
        return int(findsetting("SplitReceptorX"))
