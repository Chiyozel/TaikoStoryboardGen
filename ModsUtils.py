from Utils import findSetting


class Counters:
    @staticmethod
    def leftcounter(notes):
        out = ""
        num_centre = int(findSetting("CounterCentreLeft"))
        num_spacing = int(findSetting("CounterNumberSpacing"))
        notecount = len(notes)
        strnc = str(notecount)
        notes2 = list(reversed(notes))
        ln = len(strnc)

        for z in range(ln, 0, -1):
            n_placement = float(z * 2 - ln - 1) / 2
            x_pos = num_centre - (n_placement * num_spacing)
            out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(strnc[-z])
            out += " M,0,{0},{1},{2},{3}\n".format(notes2[-1].t,
                                                   notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, int(x_pos),
                                                   findSetting("Receptor_Y"))
            out += " S,0,{0},{1},0.5\n".format(notes2[-1].t, notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t)

        for i in range(notecount - 1, 0, -1):
            nnext = notes2[i]
            lc = len(str(i))

            for z in range(lc, 0, -1):
                n_placement = float(z * 2 - lc - 1) / 2
                x_pos = num_centre - (n_placement * num_spacing)
                if z == 1:
                    out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(str(i)[-z])
                    out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 1].t, int(x_pos),
                                                           findSetting("Receptor_Y"))
                    out += " S,0,{0},{1},0.5\n".format(nnext.t, notes2[i - 1].t)
                if ((i + 1) % 10 ** (z - 1)) == 0 and z > 1:
                    out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(str(i)[-z])
                    out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, int(x_pos),
                                                           findSetting("Receptor_Y"))
                    out += " S,0,{0},{1},0.5\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t)

        return out

    @staticmethod
    # This one contains all the comments for all four counter methods. They're the same except for one or two details.
    def rightcounter(notes):
        out = ""

        # Get settings for the center of the counter as well as spacing
        num_centre = int(findSetting("CounterCentreRight"))
        num_spacing = int(findSetting("CounterNumberSpacing"))

        # Counting down and transforming to string
        notecount = len(notes)
        strnc = str(notecount)

        # Reversing the order of the notes as we go down.
        notes2 = list(reversed(notes))
        ln = len(strnc)

        # Improvement over the old Java version: we check every digit automatically when preparing the counting.
        for z in range(ln, 0, -1):
            # Automatic number placement relative to the amount of digits. There is no limit to note amounts now.
            n_placement = float(z * 2 - ln - 1) / 2
            x_pos = num_centre - (n_placement * num_spacing)

            # Places every digit relative to its position in the number.
            out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(strnc[-z])
            out += " M,0,{0},{1},{2},{3}\n".format(notes2[-1].t,
                                                   notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, int(x_pos),
                                                   findSetting("Receptor_Y"))
            out += " S,0,{0},{1},0.5\n".format(notes2[-1].t, notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t)

        # Counts down.
        for i in range(notecount - 1, 0, -1):
            nnext = notes2[i]
            lc = len(str(i))

            # Same as above
            for z in range(lc, 0, -1):
                n_placement = float(z * 2 - lc - 1) / 2
                x_pos = num_centre - (n_placement * num_spacing)

                # Needed to avoid duplicate unit digits.
                if z == 1:
                    out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(str(i)[-z])
                    out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 1].t, int(x_pos),
                                                           findSetting("Receptor_Y"))
                    out += " S,0,{0},{1},0.5\n".format(nnext.t, notes2[i - 1].t)

                # Each time another digit goes down with your current note, make sure the change happens only once
                # for 10^n, where n is the nth LSD of the number.
                if ((i + 1) % 10 ** (z - 1)) == 0 and z > 1:
                    out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(str(i)[-z])
                    out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, int(x_pos),
                                                           findSetting("Receptor_Y"))
                    out += " S,0,{0},{1},0.5\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t)

        return out

    @staticmethod
    def rightcountermirror(notes):
        out = ""
        num_centre = int(findSetting("CounterCentreRight"))
        num_spacing = int(findSetting("CounterNumberSpacing"))
        notecount = len(notes)
        strnc = str(notecount)
        notes2 = list(reversed(notes))
        ln = len(strnc)

        for z in range(ln, 0, -1):
            n_placement = float(z * 2 - ln - 1) / -2
            x_pos = num_centre - (n_placement * num_spacing)
            out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(strnc[-z])
            out += " M,0,{0},{1},{2},{3}\n".format(notes2[-1].t,
                                                   notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, int(x_pos),
                                                   findSetting("Receptor_Y"))
            out += " V,0,{0},{1},-0.5,0.5\n".format(notes2[-1].t,
                                                    notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t)

        for i in range(notecount - 1, 0, -1):
            nnext = notes2[i]
            lc = len(str(i))

            for z in range(lc, 0, -1):
                n_placement = float(z * 2 - lc - 1) / -2
                x_pos = num_centre - (n_placement * num_spacing)
                if z == 1:
                    out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(str(i)[-z])
                    out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 1].t, int(x_pos),
                                                           findSetting("Receptor_Y"))
                    out += " V,0,{0},{1},-0.5,0.5\n".format(nnext.t, notes2[i - 1].t)
                if ((i + 1) % 10 ** (z - 1)) == 0 and z > 1:
                    out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(str(i)[-z])
                    out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, int(x_pos),
                                                           findSetting("Receptor_Y"))
                    out += " V,0,{0},{1},-0.5,0.5\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t)

        return out

    @staticmethod
    def leftcounterupside(notes):
        out = ""
        num_centre = int(findSetting("CounterCentreRight"))
        num_spacing = int(findSetting("CounterNumberSpacing"))
        notecount = len(notes)
        strnc = str(notecount)
        notes2 = list(reversed(notes))
        ln = len(strnc)

        for z in range(ln, 0, -1):
            n_placement = float(z * 2 - ln - 1) / -2
            x_pos = num_centre - (n_placement * num_spacing)
            out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(strnc[-z])
            out += " M,0,{0},{1},{2},{3}\n".format(notes2[-1].t,
                                                   notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, int(x_pos),
                                                   findSetting("UpsideDownReceptor_Y"))
            out += " V,0,{0},{1},0.5,-0.5\n".format(notes2[-1].t,
                                                    notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t)

        for i in range(notecount - 1, 0, -1):
            nnext = notes2[i]
            lc = len(str(i))

            for z in range(lc, 0, -1):
                n_placement = float(z * 2 - lc - 1) / -2
                x_pos = num_centre - (n_placement * num_spacing)
                if z == 1:
                    out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(str(i)[-z])
                    out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 1].t, int(x_pos),
                                                           findSetting("UpsideDownReceptor_Y"))
                    out += " V,0,{0},{1},0.5,-0.5\n".format(nnext.t, notes2[i - 1].t)
                if ((i + 1) % 10 ** (z - 1)) == 0 and z > 1:
                    out += "Sprite,Foreground,Centre,\"SB/numbers/val_{}.png\",320,240\n".format(str(i)[-z])
                    out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, int(x_pos),
                                                           findSetting("UpsideDownReceptor_Y"))
                    out += " V,0,{0},{1},0.5,-0.5\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t)

        return out


class Scrolls:
    @staticmethod
    def doublescroll(notes, bpm):
        pass

    @staticmethod
    def brake(notes, bpm):
        pass

    @staticmethod
    def reverse(notes, bpm):
        pass

    @staticmethod
    def negascroll(notes, bpm):
        pass

    @staticmethod
    def split(notes, bpm):
        pass

    @staticmethod
    def normal(notes, bpm):
        pass

    @staticmethod
    def upsidedown(notes, bpm):
        pass

    @staticmethod
    def boost(notes, bpm):
        pass

    @staticmethod
    def star(notes, bpm):
        pass

    @staticmethod
    def wave1(notes, bpm):
        pass

    @staticmethod
    def dwave1(notes, bpm):
        pass

    @staticmethod
    def wave2(notes, bpm):
        pass

    @staticmethod
    def dwave2(notes, bpm):
        pass


class Transformations:
    @staticmethod
    def abekobe(notes):
        pass

    @staticmethod
    def confusion(notes):
        pass

    @staticmethod
    def flashlight(notes):
        pass


class Hybrids:
    @staticmethod
    def reverseabekobe(notes, bpm):
        pass

    @staticmethod
    def upsidedownabekobe(notes, bpm):
        pass

    @staticmethod
    def waveconfusion(notes, bpm):
        pass

    @staticmethod
    def doublewaveconfusion(notes, bpm):
        pass


class Base:
    @staticmethod
    def createbase():
        out = ""

        # Main Black Bar
        out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
        out += " F,0,0,500000,1\n"
        out += " M,0,0,500000,320,{}\n".format(findSetting("Receptor_Y"))

        # Double Scroll Black Bar (Hidden by default)
        out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240"
        out += " R,0,0,500000,1.570796\n"
        out += " F,0,0,500000,0\n"
        out += " M,0,0,500000,{},390\n".format(findSetting("Receptor_X"))

        # Four Star Black Bars (Hidden by default)
        out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
        out += " R,0,0,500000,0.7853982\n"
        out += " F,0,0,500000,0\n"
        out += " M,0,0,500000,320,390\n"

        out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
        out += " R,0,0,500000,-0.7853982\n"
        out += " F,0,0,500000,0\n"
        out += " M,0,0,500000,320,390\n"

        out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
        out += " R,0,0,500000,1.570796\n"
        out += " F,0,0,500000,0\n"
        out += " M,0,0,500000,320,390\n"

        # Receptor
        out += "Sprite,Foreground,Centre,\"SB/point.png\",320,240\n"
        out += " S,0,0,500000,0.4\n"
        out += " F,0,0,500000,1\n"
        out += " M,0,0,500000,{},{}\n".format(findSetting("Receptor_X"), findSetting("Receptor_Y"))

        # Taiko Left Portion
        out += "Sprite,Foreground,Centre,\"SB/taiko_left.png\",320,240\n"
        out += " M,0,0,500000,{},{}\n".format(int(findSetting("CounterCentreLeft")) - 60, findSetting("Receptor_Y"))
        out += " F,0,0,50000,1\n"

        # No idea what else to add.

        return out
