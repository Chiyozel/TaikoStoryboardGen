from yumi.utils import findsetting
from yumi.osu.notes.notetype import NoteType
from yumi.osu.notes.hitsound import Hitsound

# TODO Add Comments once everything is finished

wavetypes = [
    [1, 2, 1, 2],   # Sin
    [2, 1, 2, 1],   # Inv. Sin
    [0, 0, 0, 0],   # Triangle
]


def doublescroll(notes, bpm):
    out = ""

    # Double Scroll Black Bar
    out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
    out += " R,0,{},,1.570796\n".format(notes[0].t)
    out += " F,0,{},{},0,1\n".format(notes[0].t - 500, notes[0].t)
    out += " F,0,{},{},1,0\n".format(notes[-1].t, notes[-1].t + 500)
    out += " M,0,{},,{},390\n".format(notes[0].t, findsetting("Receptor_X"))

    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        if n_hs.iskat() or n_type.isspinner():
            out += " MY,0,{},{},{},{}\n".format(n_in, n.t, receptor_y - pfl, receptor_y)
            out += " MX,0,{},{},{}\n".format(n_in, n.t, receptor_x)
        else:
            out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
            out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)

        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,100,160,255\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,255,80,80\n".format(n.t)

        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)
        if n_hs.iskat() or n_type.isspinner():
            out += " MY,0,{},{},{},{}\n".format(n_in, n.t, receptor_y - pfl, receptor_y)
            out += " MX,0,{},{},{}\n".format(n_in, n.t, receptor_x)
        else:
            out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
            out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)

    return out


def brake(notes, bpm):
    pass


def reverse(notes, bpm):
    pass


def negascroll(notes, bpm):
    pass


def split(notes, bpm):
    pass


def normal(notes, bpm):
    speed = max(float(raw_input("Scroll speed multiplier: >>>")), 0.01)
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * (4 / speed)))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)

        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,100,160,255\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,255,80,80\n".format(n.t)

        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)

        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
    return out


def upsidedown(notes, bpm):
    pass


def boost(notes, bpm):
    pass


def star(notes, bpm):
    pass


def wave(notes, bpm, wave_type, amplitude, freq):
    freq2 = 4. / freq

    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    out = ""

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
        for q in range(freq, 0, -1):
            out += " MY,{},{},{},{},{}\n".format(wavetypes[wave_type][0], int(n.t - 60000 / bpm * (q - 0.00) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.25) * freq2), receptor_y,
                                                 receptor_y - amplitude)
            out += " MY,{},{},{},{},{}\n".format(wavetypes[wave_type][1], int(n.t - 60000 / bpm * (q - 0.25) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.50) * freq2), receptor_y - amplitude,
                                                 receptor_y)
            out += " MY,{},{},{},{},{}\n".format(wavetypes[wave_type][2], int(n.t - 60000 / bpm * (q - 0.50) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.75) * freq2), receptor_y,
                                                 receptor_y + amplitude)
            out += " MY,{},{},{},{},{}\n".format(wavetypes[wave_type][3], int(n.t - 60000 / bpm * (q - 0.75) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 1.00) * freq2), receptor_y + amplitude,
                                                 receptor_y)
        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,100,160,255\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,255,80,80\n".format(n.t)

        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)

        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)

        for q in range(freq, 0, -1):
            out += " MY,{},{},{},{},{}\n".format(wavetypes[wave_type][0], int(n.t - 60000 / bpm * (q - 0.00) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.25) * freq2), receptor_y,
                                                 receptor_y - amplitude)
            out += " MY,{},{},{},{},{}\n".format(wavetypes[wave_type][1], int(n.t - 60000 / bpm * (q - 0.25) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.50) * freq2),
                                                 receptor_y - amplitude,
                                                 receptor_y)
            out += " MY,{},{},{},{},{}\n".format(wavetypes[wave_type][2], int(n.t - 60000 / bpm * (q - 0.50) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 0.75) * freq2), receptor_y,
                                                 receptor_y + amplitude)
            out += " MY,{},{},{},{},{}\n".format(wavetypes[wave_type][3], int(n.t - 60000 / bpm * (q - 0.75) * freq2),
                                                 int(n.t - 60000 / bpm * (q - 1.00) * freq2),
                                                 receptor_y + amplitude,
                                                 receptor_y)

    return out


def doublewave(notes, bpm, wave_type, amplitude, freq):
    out1 = wave(notes, bpm, wave_type, amplitude, freq)
    out2 = wave(notes, bpm, wave_type, -amplitude, freq)
    return "{}\n{}".format(out1, out2)
