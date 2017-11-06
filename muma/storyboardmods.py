import muma.modstypes as modstypes
import muma.sbmods.mod_types
from muma import utils
import sys


class StoryboardMods:
    def __init__(self, notelist):
        self.notes = notelist
        self.scroll = None
        self.dostoryboard()

    def dostoryboard(self):
        confirmation = ""
        notes_sb = None

        while confirmation.lower() != "y":
            notes_sb = []
            beginning_str = end_str = bpm_str = ""

            print("Beginning of the SB Mod:")
            while not beginning_str.isdigit():
                beginning_str = input(">>>")
            beginning = int(beginning_str)

            print("End of the SB Mod:")
            while not end_str.isdigit():
                end_str = input(">>>")
            end = int(end_str)

            if beginning > end:
                end, beginning = beginning, end

            for n in self.notes:
                if beginning <= n.t < end:
                    notes_sb = notes_sb + [n]

            print("Scrolling speed (BPM x Green SV):")
            while not utils.isfloat(bpm_str):
                bpm_str = input(">>>")
            self.scroll = float(bpm_str)

            print(
                "The current section spans from {}ms to {}ms, and has {} notes.".format(beginning, end, len(notes_sb)))
            print("The notes will scroll at {} BPM.".format(self.scroll))
            confirmation = input("Would you like to continue? 'y' to continue, 'q' to quit, other to restart. ")
            if confirmation.lower() == 'q':
                sys.exit()

        self.choices(notes_sb)

    def choices(self, notessb):
        print("What do you want to do? - 'q' to exit")
        n = 1
        y = z = 0

        for x in muma.sbmods.mod_types.modtypes:
            print ("{}.\t{}".format(n, x))
            n += 1

        while True:
            while True:
                choice_str = input(">>>")
                if choice_str.lower() == "q":
                    sys.exit()
                elif choice_str.isdigit():
                    choice = int(choice_str)
                    break
            if 1 <= choice <= len(muma.sbmods.mod_types.modtypes):
                break

        if choice != 3:
            modslist = modstypes.writelist(choice - 1)
            while True:
                while True:
                    y_str = input(">>>")
                    if y_str.lower() == "q":
                        sys.exit()
                    elif y_str.isdigit():
                        y = int(y_str)
                        break
                if 1 <= y <= len(modslist):
                    break
            if choice == 2:
                mods2list = modstypes.writelist(2)
                while True:
                    while True:
                        z_str = input(">>>")
                        if z_str.lower() == 'q':
                            sys.exit()
                        elif z_str.isdigit():
                            z = int(z_str)
                            break
                    if 1 <= z <= len(mods2list):
                        break

        out = modstypes.callmod2(choice - 1, y - 1, z - 1, notessb, self.scroll)

        utils.writetofile(out)

        continue_sb = input("Do you want to continue? 'y' to continue, other to quit.")
        if continue_sb == 'y':
            self.dostoryboard()
