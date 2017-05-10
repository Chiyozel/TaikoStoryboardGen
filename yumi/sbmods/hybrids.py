import math
import random

from yumi.osu.notes.hitsound import Hitsound
from yumi.osu.notes.notetype import NoteType
from yumi.utils import findsetting
from yumi.sbmods.tweentypes import hwave as wavetweens
from yumi.sbmods.tweentypes import vwave as wavetypes


def reverseabekobe(notes, bpm):
    out = ""
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("ReversedReceptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))
    notecount = len(notes)

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x - pfl, receptor_x)

        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,255,80,80\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,100,160,255\n".format(n.t)

        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)

        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x - pfl, receptor_x)

    return out


def upsidedownabekobe(notes, bpm):
    out = ""
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("UpsideDownReceptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))
    notecount = len(notes)

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
        out += " R,0,{},,{}\n".format(n.t, math.pi)

        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,255,80,80\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,100,160,255\n".format(n.t)

        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)

        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
        out += " R,0,{},,{}\n".format(n.t, math.pi)
    return out


def waveconfusion(notes, bpm, wave_type, amplitude, freq):
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
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        n_x = int((n.t - n_in) / 4)

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
            out += " C,0,{},{},{},{},{},255,200,0\n".format(n_in + n_x, n.t - n_x, red, green, blue)
        elif n_hs.iskat():
            out += " C,0,{},{},{},{},{},100,160,255\n".format(n_in + n_x, n.t - n_x, red, green, blue)
        elif n_type.isspinner():
            out += " C,0,{},{},{},{},{},128,128,128\n".format(n_in + n_x, n.t - n_x, red, green, blue)
        else:
            out += " C,0,{},{},{},{},{},255,80,80\n".format(n_in + n_x, n.t - n_x, red, green, blue)

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


def doublewaveconfusion(notes, bpm, wave_type, amplitude, freq):
    out1 = waveconfusion(notes, bpm, wave_type, amplitude, freq)
    out2 = waveconfusion(notes, bpm, wave_type, -amplitude, freq)
    return "{}\n{}".format(out1, out2)


def hwaveconfusion(notes, bpm, tween, freq):
    out = ""
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))
    notecount = len(notes)

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)
        n_st = n.t - n_in
        n_x = int((n.t - n_in) / 4)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)

        for w in range(0, freq):
            out += " MX,{},{},{},{},{}\n".format(wavetweens[tween][0],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))
            out += " MX,{},{},{},{},{}\n".format(wavetweens[tween][1],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))

        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        if n_type.isslider():
            out += " C,0,{},{},{},{},{},255,200,0\n".format(n_in + n_x, n.t - n_x, red, green, blue)
        elif n_hs.iskat():
            out += " C,0,{},{},{},{},{},100,160,255\n".format(n_in + n_x, n.t - n_x, red, green, blue)
        elif n_type.isspinner():
            out += " C,0,{},{},{},{},{},128,128,128\n".format(n_in + n_x, n.t - n_x, red, green, blue)
        else:
            out += " C,0,{},{},{},{},{},255,80,80\n".format(n_in + n_x, n.t - n_x, red, green, blue)

        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)

        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        for w in range(0, freq):
            out += " MX,{},{},{},{},{}\n".format(wavetweens[tween][0],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))
            out += " MX,{},{},{},{},{}\n".format(wavetweens[tween][1],
                                                 n_in + w * n_st / freq,
                                                 n_in + (w + 1) * n_st / freq,
                                                 receptor_x + pfl - (w * pfl / freq),
                                                 receptor_x + pfl - ((w + 1) * pfl / freq))

    return out
