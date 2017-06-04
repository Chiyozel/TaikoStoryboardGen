# TaikoStoryboardGen

## General

Upon first execution, the program will create a settings file and a
default osu! Taiko beatmap directory. Put any osu!Taiko beatmap you want
to use for mods (beatmaps of other modes will be skipped).

### Settings
**CounterCentreRight**: The central point of the right note countdown
(for every Reverse mode).

**CounterCentreLeft**: The central point of the left note countdown
(default scrolling type).

**CounterNumberSpacing**: The spacing between the digits in the note
countdown.

**Receptor_Y**: The Y position of the receptor. Affects the whole
playfield.

**Receptor_X**: The X position of the receptor. Affects the visibility
of notes for a high X value.

**UpsideDownReceptor_Y**: The Y position of the receptor for
"Upside-Down" mods. Affects the whole playfield.

**ReversedReceptor_X**: The X position of the receptor for "Reverse"
mods. Affects the visibility of notes for a high X value.

**PlayfieldLength**: Length of the playfield. A smaller value will put
the notes closer together, a bigger value will space the notes apart,
but will be harder to read.

**BeatmapsLocation**: The current beatmaps location. Note that changing
it will not rename the current folder.

**StoryboardLocation**: The name of the output storyboard files. Note
that it does not replace an actual osu! Storyboard file.

## Usage

0. If you have more than one beatmap, choose the beatmap you want to use.
You can quit out by inputting a different number.
1. Enter the beginning and end times of the section you want to mod, as
well as its scrolling speed (BPM x SV Greenline, or anything you wish).
2. Choose:
   - **Note counters**: Displays the amount of remaining notes before
   the end of the mod section.
   - **Note alteration & scrolling types**: The core for mods. Every mod
   will be explained in the wiki with a video illustration
   - **Create SB base**: Simply create a storyboard base with your
   current settings.
3. (Only if you chose 2) Choose your scrolling type as well as the
note transformations. Extra parameters like the amplitude or the
frequency may be asked.
4. If you wish to add more mods without the program closing, enter "y",
and steps from 1 onwards apply again until you wish to stop.
5. Copy-Paste the elements onto a storyboard file or your base osu
beatmap, as well as the elements in the folder.