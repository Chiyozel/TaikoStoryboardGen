from switchcase import switch

import muma.counters as counters
import muma.note_mods as mods
from muma.sbmods.mod_types import notecounters, scrollingtypes, notealterations


def writelist(n):
    for case in switch(n):
        if case(0):
            w = notecounters
        if case(1):
            w = scrollingtypes
        if case(2):
            w = notealterations
        for x in range(len(w)):
            print("{}.\t{}".format(x + 1, w[x]))

    return w


def sb_counters(y, notes):
    out = ""
    for case2 in switch(y):
        if case2(0):
            left = counters.LeftCounter(notes)
            out = left.make_sb()
        if case2(1):
            right = counters.RightCounter(notes)
            out = right.make_sb()
    return out


def note_mods(y, z, notes, bpm):
    out = ""
    for case2 in switch(y):
        if case2(0):
            normal = mods.ScrollTween(notes, bpm, z)
            out = normal.make_sb()
        if case2(1):
            tweenscroll = mods.ScrollTween(notes, bpm, z)
            tweenscroll.tween_setup()
            out = tweenscroll.make_sb()
        if case2(2):
            angle = mods.AngleScroll(notes, bpm, z)
            out = angle.make_sb()
        if case2(3):
            split = mods.Split(notes, bpm, z)
            out = split.make_sb()
        if case2(4):
            star = mods.Star(notes, bpm, z)
            out = star.make_sb()
        if case2(5):
            wave = mods.VerticalWave(notes, bpm, z)
            out = wave.make_sb()
        if case2(6):
            dwave = mods.DoubleWave(notes, bpm, z)
            out = dwave.make_sb()
        if case2(7):
            hwave = mods.HorizontalWave(notes, bpm, z)
            out = hwave.make_sb()
        if case2(8):
            spiral = mods.Spiral(notes, bpm, z)
            out = spiral.make_sb()
        if case2(9):
            bounce = mods.Bounce(notes, bpm, z)
            out = bounce.make_sb()
        if case2(10):
            axiswave = mods.DoubleAxisWave(notes, bpm, z)
            out = axiswave.make_sb()
        if case2(11):
            visioncone = mods.VisionCone(notes, bpm, z)
            out = visioncone.make_sb()
        if case2(12):
            tanz = mods.TangentZ(notes, bpm, z)
            out = tanz.make_sb()
        if case2(13):
            clock = mods.Clock(notes, bpm, z)
            out = clock.make_sb()
        if case2(14):
            wave2 = mods.StraightSineScroll(notes, bpm, z)
            out = wave2.make_sb()
        if case2(15):
            d_scroll = mods.DoubleScroll(notes, bpm, z)
            out = d_scroll.make_sb()
        if case2(16):
            vib = mods.Vibrate(notes, bpm, z)
            out = vib.make_sb()
    return out


def callmod2(x, y, z, notes, bpm):
    out = ""
    for case in switch(x):
        if case(0):
            out = sb_counters(y, notes)
        if case(1):
            out = note_mods(y, z, notes, bpm)
        if case(2):
            base = mods.TaikoBarBase()
            out = base.make_sb()
    return out
