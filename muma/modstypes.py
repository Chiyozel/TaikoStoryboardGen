import sys

from switchcase import switch

import sbmods
import muma.note_mods as mods
from sbmods import tweentypes
from muma.utils import isfloat

modtypes = [
    "Note counters...",
    "Note alterations and scrolling types...",
    "Create SB base"
]

notecounters = [
    "Left Side",
    "Right Side",
    "Right Side, Mirrored",
    "Left Side, Upside down"
]

scrollingtypes = [
    "Normal V2",
    "Tweened Scroll V2",
    "Double Scrolling",
    "----",
    "----",
    "Split V2",
    "----",
    "Four Star",
    "Vertical Wave",
    "Double V. Wave",
    "Horizontal Wave",
    "Spiral Scroll",
    "----",
    "Vertical Bounce V2",
    "Compound Scroll",
    "Cone",
    "TanZ (Hidden not applicable)",
    "Clock V2",
    "Receptor Wave",
    "Angled Scroll",
]

notealterations = [
    "None",
    "Abekobe",
    "Confusion",
    "Flashlight II (Only colors)",
    "Not Abekobe",
    "Hidden",
    "Hidden II (Only colors)",
    "Monochrome (tasuke912)",
]


def writelist(n):
    for case in switch(n):
        if case(0):
            w = notecounters
        if case(1):
            w = scrollingtypes
        if case(2):
            w = notealterations
        for x in range(len(w)):
            print ("{}.\t{}".format(x + 1, w[x]))

    return w


def sb_counters(y, notes):
    out = ""
    for case2 in switch(y):
        if case2(0):
            out = sbmods.counters.leftcounter(notes)
        if case2(1):
            out = sbmods.counters.rightcounter(notes)
        if case2(2):
            out = sbmods.counters.rightcountermirror(notes)
        if case2(3):
            out = sbmods.counters.upsidemirrorright(notes)
    return out


def note_mods(y, z, notes, bpm):
    out = ""
    for case2 in switch(y):
        if case2(0):
            normal = mods.ScrollTween(notes, bpm, z)
            out = normal.make_sb()

        if case2(1):
            tween = getwavetween(1)[0]
            tweenscroll = mods.ScrollTween(notes, bpm, z, tween)
            out = tweenscroll.make_sb()

        if case2(2):
            d_angle, k_angle = getdonkatangle()
            out = sbmods.allmods.doublescroll(notes, bpm, -d_angle, -k_angle, z)
        if case2(3):
            pass
        if case2(4):
            pass
        if case2(5):
            split = mods.Split(notes, bpm, z)
            out = split.make_sb()
        if case2(6):
            pass
        if case2(7):
            out = sbmods.allmods.star(notes, bpm, z)
        if case2(8):
            wave = mods.VerticalWave(notes, bpm, z)
            out = wave.make_sb()

        if case2(9):
            dwave = mods.DoubleWave(notes, bpm, z)
            out = dwave.make_sb()

        if case2(10):
            freq = getfreq()
            tweentype = getwavetween(2)
            out = sbmods.allmods.horizwave(notes, bpm, tweentype, freq, z)
        if case2(11):
            degoffset = getdegoffset()
            out = sbmods.allmods.spiral(notes, bpm, degoffset, z)
        if case2(12):
            pass
        if case2(13):
            bounce = mods.Bounce(notes, bpm, z)
            out = bounce.make_sb()

        if case2(14):
            amplitude, freq = getamplifreq()
            print("-- Horizontal Tween --")
            h_tweentype = getwavetween(2)
            print("-- Vertical Tween --")
            v_tweentype = getwavetween(3)
            out = sbmods.allmods.compound(notes, bpm, h_tweentype, v_tweentype, amplitude, freq, z)
        if case2(15):
            visioncone = getcone()
            freq = getffreq()
            out = sbmods.allmods.visioncone(notes, bpm, visioncone, freq, z)
        if case2(16):
            freq = getfreq()
            out = sbmods.allmods.tanz(notes, bpm, freq, z)
        if case2(17):
            clock = mods.Clock(notes, bpm, z)
            out = clock.make_sb()

        if case2(18):
            out = sbmods.allmods.wave2(notes, bpm, z)
        if case2(19):
            angle = getangle()
            out = sbmods.allmods.anglescroll(notes, bpm, angle, z)
    return out


def callmod2(x, y, z, notes, bpm):
    out = ""
    for case in switch(x):
        if case(0):
            out = sb_counters(y, notes)
        if case(1):
            out = note_mods(y, z, notes, bpm)
        if case(2):
            out = sbmods.base.createbase()
    return out


def getamplifreq():
    a_str = f_str = ""

    while not (isfloat(a_str) and f_str.isdigit()):
        a_str = raw_input("Enter the intensity: >>>")
        f_str = raw_input("Enter the frequency (Integer only): >>>")

    amplitude = float(a_str) * 25
    freq = int(f_str)

    return amplitude, freq


def getdonkatangle():
    da_str = ka_str = ""

    while not (isfloat(da_str) and isfloat(da_str)):
        da_str = raw_input("Enter the Don scroll angle: >>>")
        ka_str = raw_input("Enter the Kat scroll angle: >>>")

    d_angle = float(da_str)
    k_angle = float(ka_str)

    return d_angle, k_angle


def getangle():
    a_str = ""

    while not isfloat(a_str):
        a_str = raw_input("Enter the Scroll angle: >>>")

    angle = float(a_str)

    return angle


def getfreq():
    frq_str = ""
    print "Enter the frequency (Integer only):"
    while not frq_str.isdigit():
        frq_str = raw_input(">>>")
    freq = int(frq_str)

    return freq


def getffreq():
    frq_str = ""
    print "Enter the frequency (Decimal allowed):"
    while not isfloat(frq_str):
        frq_str = raw_input(">>>")
    freq = float(frq_str)

    return freq


def getwavetween(ntweens):
    arr_tween = []
    tween_str = ""
    x = 1
    for i in range(0, len(tweentypes.tweens), 5):
        for offset in range(0, 5):
            sys.stdout.write("{}   |   ".format(tweentypes.tweens[i + offset]))
        print("")
    while not x > ntweens:
        print "Enter tween type {} ".format(x)
        while not (tween_str.isdigit() and 0 <= int(tween_str) <= 34):
            tween_str = raw_input(">>>")
        arr_tween.append(int(tween_str))
        tween_str = ""
        x += 1
    return arr_tween


def getdegoffset():
    ang_str = ""
    print "Enter your angle offset (in deg):"
    while not ang_str.isdigit():
        ang_str = raw_input(">>>")
    angle = int(ang_str)
    if angle >= 360:
        angle %= 360
    return angle


def getcone():
    ang_str = ""
    print "Enter your cone angle (in deg):"
    while not ang_str.isdigit():
        ang_str = raw_input(">>>")
    angle = int(ang_str)
    if angle >= 360:
        angle %= 360
    return angle