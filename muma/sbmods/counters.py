from muma.utils import findsetting, isfloat


def leftcounter(notes):
    out = ""
    num_centre = int(findsetting("CounterCentreLeft"))
    scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1
    num_spacing = int(findsetting("CounterNumberSpacing")) * scale
    notecount = len(notes)
    strnc = str(notecount)
    notes2 = list(reversed(notes))
    ln = len(strnc)

    for z in range(ln, 0, -1):
        n_placement = float(z * 2 - ln - 1) / 2
        x_pos = num_centre - (n_placement * num_spacing)
        out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
            "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", strnc[-z])
        out += " M,0,{0},{1},{2},{3}\n".format(notes2[-1].t,
                                               notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, int(x_pos),
                                               findsetting("Receptor_Y"))
        out += " S,0,{0},{1},{2}\n".format(notes2[-1].t, notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t,
                                           0.5 * scale)

    for i in range(notecount - 1, 0, -1):
        nnext = notes2[i]
        lc = len(str(i))

        for z in range(lc, 0, -1):
            n_placement = float(z * 2 - lc - 1) / 2
            x_pos = num_centre - (n_placement * num_spacing)
            if z == 1:
                out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                    "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 1].t, int(x_pos),
                                                       findsetting("Receptor_Y"))
                out += " S,0,{0},{1},{2}\n".format(nnext.t, notes2[i - 1].t, 0.5 * scale)
            if ((i + 1) % 10 ** (z - 1)) == 0 and z > 1:
                out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                    "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, int(x_pos),
                                                       findsetting("Receptor_Y"))
                out += " S,0,{0},{1},{2}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, 0.5 * scale)

    return out


# This one contains all the comments for all four counter methods. They're the same except for one or two details.
def rightcounter(notes):
    out = ""
    scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

    # Get settings for the center of the counter as well as spacing
    num_centre = int(findsetting("CounterCentreRight"))
    num_spacing = int(findsetting("CounterNumberSpacing")) * scale

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
        out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
            "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", strnc[-z])
        out += " M,0,{0},{1},{2},{3}\n".format(notes2[-1].t,
                                               notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, int(x_pos),
                                               findsetting("Receptor_Y"))
        out += " S,0,{0},{1},{2}\n".format(notes2[-1].t, notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t,
                                           0.5 * scale)

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
                out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                    "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 1].t, int(x_pos),
                                                       findsetting("Receptor_Y"))
                out += " S,0,{0},{1},{2}\n".format(nnext.t, notes2[i - 1].t, 0.5 * scale)

            # Each time another digit goes down with your current note, make sure the change happens only once
            # for 10^n, where n is the nth LSD of the number.
            if ((i + 1) % 10 ** (z - 1)) == 0 and z > 1:
                out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                    "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, int(x_pos),
                                                       findsetting("Receptor_Y"))
                out += " S,0,{0},{1},{2}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, 0.5 * scale)

    return out


def rightcountermirror(notes):
    out = ""
    scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1
    num_centre = int(findsetting("CounterCentreRight"))
    num_spacing = int(findsetting("CounterNumberSpacing")) * scale
    notecount = len(notes)
    strnc = str(notecount)
    notes2 = list(reversed(notes))
    ln = len(strnc)

    for z in range(ln, 0, -1):
        n_placement = float(z * 2 - ln - 1) / -2
        x_pos = num_centre - (n_placement * num_spacing)
        out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
            "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", strnc[-z])
        out += " M,0,{0},{1},{2},{3}\n".format(notes2[-1].t,
                                               notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, int(x_pos),
                                               findsetting("Receptor_Y"))
        out += " S,0,{0},{1},{2}\n".format(notes2[-1].t,
                                           notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, 0.5 * scale)
        out += " P,0,{0},{1},H\n".format(notes2[-1].t,
                                         notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t)

    for i in range(notecount - 1, 0, -1):
        nnext = notes2[i]
        lc = len(str(i))

        for z in range(lc, 0, -1):
            n_placement = float(z * 2 - lc - 1) / -2
            x_pos = num_centre - (n_placement * num_spacing)
            if z == 1:
                out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                    "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 1].t, int(x_pos),
                                                       findsetting("Receptor_Y"))
                out += " S,0,{0},{1},{2}\n".format(nnext.t, notes2[i - 1].t, 0.5 * scale)
                out += " P,0,{0},{1},H\n".format(nnext.t, notes2[i - 1].t)
            if ((i + 1) % 10 ** (z - 1)) == 0 and z > 1:
                out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                    "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, int(x_pos),
                                                       findsetting("Receptor_Y"))
                out += " S,0,{0},{1},{2}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, 0.5 * scale)
                out += " P,0,{0},{1},H\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t)

    return out


def upsidemirrorright(notes):
    out = ""
    num_centre = int(findsetting("CounterCentreRight"))
    scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1
    num_spacing = int(findsetting("CounterNumberSpacing")) * scale
    notecount = len(notes)
    strnc = str(notecount)
    notes2 = list(reversed(notes))
    ln = len(strnc)

    for z in range(ln, 0, -1):
        n_placement = float(z * 2 - ln - 1) / -2
        x_pos = num_centre - (n_placement * num_spacing)
        out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
            "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", strnc[-z])
        out += " M,0,{0},{1},{2},{3}\n".format(notes2[-1].t,
                                               notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, int(x_pos),
                                               findsetting("UpsideDownReceptor_Y"))
        out += " S,0,{0},{1},{2}\n".format(notes2[-1].t,
                                           notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t, 0.5 * scale)

        out += " P,0,{0},{1},V\n".format(notes2[-1].t,
                                         notes2[len(notes2) - notecount % (10 ** (z - 1)) - 1].t)

    for i in range(notecount - 1, 0, -1):
        nnext = notes2[i]
        lc = len(str(i))

        for z in range(lc, 0, -1):
            n_placement = float(z * 2 - lc - 1) / -2
            x_pos = num_centre - (n_placement * num_spacing)
            if z == 1:
                out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                    "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 1].t, int(x_pos),
                                                       findsetting("UpsideDownReceptor_Y"))
                out += " S,0,{0},{1},{2}\n".format(nnext.t, notes2[i - 1].t, 0.5 * scale)
                out += " P,0,{0},{1},V\n".format(nnext.t, notes2[i - 1].t)
            if ((i + 1) % 10 ** (z - 1)) == 0 and z > 1:
                out += "Sprite,Foreground,Centre,\"{}{}.png\",320,240\n".format(
                    "score-" if findsetting("UseSkinElements") else "SB/numbers/val_", str(i)[-z])
                out += " M,0,{0},{1},{2},{3}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, int(x_pos),
                                                       findsetting("UpsideDownReceptor_Y"))
                out += " S,0,{0},{1},{2}\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t, 0.5 * scale)
                out += " P,0,{0},{1},V\n".format(nnext.t, notes2[i - 10 ** (z - 1)].t)

    return out
