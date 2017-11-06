from muma.utils import findsetting, isfloat
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans


class TangentZ(BasicMod):
    def note_to_sb(self, note):
        r_string = ""
        note_in = int(note.t - (60000 / self.bpm * (4 / self.scroll)))
        period = 4. / self.freq
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

        r_string += muma.note_mods.sbUtils.sbUtils.tan_scale(note, self.freq, self.bpm)
        r_string += n_trans(note, self.color, note_in)
        for y in range(self.freq, 0, -1):
            r_string += " F,15,{},{},1\n".format(int(note.t - 60000 / self.bpm * (y - 0.5) * period),
                                                 int(note.t - 60000 / self.bpm * (y - 1.0) * period))
            r_string += " F,16,{},{},1,0\n".format(int(note.t - 60000 / self.bpm * (y - 0.0) * period),
                                                   int(note.t - 60000 / self.bpm * (y - 0.5) * period))

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
        r_string += muma.note_mods.sbUtils.sbUtils.tan_scale(note, self.freq, self.bpm)
        r_string += " MY,{},{},,{}\n".format(self.tween,
                                             note_in,
                                             self.receptor_y())

        r_string += " MX,{},{},{},{},{}\n".format(self.tween,
                                                  note_in,
                                                  note.t,
                                                  self.receptor_x() + playfield_length * (-1 if self.is_reverse else 1),
                                                  self.receptor_x())

        r_string += n_trans(note, self.color, note_in, True)
        for y in range(self.freq, 0, -1):
            r_string += " F,15,{},{},1\n".format(int(note.t - 60000 / self.bpm * (y - 0.5) * period),
                                                 int(note.t - 60000 / self.bpm * (y - 1.0) * period))
            r_string += " F,16,{},{},1,0\n".format(int(note.t - 60000 / self.bpm * (y - 0.0) * period),
                                                   int(note.t - 60000 / self.bpm * (y - 0.5) * period))
        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        if self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)

        return r_string

    def mod_setup(self):
        print("Frequency (Rounded to integers)")
        while True:
            freq_str = input(">>>")
            if isfloat(freq_str):
                break
        self.freq = max(int(float(freq_str)), 1)
        self.tween = muma.note_mods.sbUtils.sbUtils.getwavetween(1)[0]
