"""
Storyboard Scroll Types
"""

import math

from yumi.utils import findsetting
from yumi.osu.notes.notetype import NoteType
from yumi.osu.notes.hitsound import Hitsound
from yumi.sbmods.tweentypes import hwave as wavetweens
from yumi.sbmods.tweentypes import vwave as wavetypes


def doublescroll(notes, bpm):
    out = ""

    # Double Scroll Black Bar. We only need one additional bar.
    out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
    out += " R,0,{},,1.570796\n".format(notes[0].t)
    out += " F,0,{},{},0,1\n".format(notes[0].t - 500, notes[0].t)
    out += " F,0,{},{},1,0\n".format(notes[-1].t, notes[-1].t + 500)
    out += " M,0,{},,{},{}\n".format(notes[0].t, findsetting("Receptor_X"), findsetting("Receptor_Y") + 20)

    # Get notecount, receptor coordinates, playfield length. Reverse the notes list for the correct draw order.
    notecount = len(notes)
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    # Per note scroll
    for i in range(0, notecount):
        n = notes2[i]  # Current note
        n_in = int(n.t - (60000 / bpm * 4))  # Note gets drawn at this time
        n_type = NoteType(n.note_type)  # Get the Note Type (Slider, Spinner, Circle)
        n_hs = Hitsound(n.hs)  # Get the Hitsound (Don, Kat, Normal, Big)

        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        if n_hs.iskat() or n_type.isspinner():  # Kats and spinners scroll vertically
            out += " MY,0,{},{},{},{}\n".format(n_in, n.t, receptor_y - pfl, receptor_y)
            out += " MX,0,{},{},{}\n".format(n_in, n.t, receptor_x)
        else:  # Dons and roll beginnings scroll horizontally
            out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
            out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x + pfl, receptor_x)

        # Finisher scaling
        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        # Note coloring: Yellow for rolls, grey for spinners, blue for k and red for d
        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,100,160,255\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,255,80,80\n".format(n.t)

        # Overlay element, scrolling rules are the same.
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
    # Tween = the tweening type described above.
    out = ""

    # Get notecount, receptor coordinates, playfield length. Reverse the notes list for the correct draw order.
    notes2 = list(reversed(notes))
    receptor_x = int(findsetting("Receptor_X"))
    receptor_y = int(findsetting("Receptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))
    notecount = len(notes)

    for i in range(0, notecount):
        n = notes2[i]  # Current note
        n_in = int(n.t - (60000 / bpm * 4))  # Drawing time
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        # We put the tween accordingly. 0 will work, but is not the subject of this mod.
        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,{},{},{},{},{}\n".format(tween, n_in, n.t, receptor_x + pfl, receptor_x)

        # Finisher scale rule
        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        # Note color rule
        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,100,160,255\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,255,80,80\n".format(n.t)

        # Overlay scale and movement rules are similar to the note
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

    # Get notecount, receptor coordinates, playfield length. Reverse the notes list for the correct draw order.
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
    # Get notecount, receptor coordinates, playfield length. Reverse the notes list for the correct draw order.
    notecount = len(notes)
    notes2 = list(reversed(notes))
    out = ""
    receptor_x = int(findsetting("ReversedReceptor_X"))
    receptor_y = int(findsetting("UpsideDownReceptor_Y"))
    pfl = int(findsetting("PlayfieldLength"))

    for i in range(0, notecount):
        n = notes2[i]  # Current note
        n_in = int(n.t - (60000 / bpm * 4))  # Draw time
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        # Pretty straightforward. It's just normal scroll but pretty much rotated 180 deg.
        out += "Sprite,Foreground,Centre,\"SB/note.png\",320,240\n"
        out += " MY,0,{},{},{}\n".format(n_in, n.t, receptor_y)
        out += " MX,0,{},{},{},{}\n".format(n_in, n.t, receptor_x - pfl, receptor_x)
        out += " R,0,{},,{}\n".format(n.t, math.pi)

        # Finisher Scale
        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        # Note Color
        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,100,160,255\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,255,80,80\n".format(n.t)

        # Overlay
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
        n_type = NoteType(n.note_type)
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
        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,100,160,255\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,255,80,80\n".format(n.t)

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

    return out


def spiral(notes, bpm, degoffset):
    # This mod is centered on a single point.
    d2r_scale = math.pi / 180  # Deg to Radians ratio.
    out = ""

    # We need like 12 bars to see most of it
    for i in range(0, 180, 15):
        out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
        out += " R,0,{},,{}\n".format(notes[0].t, i * d2r_scale)
        out += " F,0,{},{},0,1\n".format(notes[0].t - 500, notes[0].t)
        out += " F,0,{},{},1,0\n".format(notes[-1].t, notes[-1].t + 500)
        out += " M,0,{},,320,{}\n".format(notes[0].t, int(findsetting("Receptor_Y")))

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
        n_type = NoteType(n.note_type)
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
        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,100,160,255\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,255,80,80\n".format(n.t)

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

    return out


def wave(notes, bpm, wave_type, amplitude, freq):
    freq2 = 4. / freq  # It's actually the period; it's so we can have more periods if the frequency is higher.

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
        n_type = NoteType(n.note_type)
        n_hs = Hitsound(n.hs)

        # Rule: On the X axis, scroll normally. On the Y axis, scroll such that:
        # - Move vertically following the wave tween type provided by the user. Wave tweens are defined in tweentypes.py
        # - Do it freq amount of times. As it is regular, each time will be divided by 4 subtweens.
        # - Amplitude is how big the change is.
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

        # Smaller comment to say finisher scale rules.
        if n_hs.isfinish():
            out += " S,0,{},,0.5\n".format(n.t)
        else:
            out += " S,0,{},,0.35\n".format(n.t)

        # Note coloring rules
        if n_type.isslider():
            out += " C,0,{},,255,200,0\n".format(n.t)
        elif n_hs.iskat():
            out += " C,0,{},,100,160,255\n".format(n.t)
        elif n_type.isspinner():
            out += " C,0,{},,128,128,128\n".format(n.t)
        else:
            out += " C,0,{},,255,80,80\n".format(n.t)

        # I don't need to explain it once again, the rules are described above. Overlay rules are the same.
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
    # We just do twice the simple wave, but the amplitudes are n and -n for better effect.
    out1 = wave(notes, bpm, wave_type, amplitude, freq)
    out2 = wave(notes, bpm, wave_type, -amplitude, freq)
    return "{}\n{}".format(out1, out2)
