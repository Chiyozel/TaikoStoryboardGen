import modstypes
from yumi import utils


class StoryboardMods:
    def __init__(self, notelist):
        self.notes = notelist
        self.scroll = None
        self.dostoryboard()

    def dostoryboard(self):
        confirmation = None
        notes_sb = None
        while confirmation != "y":
            notes_sb = []
            beginning = int(raw_input("Beginning of the SB mod: >>>"))
            end = int(raw_input("End of the SB mod: >>>"))
            if beginning > end:
                end, beginning = beginning, end
            for n in self.notes:
                if beginning <= n.t < end:
                    notes_sb = notes_sb + [n]

            self.scroll = float(raw_input("Scrolling speed of the SB mod: >>>"))

            print(
                "The current section spans from {}ms to {}ms, and has {} notes.".format(beginning, end, len(notes_sb)))
            print("The notes will scroll at {} BPM.".format(self.scroll))
            confirmation = raw_input("Would you like to continue? 'y' to continue, other to restart. ")

        self.choices(notes_sb)

    def choices(self, notessb):
        print("What do you want to do?")
        n = 1
        choice = 0
        for x in modstypes.modtypes:
            print ("{}.\t{}".format(n, x))
            n += 1

        while choice not in range(1, len(modstypes.modtypes) + 1):
            choice = int(raw_input(">>>"))
        if choice != 3:
            modslist = modstypes.writelist(choice - 1)
            y = 0
            while y not in range(1, len(modslist) + 1):
                y = int(raw_input(">>>"))

            if choice == 2:
                mods2list = modstypes.writelist(2)
                z = 0
                while z not in range(1, len(mods2list) + 1):
                    z = int(raw_input(">>>"))
            else:
                z = 0
        else:
            y = z = 0

        out = modstypes.callmod2(choice - 1, y - 1, z - 1, notessb, self.scroll)
        utils.writetofile(out)
        continue_sb = raw_input("Do you want to continue? 'y' to continue, other to quit.")
        if continue_sb == 'y':
            self.dostoryboard()
