from switchcase import switch
import sbmods
from sbmods import tweentypes

modtypes = [
    "Note counters...",
    "Scrolling types...",
    "Note alterations...",
    "Note alterations and scrolling types...",
    "Base for SB"
]

notecounters = [
    "Left Side",
    "Right Side",
    "Right Side, Mirrored",
    "Left Side, Upside down"
]

scrollingtypes = [
    "Perpendicular Double Scrolling",
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
    "Upside Down + Reversed"
]

notealterations = [
    "Abekobe",
    "Confusion",
    "Flashlight II (Only colors)",
    "Not Abekobe",
    "Hidden",
    "Hidden II (Only colors)",
]

hybrids = [
    "Reversed Abekobe",
    "Upside down Abekobe",
    "Confusion Vertical Wave",
    "Confusion V. Double Wave",
    "Confusion Horizontal Wave"
]

sbbase = [
    "Create base"
]


def writelist(n):
    for case in switch(n):
        if case(0):
            w = notecounters
        if case(1):
            w = scrollingtypes
        if case(2):
            w = notealterations
        if case(3):
            w = hybrids
        if case(4):
            w = sbbase
        for x in range(len(w)):
            print ("{}.\t{}".format(x + 1, w[x]))

    return w


def callmod(x, y, notes, bpm):
    out = ""
    for case in switch(x):
        if case(0):
            for case2 in switch(y):
                if case2(0):
                    out = sbmods.counters.leftcounter(notes)
                if case2(1):
                    out = sbmods.counters.rightcounter(notes)
                if case2(2):
                    out = sbmods.counters.rightcountermirror(notes)
                if case2(3):
                    out = sbmods.counters.leftcounterupside(notes)
        if case(1):
            for case2 in switch(y):
                if case2(0):
                    out = sbmods.scrolls.doublescroll(notes, bpm)
                if case2(1):
                    out = sbmods.scrolls.scrolltween(notes, bpm, 1)
                if case2(2):
                    out = sbmods.scrolls.reverse(notes, bpm)
                if case2(3):
                    out = sbmods.scrolls.negascroll(notes, bpm)
                if case2(4):
                    out = sbmods.scrolls.split(notes, bpm)
                if case2(5):
                    out = sbmods.scrolls.normal(notes, bpm)
                if case2(6):
                    out = sbmods.scrolls.upsidedown(notes, bpm)
                if case2(7):
                    out = sbmods.scrolls.scrolltween(notes, bpm, 2)
                if case2(8):
                    out = sbmods.scrolls.star(notes, bpm)
                if case2(9):
                    amplitude, freq = getamplifreq()
                    tweentype = getwavetween()
                    out = sbmods.scrolls.wave(notes, bpm, tweentype, amplitude, freq)
                if case2(10):
                    amplitude, freq = getamplifreq()
                    tweentype = getwavetween()
                    out = sbmods.scrolls.doublewave(notes, bpm, tweentype, amplitude, freq)
                if case2(11):
                    freq = getfreq()
                    tweentype = gethwavetween()
                    out = sbmods.scrolls.horizwave(notes, bpm, tweentype, freq)
                if case2(12):
                    degoffset = getdegoffset()
                    out = sbmods.scrolls.spiral(notes, bpm, degoffset)
                if case2(13):
                    out = sbmods.scrolls.upsidedownrev(notes, bpm)
        if case(2):
            for case2 in switch(y):
                if case2(0):
                    out = sbmods.transformations.abekobe(notes, bpm)
                if case2(1):
                    out = sbmods.transformations.confusion(notes, bpm)
                if case2(2):
                    out = sbmods.transformations.flashlight(notes, bpm)
                if case2(3):
                    out = sbmods.transformations.abekoreset(notes, bpm)
                if case2(4):
                    out = sbmods.transformations.hidden(notes, bpm)
                if case2(5):
                    out = sbmods.transformations.hidden2(notes, bpm)
        if case(3):
            for case2 in switch(y):
                if case2(0):
                    out = sbmods.hybrids.reverseabekobe(notes, bpm)
                if case2(1):
                    out = sbmods.hybrids.upsidedownabekobe(notes, bpm)
                if case2(2):
                    amplitude, freq = getamplifreq()
                    tweentype = getwavetween()
                    out = sbmods.hybrids.waveconfusion(notes, bpm, tweentype, amplitude, freq)
                if case2(3):
                    amplitude, freq = getamplifreq()
                    tweentype = getwavetween()
                    out = sbmods.hybrids.doublewaveconfusion(notes, bpm, tweentype, amplitude, freq)
                if case2(4):
                    freq = getfreq()
                    tweentype = gethwavetween()
                    out = sbmods.hybrids.hwaveconfusion(notes, bpm, tweentype, freq)
        if case(4):
            for case2 in switch(y):
                if case2(0):
                    out = sbmods.base.createbase()
    return out


def getamplifreq():
    amplitude = float(raw_input("Enter the intensity of the wave: >>>")) * 25
    freq = int(round(float(raw_input("Enter the frequency of the wave: >>>")), 1))

    return amplitude, freq


def getfreq():
    freq = int(round(float(raw_input("Enter the frequency of the wave: >>>")), 1))

    return freq


def getwavetween():
    for i in range(0, len(tweentypes.vwave)):
        print("{}.\t{}".format(i, tweennumber(tweentypes.vwave[i])))
    tween = int(raw_input("Enter your tween type: >>>"))
    if tween > len(tweentypes.vwave):
        tween = 0
    return tween


def getdegoffset():
    angle = int(raw_input("Enter your angle offset (in deg) >>>"))
    if angle >= 360:
        angle %= 360
    return angle


def gethwavetween():
    for i in range(0, len(tweentypes.hwave)):
        print("{}.\t{}".format(i, tweennumber(tweentypes.hwave[i])))
    tween = int(raw_input("Enter your tween type: >>>"))
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
