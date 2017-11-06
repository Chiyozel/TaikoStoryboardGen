from muma.utils import findsetting, isfloat
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans


class HorizontalWave(BasicMod):
    def mod_setup(self):
        print("Frequency (Rounded to integers)")
        while True:
            freq_str = input(">>>")
            if isfloat(freq_str):
                break
        self.freq = max(int(float(freq_str)), 1)

        self.array_tweens = muma.note_mods.sbUtils.sbUtils.getwavetween(2)

    def note_to_sb(self, note):
        r_string = ""

        period = 4. / self.freq
        note_in = int(note.t - (60000 / self.bpm * (4 / self.scroll)))
        playfield_length = int(findsetting("PlayfieldLength"))
        l = (playfield_length * 1.) / self.freq

        """
        +------+
        | Note |
        +------+
        """
        r_string += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
        r_string += " MY,0,{},{},{}\n".format(note_in, note.t, self.receptor_y())
        r_string += muma.note_mods.sbUtils.sbUtils.scale_big(note)
        r_string += n_trans(note, self.color, note_in)

        for i in range(self.freq, 0, -1):
            r_string += " MX,{},{},{},{},{}\n".format(self.array_tweens[0],
                                                      int(note.t - 60000 / self.bpm * (i - 0.0) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 0.5) * period),
                                                      self.receptor_x() + (-1 if self.is_reverse else 1) * (
                                                          (i - 0.0) * l),
                                                      self.receptor_x() + (-1 if self.is_reverse else 1) * (
                                                          (i - 0.5) * l))
            r_string += " MX,{},{},{},{},{}\n".format(self.array_tweens[1],
                                                      int(note.t - 60000 / self.bpm * (i - 0.5) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 1.0) * period),
                                                      self.receptor_x() + (-1 if self.is_reverse else 1) * (
                                                          (i - 0.5) * l),
                                                      self.receptor_x() + (-1 if self.is_reverse else 1) * (
                                                          (i - 1.0) * l))
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
        r_string += " MY,0,{},{},{}\n".format(note_in, note.t, self.receptor_y())
        for i in range(self.freq, 0, -1):
            r_string += " MX,{},{},{},{},{}\n".format(self.array_tweens[0],
                                                      int(note.t - 60000 / self.bpm * (i - 0.0) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 0.5) * period),
                                                      self.receptor_x() + (-1 if self.is_reverse else 1) * (
                                                          (i - 0.0) * l),
                                                      self.receptor_x() + (-1 if self.is_reverse else 1) * (
                                                          (i - 0.5) * l))
            r_string += " MX,{},{},{},{},{}\n".format(self.array_tweens[1],
                                                      int(note.t - 60000 / self.bpm * (i - 0.5) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 1.0) * period),
                                                      self.receptor_x() + (-1 if self.is_reverse else 1) * (
                                                          (i - 0.5) * l),
                                                      self.receptor_x() + (-1 if self.is_reverse else 1) * (
                                                          (i - 1.0) * l))
        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        if self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)
        return r_string
