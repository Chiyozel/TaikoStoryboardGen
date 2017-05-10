import math

from yumi.utils import findsetting
from yumi.osu.notes.notetype import NoteType
from yumi.osu.notes.hitsound import Hitsound
from yumi.sbmods.tweentypes import hwave as wavetweens
from yumi.sbmods.tweentypes import vwave as wavetypes


# TODO Add Comments once everything is finished


def doublescroll(notes, bpm):
    out = ""

    # Double Scroll Black Bar
    out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
    out += " R,0,{},,1.570796\n".format(notes[0].t)
    out += " F,0,{},{},0,1\n".format(notes[0].t - 500, notes[0].t)
    out += " F,0,{},{},1,0\n".format(notes[-1].t, notes[-1].t + 500)
    out += " M,0,{},,{},{}\n".format(notes[0].t, findsetting("Receptor_X"), findsetting("Receptor_Y") + 20)

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


def scrolltween(notes, bpm, tween):
    # 1 = Brake, 2 = Boost
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

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,{},{},{},{},{}\n".format(tween, n_in, n.t, receptor_x + pfl, receptor_x)

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
        out += " MX,{},{},{},{},{}\n".format(tween, n_in, n.t, receptor_x + pfl, receptor_x)

    return out


def horizwave(notes, bpm, tween, freq):
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


def reverse(notes, bpm):
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
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x - pfl, receptor_x)

    return out


def negascroll(notes, bpm):
    out = ""
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(int(findsetting("PlayfieldLength")) / 3.5)
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
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x - pfl, receptor_x)

    return out


def split(notes, bpm):
    out = ""

    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = 320
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(int(findsetting("PlayfieldLength")) / 1.5)

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        if n_hs.iskat() or n_type.isspinner():
            out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x - pfl, receptor_x)
        else:
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
        if n_hs.iskat() or n_type.isspinner():
            out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x - pfl, receptor_x)
        else:
            out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)

    return out


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
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("UpsideDownReceptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

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


def upsidedownrev(notes, bpm):
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("ReversedReceptor_X"))
    receptor_y = int(findsetting("UpsideDownReceptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x - pfl, receptor_x)
        out += " R,0,{},,{}\n".format(n.t, math.pi)

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
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x - pfl, receptor_x)
    return out


def star(notes, bpm):
    out = ""

    # Four Star Black Bars (Hidden by default)
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

    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = 320
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = 500
    rot_i = [0, 3, 4, 1]

    for i in range(0, notecount):
        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 4))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)
        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos((i % 4) * math.pi / 4)),
                                                 int(receptor_y - pfl * math.sin((i % 4) * math.pi / 4)),
                                                 receptor_x,
                                                 receptor_y)  # 500, 0
        out += " R,0,{},,{}\n".format(n.t, (rot_i[i % 4]) * math.pi / 4)

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
        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos((i % 4) * math.pi / 4)),
                                                 int(receptor_y - pfl * math.sin((i % 4) * math.pi / 4)),
                                                 receptor_x,
                                                 receptor_y)
        out += " R,0,{},,{}\n".format(n.t, (rot_i[i % 4]) * math.pi / 4)

    return out


def spiral(notes, bpm, degoffset):
    # This mod is centered on a single point
    d2r_scale = math.pi / 180
    out = ""

    # All Bars:
    for i in range(0, 180, 15):
        out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
        out += " R,0,{},,{}\n".format(notes[0].t, i * d2r_scale)
        out += " F,0,{},{},0,1\n".format(notes[0].t - 500, notes[0].t)
        out += " F,0,{},{},1,0\n".format(notes[-1].t, notes[-1].t + 500)
        out += " M,0,{},,320,{}\n".format(notes[0].t, int(findsetting("Receptor_Y")))

    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = 320
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = 500

    for i in range(0, notecount):
        angle = (i * degoffset) % 360
        angle_rad = angle * d2r_scale

        n = notes2[i]
        n_in = int(n.t - (60000 / bpm * 8))
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)
        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos(angle_rad)),
                                                 int(receptor_y - pfl * math.sin(angle_rad)),
                                                 receptor_x,
                                                 receptor_y)  # 500, 0
        out += " R,0,{},,{}\n".format(n.t, angle_rad)

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
        out += " M,0,{},{},{},{},{},{}\n".format(n_in,
                                                 n.t,
                                                 int(receptor_x + pfl * math.cos(angle_rad)),
                                                 int(receptor_y - pfl * math.sin(angle_rad)),
                                                 receptor_x,
                                                 receptor_y)
        out += " R,0,{},,{}\n".format(n.t, angle_rad)

    return out


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
