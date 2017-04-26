import os
from DefaultSettings import TaikoStoryboard


def getbit(x, k):
    return (x >> k) & 1 == 1


def promptmaps(listmaps):
    x = 1
    print("Choose a beatmap from this list to continue.\n{} or above to abort.".format(listmaps.__len__() + 1))
    for beatmap in listmaps:
        print("{}.\t{}".format(x, os.path.splitext(beatmap)[0]))
        x += 1
    return int(raw_input(">>>"))


def writeFile(out):
    sb_location = findSetting("StoryboardLocation")
    f = open(sb_location, "a")
    f.write(out)
    f.write("\n")
    f.close()


def findSetting(setting):
    if os.path.isfile("./settings.ini"):
        settings_file = open("./settings.ini", "r")
        listsettings = {}
        for line in settings_file:
            key, value = line.strip('\n').split("=")
            listsettings[key] = value
        return listsettings[setting] if setting in listsettings.keys() else TaikoStoryboard[setting]
    else:
        return TaikoStoryboard[setting]