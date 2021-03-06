from muma.utils import findsetting, isfloat
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans


class VerticalWave(BasicMod):
    def mod_setup(self):
        print("Frequency (Rounded to integers)")
        while True:
            freq_str = input(">>>")
            if isfloat(freq_str):
                break
        self.freq = max(int(float(freq_str)), 1)

        print("Amplitude")
        while True:
            amp_str = input(">>>")
            if isfloat(amp_str):
                break
        self.amp = 25 * float(amp_str)

        self.array_tweens = muma.note_mods.sbUtils.sbUtils.getwavetween(3)

    def note_to_sb(self, note):
        r_string = ""

        period = 4. / self.freq
        note_in = int(note.t - (60000 / self.bpm * (4 / self.scroll)))
        playfield_length = int(findsetting("PlayfieldLength"))

        """
        +------+
        | Note |
        +------+
        """
        r_string += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
        r_string += " MX,0,{},{},{},{}\n".format(note_in, note.t,
                                                 self.receptor_x() + playfield_length * (-1 if self.is_reverse else 1),
                                                 self.receptor_x())
        r_string += muma.note_mods.sbUtils.sbUtils.scale_big(note)
        r_string += n_trans(note, self.color, note_in)

        for i in range(self.freq, 0, -1):
            r_string += " MY,{},{},{},{},{}\n".format(self.array_tweens[0],
                                                      int(note.t - 60000 / self.bpm * (i - 0.00) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 0.25) * period),
                                                      self.receptor_y(),
                                                      self.receptor_y() - (-1 if self.is_upside_down else 1) * self.amp)
            r_string += " MY,{},{},{},{},{}\n".format(self.array_tweens[1],
                                                      int(note.t - 60000 / self.bpm * (i - 0.25) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 0.75) * period),
                                                      self.receptor_y() - (-1 if self.is_upside_down else 1) * self.amp,
                                                      self.receptor_y() + (-1 if self.is_upside_down else 1) * self.amp)
            r_string += " MY,{},{},{},{},{}\n".format(self.array_tweens[2],
                                                      int(note.t - 60000 / self.bpm * (i - 0.75) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 1.00) * period),
                                                      self.receptor_y() + (-1 if self.is_upside_down else 1) * self.amp,
                                                      self.receptor_y())

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
        r_string += " MX,0,{},{},{},{}\n".format(note_in, note.t,
                                                 self.receptor_x() + playfield_length * (-1 if self.is_reverse else 1),
                                                 self.receptor_x())
        for i in range(self.freq, 0, -1):
            r_string += " MY,{},{},{},{},{}\n".format(self.array_tweens[0],
                                                      int(note.t - 60000 / self.bpm * (i - 0.00) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 0.25) * period),
                                                      self.receptor_y(),
                                                      self.receptor_y() - (-1 if self.is_upside_down else 1) * self.amp)
            r_string += " MY,{},{},{},{},{}\n".format(self.array_tweens[1],
                                                      int(note.t - 60000 / self.bpm * (i - 0.25) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 0.75) * period),
                                                      self.receptor_y() - (-1 if self.is_upside_down else 1) * self.amp,
                                                      self.receptor_y() + (-1 if self.is_upside_down else 1) * self.amp)
            r_string += " MY,{},{},{},{},{}\n".format(self.array_tweens[2],
                                                      int(note.t - 60000 / self.bpm * (i - 0.75) * period),
                                                      int(note.t - 60000 / self.bpm * (i - 1.00) * period),
                                                      self.receptor_y() + (-1 if self.is_upside_down else 1) * self.amp,
                                                      self.receptor_y())

        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        if self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)
        return r_string
