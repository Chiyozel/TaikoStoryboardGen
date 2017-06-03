import modstypes
from yumi import utils
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
                beginning_str = raw_input(">>>")
            beginning = int(beginning_str)

            print("End of the SB Mod:")
            while not end_str.isdigit():
                end_str = raw_input(">>>")
            end = int(end_str)

            if beginning > end:
                end, beginning = beginning, end

            for n in self.notes:
                if beginning <= n.t < end:
                    notes_sb = notes_sb + [n]

            print("Scrolling speed (BPM x Green SV):")
            while not utils.isfloat(bpm_str):
                bpm_str = raw_input(">>>")
            self.scroll = float(bpm_str)

            print(
                "The current section spans from {}ms to {}ms, and has {} notes.".format(beginning, end, len(notes_sb)))
            print("The notes will scroll at {} BPM.".format(self.scroll))
            confirmation = raw_input("Would you like to continue? 'y' to continue, 'q' to quit, other to restart. ")
            if confirmation.lower() == 'q':
                sys.exit()

        self.choices(notes_sb)

    def choices(self, notessb):
        print("What do you want to do? - 'q' to exit")
        n = 1

        choice_str = y_str = z_str = ""
        choice = y = z = 0

        for x in modstypes.modtypes:
            print ("{}.\t{}".format(n, x))
            n += 1

        while choice not in range(1, len(modstypes.modtypes) + 1):
            while not choice_str.isdigit():
                choice_str = raw_input(">>>")
                if choice_str.lower() == 'q':
                    sys.exit()
            choice = int(choice_str)

        if choice != 3:
            modslist = modstypes.writelist(choice - 1)
            y = 0
            while y not in range(1, len(modslist) + 1):
                while not y_str.isdigit():
                    y_str = raw_input(">>>")
                    if y_str.lower() == 'q':
                        sys.exit()
                y = int(y_str)

            if choice == 2:
                mods2list = modstypes.writelist(2)
                z = 0
                while z not in range(1, len(mods2list) + 1):
                    while not z_str.isdigit():
                        z_str = raw_input(">>>")
                        if z_str.lower() == 'q':
                            sys.exit()
                    z = int(z_str)

        out = modstypes.callmod2(choice - 1, y - 1, z - 1, notessb, self.scroll)

        utils.writetofile(out)

        continue_sb = raw_input("Do you want to continue? 'y' to continue, other to quit.")
        if continue_sb == 'y':
            self.dostoryboard()
