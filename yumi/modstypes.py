from switchcase import switch
import sbmods

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
    "Sine Wave",
    "Double Sine Wave",
    "Inverted Sine Wave",
    "Double Invert Sine Wave",
    "Triangle Wave",
    "Double Triangle Wave",
]

notealterations = [
    "Abekobe",
    "Confusion",
    "Flashlight II"
]

hybrids = [
    "Reversed Abekobe",
    "Upside down Abekobe",
    "Confusion Wave I",
    "Confusion Double Wave I"
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
                    out = sbmods.scrolls.brake(notes, bpm)
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
                    out = sbmods.scrolls.boost(notes, bpm)
                if case2(8):
                    out = sbmods.scrolls.star(notes, bpm)
                if case2(9):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.wave(notes, bpm, 0, amplitude, freq)
                if case2(10):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.doublewave(notes, bpm, 0, amplitude, freq)
                if case2(11):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.wave(notes, bpm, 1, amplitude, freq)
                if case2(12):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.doublewave(notes, bpm, 1, amplitude, freq)
                if case2(13):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.wave(notes, bpm, 2, amplitude, freq)
                if case2(14):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.doublewave(notes, bpm, 2, amplitude, freq)
                if case2(15):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.wave(notes, bpm, 3, amplitude, freq)
                if case2(16):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.doublewave(notes, bpm, 3, amplitude, freq)
                if case2(17):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.wave(notes, bpm, 4, amplitude, freq)
                if case2(18):
                    amplitude, freq = getamplifreq()
                    out = sbmods.scrolls.doublewave(notes, bpm, 4, amplitude, freq)
        if case(2):
            for case2 in switch(y):
                if case2(0):
                    out = sbmods.transformations.abekobe(notes)
                if case2(1):
                    out = sbmods.transformations.confusion(notes)
                if case2(2):
                    out = sbmods.transformations.flashlight(notes)
        if case(3):
            for case2 in switch(y):
                if case2(0):
                    out = sbmods.hybrids.reverseabekobe(notes, bpm)
                if case2(1):
                    out = sbmods.hybrids.upsidedownabekobe(notes, bpm)
                if case2(2):
                    out = sbmods.hybrids.waveconfusion(notes, bpm)
                if case2(3):
                    out = sbmods.hybrids.doublewaveconfusion(notes, bpm)
        if case(4):
            for case2 in switch(y):
                if case2(0):
                    out = sbmods.base.createbase()
    return out


def getamplifreq():
    amplitude = float(raw_input("Enter the intensity of the wave: >>>")) * 25
    freq = int(round(float(raw_input("Enter the frequency of the wave: >>>")), 1))

    return amplitude, freq
