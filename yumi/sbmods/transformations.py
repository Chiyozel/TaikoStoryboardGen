import math
import random

from yumi.utils import findsetting
from yumi.osu.notes.notetype import NoteType
from yumi.osu.notes.hitsound import Hitsound


def abekobe(notes, bpm):
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
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
    return out


def confusion(notes, bpm):
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_x = int((n.t - n_in) / 4)
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)

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
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
    return out


def abekoreset(notes, bpm):
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_x = int((n.t - n_in) / 8)
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
            out += " C,0,{},{},255,80,80,100,160,255\n".format(n_in + 4*n_x, n.t - 2*n_x)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n_in)
        else:
            out += " C,0,{},{},100,160,255,255,80,80\n".format(n_in + 4*n_x, n.t - 2*n_x)

        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)

        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
    return out


def flashlight(notes, bpm):
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_x = int((n.t - n_in) / 8)
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
            out += " C,0,{},{},0,0,0,255,200,0\n".format(n_in + 5 * n_x, n.t - 2 * n_x)
        elif n_hs.iskat():
            out += " C,0,{},{},0,0,0,100,160,255\n".format(n_in + 5 * n_x, n.t - 2 * n_x)
        elif n_type.isspinner():
            out += " C,0,{},{},0,0,0,128,128,128\n".format(n_in + 5 * n_x, n.t - 2 * n_x)
        else:
            out += " C,0,{},{},0,0,0,255,80,80\n".format(n_in + 5 * n_x, n.t - 2 * n_x)

        if n_hs.isfinish():
            out += "Sprite,Foreground,Centre,\"SB/notebig-overlay.png\",320,240\n"
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += "Sprite,Foreground,Centre,\"SB/note-overlay.png\",320,240\n"
            out += " S,0,{},,0.35\n".format(n.t)

        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
    return out


def hidden(notes, bpm):
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)
        n_x = int((n.t - n_in) / 8)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
        out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
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
        out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
    return out


def hidden2(notes, bpm):
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)
        n_x = int((n.t - n_in) / 4)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)
        out += " F,0,{},{},1,0\n".format(n_in + n_x, n.t - n_x)
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
