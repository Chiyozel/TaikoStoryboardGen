import ModsUtils
from switchcase import switch

ModTypes = [
    "Note Counters...",
    "Scrolling types...",
    "Note alterations...",
    "Note alterations and scrolling types...",
    "Base for SB"
]

NoteCounters = [
    "Left Side",
    "Right Side",
    "Right Side, Mirrored",
    "Left Side, Upside down"
]

ScrollingTypes = [
    "Perpendicular Double Scrolling",
    "Brake",
    "Reversed",
    "Negative Scroll",
    "Split",
    "Normal",
    "Upside Down",
    "Boost",
    "Four Star",
    "Wave Type I",
    "Double Wave Type I",
    "Wave Type II",
    "Double Wave Type II"
]

NoteAlterations = [
    "Abekobe",
    "Confusion",
    "Flashlight II"
]

Hybrids = [
    "Reversed Abekobe",
    "Upside down Abekobe",
    "Confusion Wave I",
    "Confusion Double Wave I"
]

SBBase = [
    "Create Base"
]


def writeList(n):
    for case in switch(n):
        if case(0):
            w = NoteCounters
        if case(1):
            w = ScrollingTypes
        if case(2):
            w = NoteAlterations
        if case(3):
            w = Hybrids
        if case(4):
            w = SBBase
        for x in range(len(w)):
            print ("{}.\t{}".format(x + 1, w[x]))

    return w


def callMod(x, y, notes, bpm):
    for case in switch(x):
        if case(0):
            for case2 in switch(y):
                if case2(0):
                    out = ModsUtils.Counters.leftcounter(notes)
                if case2(1):
                    out = ModsUtils.Counters.rightcounter(notes)
                if case2(2):
                    out = ModsUtils.Counters.rightcountermirror(notes)
                if case2(3):
                    out = ModsUtils.Counters.leftcounterupside(notes)
        if case(1):
            for case2 in switch(y):
                if case2(0):
                    out = ModsUtils.Scrolls.doublescroll(notes, bpm)
                if case2(1):
                    out = ModsUtils.Scrolls.brake(notes, bpm)
                if case2(2):
                    out = ModsUtils.Scrolls.reverse(notes, bpm)
                if case2(3):
                    out = ModsUtils.Scrolls.negascroll(notes, bpm)
                if case2(4):
                    out = ModsUtils.Scrolls.split(notes, bpm)
                if case2(5):
                    out = ModsUtils.Scrolls.normal(notes, bpm)
                if case2(6):
                    out = ModsUtils.Scrolls.upsidedown(notes, bpm)
                if case2(7):
                    out = ModsUtils.Scrolls.boost(notes, bpm)
                if case2(8):
                    out = ModsUtils.Scrolls.star(notes, bpm)
                if case2(9):
                    out = ModsUtils.Scrolls.wave1(notes, bpm)
                if case2(10):
                    out = ModsUtils.Scrolls.dwave1(notes, bpm)
                if case2(11):
                    out = ModsUtils.Scrolls.wave2(notes, bpm)
                if case2(12):
                    out = ModsUtils.Scrolls.dwave2(notes, bpm)
        if case(2):
            for case2 in switch(y):
                if case2(0):
                    out = ModsUtils.Transformations.abekobe(notes)
                if case2(1):
                    out = ModsUtils.Transformations.confusion(notes)
                if case2(2):
                    out = ModsUtils.Transformations.flashlight(notes)
        if case(3):
            for case2 in switch(y):
                if case2(0):
                    out = ModsUtils.Hybrids.reverseabekobe(notes, bpm)
                if case2(1):
                    out = ModsUtils.Hybrids.upsidedownabekobe(notes, bpm)
                if case2(2):
                    out = ModsUtils.Hybrids.waveconfusion(notes, bpm)
                if case2(3):
                    out = ModsUtils.Hybrids.doublewaveconfusion(notes, bpm)
        if case(4):
            for case2 in switch(y):
                if case2(0):
                    out = ModsUtils.Base.createbase()
    return out
