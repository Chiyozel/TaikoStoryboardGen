import abc
from muma.utils import findsetting, isfloat


class Counter:
    def __init__(self, notes):
        self.notes = notes
        self.is_reverse = self.is_upside_down = self.is_mirror = None
        self.setup()

    def make_sb(self):
        r_string = ""
        strnc = str(len(self.notes))
        notes2 = list(reversed(self.notes))
        ln = len(strnc)

        for z in range(ln, 0, -1):
            n_placement = float(z * 2 - ln - 1) / 2
            x_pos = self.counter_x() - (n_placement * self.spacing())
            r_string += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", strnc[-z])
            r_string += " M,0,{},{},{},{}\n".format(notes2[-1].t,
                                                    notes2[len(notes2) - len(self.notes) % (10 ** (z - 1)) - 1].t,
                                                    int(x_pos),
                                                    findsetting("Receptor_Y"))
            r_string += " S,0,{},{},{}\n".format(notes2[-1].t,
                                                 notes2[len(notes2) - len(self.notes) % (10 ** (z - 1)) - 1].t,
                                                 0.5 * self.scale())
            if self.is_upside_down:
                r_string += " P,0,{},,V\n".format(notes2[-1].t)
            if self.is_mirror:
                r_string += " P,0,{},,H\n".format(notes2[-1].t)

        for i in range(len(self.notes) - 1, 0, -1):
            nnext = notes2[i]
            lc = len(str(i))

            for z in range(lc, 0, -1):
                n_placement = float(z * 2 - lc - 1) / 2
                x_pos = self.counter_x() - (n_placement * self.spacing())
                if z == 1:
                    r_string += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                        "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                    r_string += " M,0,{0},{1},{2},{3}\n".format(nnext.t,
                                                                notes2[i - 1].t,
                                                                int(x_pos),
                                                                findsetting("Receptor_Y"))
                    r_string += " S,0,{0},{1},{2}\n".format(nnext.t,
                                                            notes2[i - 1].t,
                                                            0.5 * self.scale())
                if ((i + 1) % 10 ** (z - 1)) == 0 and z > 1:
                    r_string += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                        "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                    r_string += " M,0,{0},{1},{2},{3}\n".format(nnext.t,
                                                                notes2[i - 10 ** (z - 1)].t,
                                                                int(x_pos),
                                                                findsetting("Receptor_Y"))
                    r_string += " S,0,{0},{1},{2}\n".format(nnext.t,
                                                            notes2[i - 10 ** (z - 1)].t,
                                                            0.5 * self.scale())
                if self.is_upside_down:
                    r_string += " P,0,{},,V\n".format(nnext.t)
                if self.is_mirror:
                    r_string += " P,0,{},,H\n".format(nnext.t)

        return r_string

    def setup(self):
        print("Reverse?\t0=No\t1=Yes")
        while True:
            r_ = input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_reverse = False if int(r_) == 0 else True

        print("Upside down?\t0=No\t1=Yes")
        while True:
            r_ = input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_upside_down = False if int(r_) == 0 else True

        print("Mirror numbers?\t0=No\t1=Yes")
        while True:
            r_ = input(">>>")
            if r_.isdigit() and 0 <= int(r_) <= 1:
                break
        self.is_mirror = False if int(r_) == 0 else True

    @abc.abstractmethod
    def counter_x(self):
        pass

    def counter_y(self):
        return int(findsetting("UpsideDownReceptor_Y")) if self.is_upside_down else int(findsetting("Receptor_Y"))

    def scale(self):
        return float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

    def spacing(self):
        return int(findsetting("CounterNumberSpacing")) * self.scale() * (-1 if self.is_mirror else 1)
