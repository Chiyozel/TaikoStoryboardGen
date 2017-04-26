from Note import Note
from NoteType import NoteType


def istaiko(f):
    f2 = open(f, "r")
    for line in f2:
        if "Mode: 1\n" in line:
            return True
    return False


def listnotes(f):
    f2 = open(f, 'r')
    notes = []

    # We gotta do this kinda shit mate, but lazy to find a better alternative lol
    for line in f2:
        if line == "[HitObjects]\n":
            break

    # Time to get the notes going
    for line in f2:
        stuff = line.split(",")
        params = "0:0:0:0:" if len(stuff) < 6 else stuff[5]

        # We check the note type, as a spinner has a different argument list
        ntype = NoteType(int(stuff[3]))

        if ntype.isspinner():
            note = Note(int(stuff[0]), int(stuff[1]), int(stuff[2]), int(stuff[3]), int(stuff[4]), params)
        elif ntype.isslider():
            note = Note(int(stuff[0]), int(stuff[1]), int(stuff[2]), int(stuff[3]), int(stuff[4]), params)
        else:
            note = Note(int(stuff[0]), int(stuff[1]), int(stuff[2]), int(stuff[3]), int(stuff[4]), params)

        # Adding the note to the list
        notes = notes + [note]

    return notes
