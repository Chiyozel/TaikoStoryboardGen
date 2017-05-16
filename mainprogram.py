"""
Taiko Storyboard Generator & Beatmap Modifier
Made with love by Unmei Muma (https://osu.ppy.sh/u/481582)
Pls no slap for python 2.7 </3
"""

# Imports
import os
import sys
import time

from yumi.default.settings import taikostoryboard as taikosettings, beatmaplocation as beatmapdirectory
from yumi.osu import parser
from yumi.osu.parser import listnotes as listnotes
from yumi.storyboardmods import StoryboardMods
from yumi.utils import promptmaps

# We need to check if the osu! beatmap folder and settings exist before doing anything
if not (os.path.isdir(beatmapdirectory) and os.path.isfile("./settings.ini")):

    # Check which ones to create.
    directory = not os.path.isdir(beatmapdirectory)
    settings = not os.path.isfile("./settings.ini")

    # If the directory is not here well just create it
    if directory:
        os.mkdir(beatmapdirectory)
        print("osu! beatmaps directory created. Put osu!taiko beatmaps (.osu) in the folder.")

    # Same for settings
    if settings:
        settings_file = open("./settings.ini", "w")
        for K in taikosettings:
            settings_file.write("{}={}\n".format(K, taikosettings[K]))
        settings_file.close()
        print("Settings file created.")

    # And we gotta quit too. Leave 10 seconds for the user to be fully aware the program closes.
    print("Program will close in 5 seconds.")
    time.sleep(5)
    sys.exit()

# Build a list of files in the Beatmap Directory: get everything, but only add .osu files in the list.
filelist = [f for f in os.listdir(beatmapdirectory)
            if os.path.isfile(os.path.join(beatmapdirectory, f)) and os.path.splitext(f)[1] == ".osu"
            ]

# Time to prompt the user to use 1 beatmap if there are more than one. If there are none, tell them to add some.
if filelist.__len__() == 0:
    print("There are no available osu!taiko beatmaps. Please add some before using this program.")
    time.sleep(5)
    sys.exit()

# We only retrieve the beatmaps that are Taiko. Other modes get ignored because it is not the point of this program.
taikofiles = [f for f in filelist if parser.istaiko(beatmapdirectory + "/" + f)]
if taikofiles.__len__() > 1:
    choice = promptmaps(taikofiles)
    # If the user chooses an invalid index, quit out as it is an abort command.
    if choice > taikofiles.__len__() or choice < 1:
        sys.exit()
    usefile = beatmapdirectory + "/" + taikofiles[choice - 1]
else:
    usefile = beatmapdirectory + "/" + taikofiles[0]

# The fun part starts here now.
StoryboardMods(listnotes(usefile))
