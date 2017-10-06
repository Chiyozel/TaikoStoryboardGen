from muma.utils import findsetting, isfloat
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans


class VerticalWave(BasicMod):
    def __init__(self, notes, bpm, transformation):
        BasicMod.__init__(self, notes, bpm, transformation)

    def setup(self):
        print("Scroll Speed Multiplier")
        while True:
            speed_str = raw_input(">>>")
            if isfloat(speed_str):
                break
        self.scroll = max(float(speed_str), 0.001)

        print("Frequency (Rounded to integers)")
        while True:
            freq_str = raw_input(">>>")
            if isfloat(freq_str):
                break
        self.freq = max(int(float(freq_str)), 1)

        print("Amplitude")
        while True:
            amp_str = raw_input(">>>")
            if isfloat(amp_str):
                break
        self.amp = 25 * min(float(amp_str), 1)

        self.array_tweens = muma.note_mods.sbUtils.sbUtils.getwavetween(3)

        print("Reverse?\t0=No\t1=Yes")
        while True:
            r_ = raw_input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_reverse = False if int(r_) == 0 else True

        print("Upside down?\t0=No\t1=Yes")
        while True:
            r_ = raw_input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_upside_down = False if int(r_) == 0 else True

        print("Mirror notes?\t0=No\t1=Yes")
        while True:
            r_ = raw_input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_mirror = False if int(r_) == 0 else True

    def note_to_sb(self, note):
        r_string = ""

        period = 4. / self.freq
        note_in = int(note.t - (60000 / self.bpm * (4 / self.scroll)))
        playfield_length = int(findsetting("PlayfieldLength"))

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

        r_string += muma.note_mods.sbUtils.sbUtils.overlay(note)
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
        return r_string
