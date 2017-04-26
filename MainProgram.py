"""
Taiko Storyboard Generator & Beatmap Modifier
by Unmei Muma (https://osu.ppy.sh/u/481582)
Pls no slap for python 2.7 </3
"""

# Imports
import os
import sys
import time
import BeatmapParser
from BeatmapParser import listnotes as listnotes
from StoryboardMods import StoryboardMods
from DefaultSettings import TaikoStoryboard as TaikoSettings, BeatmapLocation as BeatmapDirectory
from Utils import promptmaps

# We need to check if the osu! beatmap folder and settings exist before doing anything
if not (os.path.isdir(BeatmapDirectory) and os.path.isfile("./settings.ini")):

    # Check which ones to create.
    directory = not os.path.isdir(BeatmapDirectory)
    settings = not os.path.isfile("./settings.ini")

    # If the directory is not here well just create it
    if directory:
        os.mkdir(BeatmapDirectory)
        print("osuBeatmaps directory created.")

    # Same for settings
    if settings:
        settings_file = open("./settings.ini", "w")
        for K in TaikoSettings:
            settings_file.write("{}={}\n".format(K, TaikoSettings[K]))
        settings_file.close()
        print("Settings file created.")

    # And we gotta quit too. Leave 10 seconds for the user to be fully aware the program closes.
    print("Program will close in 5 seconds.")
    time.sleep(5)
    sys.exit()

# Build a list of files in the Beatmap Directory: get everything, but only add .osu files in the list.
filelist = [f for f in os.listdir(BeatmapDirectory)
            if os.path.isfile(os.path.join(BeatmapDirectory, f)) and os.path.splitext(f)[1] == ".osu"
            ]

# Time to prompt the user to use 1 beatmap if there are more than one. If there are none, tell them to add some.
if filelist.__len__() == 0:
    print("There are no available beatmaps. Please add some before using this program.")
    time.sleep(5)
    sys.exit()

# We only retrieve the beatmaps that are Taiko. Other modes get ignored because it is not the point of this program.
taikofiles = [f for f in filelist if BeatmapParser.istaiko(BeatmapDirectory + "/" + f)]
if taikofiles.__len__() > 1:
    choice = promptmaps(taikofiles)
    # If the user chooses an invalid index, quit out as it is an abort command.
    if choice > taikofiles.__len__() or choice < 1:
        sys.exit()
    usefile = BeatmapDirectory + "/" + taikofiles[choice - 1]
else:
    usefile = BeatmapDirectory + "/" + taikofiles[0]

# The fun part starts here now.
StoryboardMods(listnotes(usefile))
