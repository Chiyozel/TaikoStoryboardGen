from muma.utils import findsetting, isfloat
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans
import random


class Vibrate(BasicMod):
    def mod_setup(self):
        print("Amplitude")
        while True:
            amp_str = input(">>>")
            if isfloat(amp_str):
                break
        self.amp = 25 * float(amp_str)

        print("Beginning of Vibration")
        while True:
            beg_str = input(">>>")
            if isfloat(beg_str):
                break
        self.begin = int(beg_str)

        print("Beginning of Vibration")
        while True:
            end_str = input(">>>")
            if isfloat(end_str):
                break
        self.end = int(end_str)

    def note_to_sb(self, note):
        r_string = ""
        tab_times = []
        note_in = int(note.t - (60000 / self.bpm * (4 / self.scroll)))
        playfield_length = int(findsetting("PlayfieldLength"))

        for i in range(self.begin, self.end, 20):
            z = [i, random.randint(self.receptor_y() - self.amp, self.receptor_y() + self.amp)]
            tab_times.append(z)

        tab_times.append([self.end + 20, self.receptor_y()])

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

        for i in range(0, len(tab_times) - 1):
            r_string += " MY,0,{},,{}\n".format(tab_times[i][0], tab_times[i][1])

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
        for i in range(0, len(tab_times) - 1):
            r_string += " MY,0,{},,{}\n".format(tab_times[i][0], tab_times[i][1])

        if self.is_upside_down:
            r_string += " P,0,{},,V\n".format(note_in)
        if self.is_mirror:
            r_string += " P,0,{},,H\n".format(note_in)
        return r_string
