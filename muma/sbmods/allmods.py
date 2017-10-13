"""
Storyboard Scroll Types
"""

import math

from muma.osu.notes import NoteType, Hitsound
from muma.sbmods.transformations import note_transform as n_trans
from muma.utils import findsetting
from muma.utils import isfloat


# Done | Needs R/UD
def horizwave(notes, bpm, tween, freq, z):
    out = ""
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))
    notecount = len(notes)
    scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_hs = Hitsound(n.hs)
        n_st = n.t - n_in

        out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)

        for w in range(0, freq):
            out += " MX,{},{},{},{},{}\n".format(tween[0],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))
            out += " MX,{},{},{},{},{}\n".format(tween[1],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))

        if n_hs.isfinish():
            out += " S,0,{},,{}\n".format(n.t, 0.5 * scale)
        else:
            out += " S,0,{},,{}\n".format(n.t, 0.35 * scale)

        out += n_trans(n, z, n_in, False)

        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
                "taikobigcircleoverlay" if findsetting("UseSkinElements") else "SB/notebig-overlay")
            out += " S,0,{},,{}\n".format(n.t, 0.5 * scale)
        else:
            out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
                "taikohitcircleoverlay" if findsetting("UseSkinElements") else "SB/note-overlay")
            out += " S,0,{},,{}\n".format(n.t, 0.35 * scale)

        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        for w in range(0, freq):
            out += " MX,{},{},{},{},{}\n".format(tween[0],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))
            out += " MX,{},{},{},{},{}\n".format(tween[1],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))
        out += n_trans(n, z, n_in, True)

    return out


# Pending Adaptation | Needs R/UD
def star(notes, bpm, z):
    out = ""

    # Additional black bars to see notes better.
    out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
    out += " R,0,{},,0.7853982\n".format(notes[0].t)
    out += " F,0,{},{},0,1\n".format(notes[0].t - 500, notes[0].t)
    out += " F,0,{},{},1,0\n".format(notes[-1].t, notes[-1].t + 500)
    out += " M,0,{},,320,{}\n".format(notes[0].t, int(findsetting("Receptor_Y")))

    out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
    out += " R,0,{},,-0.7853982\n".format(notes[0].t)
    out += " F,0,{},{},0,1\n".format(notes[0].t - 500, notes[0].t)
    out += " F,0,{},{},1,0\n".format(notes[-1].t, notes[-1].t + 500)
    out += " M,0,{},,320,{}\n".format(notes[0].t, int(findsetting("Receptor_Y")))

    out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
    out += " R,0,{},,1.570796\n".format(notes[0].t)
    out += " F,0,{},{},0,1\n".format(notes[0].t - 500, notes[0].t)
    out += " F,0,{},{},1,0\n".format(notes[-1].t, notes[-1].t + 500)
    out += " M,0,{},,320,{}\n".format(notes[0].t, int(findsetting("Receptor_Y")))

    # Get notecount, receptor coordinates, playfield length. Reverse the notes list for the correct draw order.
    # Note rotation is already predefined.
    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = 320
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = 500
    rot_i = [0, 3, 4, 1]

    for i in range(0, notecount):
        n = notes2[i]  # Current note
        n_in = int(n.t - (60000 / bpm * 4))  # Drawing time
        n_hs = Hitsound(n.hs)

        # Gotta trig this: Drawing time and end time are unchanged. But we need to make sure the origin points of the
        # note are correct by using trigonometry. This saves up conditional stuff and makes the code less cluttered.
        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos((i % 4) * math.pi / 4)),
                                                 int(receptor_y - pfl * math.sin((i % 4) * math.pi / 4)),
                                                 receptor_x,
                                                 receptor_y)
        out += " R,0,{},,{}\n".format(n.t, (rot_i[i % 4]) * math.pi / 4)  # Predefined rotation type. Still using trig.

        # Finisher scale rules
        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        # Note coloring rules
        out += n_trans(n, z, n_in, False)

        # Overlay rules remain the same as note rules.
        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)

        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos((i % 4) * math.pi / 4)),
                                                 int(receptor_y - pfl * math.sin((i % 4) * math.pi / 4)),
                                                 receptor_x,
                                                 receptor_y)
        out += " R,0,{},,{}\n".format(n.t, (rot_i[i % 4]) * math.pi / 4)
        out += n_trans(n, z, n_in, True)

    return out


# Pending Adaptation
def spiral(notes, bpm, degoffset, z):
    # This mod is centered on a single point.
    d2r_scale = math.pi / 180  # Deg to Radians ratio.
    out = ""

    # Get notecount, receptor coordinates, playfield length. Reverse the notes list for the correct draw order.
    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = 320
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = 500

    for i in range(0, notecount):
        angle = (i * degoffset) % 360  # Angle of the current note, expressed only between 0 and 360 deg.
        angle_rad = angle * d2r_scale  # Convert to radians

        n = notes2[i]  # Current note
        n_in = int(n.t - (60000 / bpm * 8))  # Draw time
        n_hs = Hitsound(n.hs)

        # Similar to the 4 Star mode, we get the original draw points through trig. However, the note rotation is
        # different as it depends of the angle of which it comes from.
        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos(angle_rad)),
                                                 int(receptor_y - pfl * math.sin(angle_rad)),
                                                 receptor_x,
                                                 receptor_y)
        out += " R,0,{},,{}\n".format(n.t, angle_rad)

        # Finisher scale
        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        # Note Color
        out += n_trans(n, z, n_in, False)

        # Same rules as normal note
        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)

        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos(angle_rad)),
                                                 int(receptor_y - pfl * math.sin(angle_rad)),
                                                 receptor_x,
                                                 receptor_y)
        out += " R,0,{},,{}\n".format(n.t, angle_rad)
        out += n_trans(n, z, n_in, True)

    return out


# Done | Needs R/UD
def tanz(notes, bpm, freq, z):
    freq2 = 4. / freq  # It's actually the period; it's so we can have more periods if the frequency is higher.
    scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

    # Get notecount, receptor coordinates, playfield length. Reverse the notes list for the correct draw order.
    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    out = ""

    for i in range(0, notecount):
        n = notes2[i]  # Current note
        n_in = int(n.t - (60000 / bpm * 4))  # Drawing time
        n_hs = Hitsound(n.hs)

        # Rule: On the X axis, scroll normally. On the Y axis, scroll such that:
        # - Move vertically following the wave tween type provided by the user. Wave tweens are defined in tweentypes.py
        # - Do it freq amount of times. As it is regular, each time will be divided by 4 subtweens.
        # - Amplitude is how big the change is.
        out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        for q in range(freq, 0, -1):
            if n_hs.isfinish():
                out += " S,2,{},{},{},{}\n".format(int(n.t - 60000 / bpm * (q - 0.0) * freq2),
                                                   int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                                   0.5 * scale,
                                                   5 * scale)

                out += " S,1,{},{},0,{}\n".format(int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                                  int(n.t - 60000 / bpm * (q - 1.0) * freq2),
                                                  0.5 * scale)
            else:
                out += " S,2,{},{},{},{}\n".format(int(n.t - 60000 / bpm * (q - 0.0) * freq2),
                                                   int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                                   0.35 * scale,
                                                   3.5 * scale)
                out += " S,1,{},{},0,{}\n".format(int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                                  int(n.t - 60000 / bpm * (q - 1.0) * freq2),
                                                  0.35 * scale)
            out += " F,0,{},{},1\n".format(int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                           int(n.t - 60000 / bpm * (q - 1) * freq2))
            out += " F,1,{},{},1,0\n".format(int(n.t - 60000 / bpm * (q - 0) * freq2),
                                             int(n.t - 60000 / bpm * (q - 0.5) * freq2))

        # Note coloring rules
        out += n_trans(n, z if z < 5 else 0, n_in, False)

        # I don't need to explain it once again, the rules are described above. Overlay rules are the same.
        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
                "taikobigcircleoverlay" if findsetting("UseSkinElements") else "SB/notebig-overlay")
            for q in range(freq, 0, -1):
                out += " S,2,{},{},{},{}\n".format(int(n.t - 60000 / bpm * (q - 0.0) * freq2),
                                                   int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                                   0.5 * scale,
                                                   5 * scale)

                out += " S,1,{},{},0,{}\n".format(int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                                  int(n.t - 60000 / bpm * (q - 1.0) * freq2),
                                                  0.5 * scale)

                out += " F,0,{},{},1\n".format(int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                               int(n.t - 60000 / bpm * (q - 1) * freq2))

                out += " F,1,{},{},1,0\n".format(int(n.t - 60000 / bpm * (q - 0) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.5) * freq2))

        else:
            out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
                "taikohitcircleoverlay" if findsetting("UseSkinElements") else "SB/note-overlay")
            for q in range(freq, 0, -1):
                out += " S,2,{},{},{},{}\n".format(int(n.t - 60000 / bpm * (q - 0.0) * freq2),
                                                   int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                                   0.35 * scale,
                                                   3.5 * scale)
                out += " S,1,{},{},0,{}\n".format(int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                                  int(n.t - 60000 / bpm * (q - 1.0) * freq2),
                                                  0.35 * scale)
                out += " F,0,{},{},1\n".format(int(n.t - 60000 / bpm * (q - 0.5) * freq2),
                                               int(n.t - 60000 / bpm * (q - 1) * freq2))
                out += " F,1,{},{},1,0\n".format(int(n.t - 60000 / bpm * (q - 0) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.5) * freq2))

        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += n_trans(n, z, n_in, True)

    return out


# Done | Needs R/UD
def compound(notes, bpm, h_wave_type, v_wave_type, amplitude, freq, z):
    freq2 = 4. / freq  # It's actually the period; it's so we can have more periods if the frequency is higher.
    scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

    # Get notecount, receptor coordinates, playfield length. Reverse the notes list for the correct draw order.
    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    out = ""

    for i in range(0, notecount):
        n = notes2[i]  # Current note
        n_in = int(n.t - (60000 / bpm * 4))  # Drawing time
        n_hs = Hitsound(n.hs)
        n_st = n.t - n_in

        # Rule: On the X axis, horizontal scroll wave. On the Y axis, scroll such that:
        # - Move vertically following the wave tween type provided by the user. Wave tweens are defined in tweentypes.py
        # - Do it freq amount of times. As it is regular, each time will be divided by 4 subtweens.
        # - Amplitude is how big the change is.
        out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
        # out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
        for w in range(0, freq):
            out += " MX,{},{},{},{},{}\n".format(h_wave_type[0],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))
            out += " MX,{},{},{},{},{}\n".format(h_wave_type[1],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))
        for q in range(freq, 0, -1):
            out += " MY,{},{},{},{},{}\n".format(v_wave_type[0], int(n.t - 60000 / bpm * (q - 0.00) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.25) * freq2), receptor_y,
                                                 receptor_y - amplitude)
            out += " MY,{},{},{},{},{}\n".format(v_wave_type[1], int(n.t - 60000 / bpm * (q - 0.25) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.75) * freq2), receptor_y - amplitude,
                                                 receptor_y + amplitude)
            out += " MY,{},{},{},{},{}\n".format(v_wave_type[2], int(n.t - 60000 / bpm * (q - 0.75) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 1.00) * freq2), receptor_y + amplitude,
                                                 receptor_y)

        # Smaller comment to say finisher scale rules.
        if n_hs.isfinish():
            out += " S,0,{},,{}\n".format(n.t, 0.5 * scale)
        else:
            out += " S,0,{},,{}\n".format(n.t, 0.35 * scale)

        # Note coloring rules
        out += n_trans(n, z, n_in, False)

        # I don't need to explain it once again, the rules are described above. Overlay rules are the same.
        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
                "taikobigcircleoverlay" if findsetting("UseSkinElements") else "SB/notebig-overlay")
            out += " S,0,{},,{}\n".format(n.t, 0.5 * scale)
        else:
            out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
                "taikohitcircleoverlay" if findsetting("UseSkinElements") else "SB/note-overlay")
            out += " S,0,{},,{}\n".format(n.t, 0.35 * scale)

        # out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
        for w in range(0, freq):
            out += " MX,{},{},{},{},{}\n".format(h_wave_type[0],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))
            out += " MX,{},{},{},{},{}\n".format(h_wave_type[1],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))
        for q in range(freq, 0, -1):
            out += " MY,{},{},{},{},{}\n".format(v_wave_type[0], int(n.t - 60000 / bpm * (q - 0.00) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.25) * freq2), receptor_y,
                                                 receptor_y - amplitude)
            out += " MY,{},{},{},{},{}\n".format(v_wave_type[1], int(n.t - 60000 / bpm * (q - 0.25) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.75) * freq2),
                                                 receptor_y - amplitude,
                                                 receptor_y + amplitude)
            out += " MY,{},{},{},{},{}\n".format(v_wave_type[2], int(n.t - 60000 / bpm * (q - 0.75) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 1.00) * freq2),
                                                 receptor_y + amplitude,
                                                 receptor_y)

        out += n_trans(n, z, n_in, True)
    return out


# Done | Needs R/UD
def visioncone(notes, bpm, cone_angle, freq, z):
    # This mod is centered on a single point.
    d2r_scale = math.pi / 180  # Deg to Radians ratio.
    scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1
    out = ""

    # Get notecount, receptor coordinates, playfield length. Reverse the notes list for the correct draw order.
    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):

        n = notes2[i]  # Current note
        n_in = int(n.t - (60000 / bpm * 4))  # Draw time
        n_hs = Hitsound(n.hs)
        angle = math.sin(n.t / (((60000 / bpm) / math.pi) / freq)) * cone_angle
        angle_rad = angle * d2r_scale  # Convert to radians

        # Similar to the 4 Star mode, we get the original draw points through trig. However, the note rotation is
        # different as it depends of the angle of which it comes from.
        out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
            "taikohitcircle" if findsetting("UseSkinElements") else "SB/note")
        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos(angle_rad)),
                                                 int(receptor_y - pfl * math.sin(angle_rad)),
                                                 receptor_x,
                                                 receptor_y)

        # Finisher scale
        if n_hs.isfinish():
            out += " S,0,{},,{}\n".format(n.t, 0.5 * scale)
        else:
            out += " S,0,{},,{}\n".format(n.t, 0.35 * scale)

        # Note Color
        out += n_trans(n, z, n_in, False)

        # Same rules as normal note
        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
                "taikobigcircleoverlay" if findsetting("UseSkinElements") else "SB/notebig-overlay")
            out += " S,0,{},,{}\n".format(n.t, 0.5 * scale)
        else:
            out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format(
                "taikohitcircleoverlay" if findsetting("UseSkinElements") else "SB/note-overlay")
            out += " S,0,{},,{}\n".format(n.t, 0.35 * scale)

        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos(angle_rad)),
                                                 int(receptor_y - pfl * math.sin(angle_rad)),
                                                 receptor_x,
                                                 receptor_y)
        out += n_trans(n, z, n_in, True)
    return out