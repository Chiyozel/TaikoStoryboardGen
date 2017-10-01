from switchcase import switch
from yumi.utils import isfloat
import sbmods
from sbmods import tweentypes

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
    "Double Scrolling",
    "Brake",
    "Reversed",
    "Negative Scroll",
    "Split",
    "Normal",
    "Upside Down",
    "Boost",
    "Four Star",
    "Vertical Wave",
    "Double V. Wave",
    "Horizontal Wave",
    "Spiral Scroll",
    "Upside Down + Reversed",
    "Vertical Bounce",
    "Compound Scroll",
    "Cone",
    "TanZ (Hidden not applicable)",
    "Clock (Experimental as Rox sucks at making Taiko mods)",
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
            out = sbmods.counters.leftcounterupside(notes)
    return out


def note_mods(y, z, notes, bpm):
    out = ""
    for case2 in switch(y):
        if case2(0):
            d_angle, k_angle = getdonkatangle()
            out = sbmods.allmods.doublescroll(notes, bpm, -d_angle, -k_angle, z)
        if case2(1):
            out = sbmods.allmods.scrolltween(notes, bpm, 1, z)
        if case2(2):
            out = sbmods.allmods.reverse(notes, bpm, z)
        if case2(3):
            out = sbmods.allmods.negascroll(notes, bpm, z)
        if case2(4):
            out = sbmods.allmods.split(notes, bpm, z)
        if case2(5):
            out = sbmods.allmods.normal(notes, bpm, z)
        if case2(6):
            out = sbmods.allmods.upsidedown(notes, bpm, z)
        if case2(7):
            out = sbmods.allmods.scrolltween(notes, bpm, 2, z)
        if case2(8):
            out = sbmods.allmods.star(notes, bpm, z)
        if case2(9):
            amplitude, freq = getamplifreq()
            tweentype = getwavetween()
            out = sbmods.allmods.wave(notes, bpm, tweentype, amplitude, freq, z)
        if case2(10):
            amplitude, freq = getamplifreq()
            tweentype = getwavetween()
            out = sbmods.allmods.doublewave(notes, bpm, tweentype, amplitude, freq, z)
        if case2(11):
            freq = getfreq()
            tweentype = gethwavetween()
            out = sbmods.allmods.horizwave(notes, bpm, tweentype, freq, z)
        if case2(12):
            degoffset = getdegoffset()
            out = sbmods.allmods.spiral(notes, bpm, degoffset, z)
        if case2(13):
            out = sbmods.allmods.upsidedownrev(notes, bpm, z)
        if case2(14):
            amplitude, freq = getamplifreq()
            tweentype = getwavetween()
            out = sbmods.allmods.bounce(notes, bpm, tweentype, amplitude, freq, z)
        if case2(15):
            amplitude, freq = getamplifreq()
            print("-- Horizontal Tween --")
            h_tweentype = gethwavetween()
            print("-- Vertical Tween --")
            v_tweentype = getwavetween()
            out = sbmods.allmods.compound(notes, bpm, h_tweentype, v_tweentype, amplitude, freq, z)
        if case2(16):
            visioncone = getcone()
            freq = getffreq()
            out = sbmods.allmods.visioncone(notes, bpm, visioncone, freq, z)
        if case2(17):
            freq = getfreq()
            out = sbmods.allmods.tanz(notes, bpm, freq, z)
        if case2(18):
            out = sbmods.allmods.clock(notes, bpm, z)
        if case2(19):
            out = sbmods.allmods.wave2(notes, bpm, z)
        if case2(20):
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


def getwavetween():
    tween_str = ""
    for i in range(0, len(tweentypes.vwave)):
        print("{}.\t{}".format(i, tweennumber(tweentypes.vwave[i])))
    print "Enter your tween type:"
    while not tween_str.isdigit():
        tween_str = raw_input(">>>")
    tween = int(tween_str)
    if tween > len(tweentypes.vwave):
        tween = 0
    return tween


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


def gethwavetween():
    tween_str = ""
    for i in range(0, len(tweentypes.hwave)):
        print("{}.\t{}".format(i, tweennumber(tweentypes.hwave[i])))
    print "Enter your tweening method:"
    while not tween_str.isdigit():
        tween_str = raw_input(">>>")
    tween = int(tween_str)
    if tween > len(tweentypes.hwave):
        tween = 0
    return tween


def tweennumber(n):
    out = ""
    for i in range(0, len(n)):
        if i < len(n) - 1:
            out += "{} - ".format(j(n[i]))
        else:
            out += "{}".format(j(n[i]))
    return out


def j(n):
    if n == 0:
        return "Linear"
    elif n == 1:
        return "Decelerate"
    elif n == 2:
        return "Accelerate"
    else:
        return "Unsupported"
