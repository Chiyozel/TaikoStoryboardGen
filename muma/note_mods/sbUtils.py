import math
import sys

from muma.osu.notes import Hitsound
from muma.sbmods.tweentypes import tweens
from muma.utils import findsetting, isfloat


class sbUtils:
    def __init__(self):
        pass

    @staticmethod
    def scale_big(note):
        scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

        if Hitsound(note.hs).isfinish():
            return " S,0,{},,{}\n".format(note.t, 0.50 * scale)
        else:
            return " S,0,{},,{}\n".format(note.t, 0.35 * scale)

    @staticmethod
    def scale_big_clock(note):
        scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

        if Hitsound(note.hs).isfinish():
            return " S,0,{},,{}\n".format(note.t, 0.25 * scale)
        else:
            return " S,0,{},,{}\n".format(note.t, 0.175 * scale)

    @staticmethod
    def overlay(note, color):
        scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

        if Hitsound(note.hs).isfinish():
            return "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format("bigcirc_inv" if color == 8 else
                                                                          "taikobigcircleoverlay" if findsetting(
                                                                              "UseSkinElements")
                                                                          else "SB/notebig-overlay") \
                   + " S,0,{},,{}\n".format(note.t, 0.50 * scale)
        else:
            return "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format("hitcirc_inv" if color == 8 else
                                                                          "taikohitcircleoverlay" if findsetting(
                                                                              "UseSkinElements")
                                                                          else "SB/note-overlay") \
                   + " S,0,{},,{}\n".format(note.t, 0.35 * scale)

    @staticmethod
    def overlay_clock(note, color):
        scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

        if Hitsound(note.hs).isfinish():
            return "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format("bigcirc_inv" if color == 8 else
                                                                          "taikobigcircleoverlay" if findsetting(
                                                                              "UseSkinElements")
                                                                          else "SB/notebig-overlay") \
                   + " S,0,{},,{}\n".format(note.t, 0.25 * scale)
        else:
            return "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format("hitcirc_inv" if color == 8 else
                                                                          "taikohitcircleoverlay" if findsetting(
                                                                              "UseSkinElements")
                                                                          else "SB/note-overlay") \
                   + " S,0,{},,{}\n".format(note.t, 0.175 * scale)

    @staticmethod
    def getwavetween(ntweens):
        arr_tween = []
        tween_str = ""
        x = 1
        for i in range(0, len(tweens), 5):
            for offset in range(0, 5):
                sys.stdout.write("{}   |   ".format(tweens[i + offset]))
            print("")
        while not x > ntweens:
            print ("Enter tween type {} ".format(x))
            while not (tween_str.isdigit() and 0 <= int(tween_str) <= 34):
                tween_str = input(">>>")
            arr_tween.append(int(tween_str))
            tween_str = ""
            x += 1
        return arr_tween

    @staticmethod
    def convert_deg_to_rad(deg):
        return deg * (math.pi / 180)

    @staticmethod
    def tan_scale(note, freq, bpm):
        scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1
        size = 0.50 if Hitsound(note.hs).isfinish() else 0.35
        period = 4. / freq
        scale_str = ""
        for x in range(freq, 0, -1):
            scale_str += " S,15,{},{},{},{}\n".format(int(note.t - 60000 / bpm * (x - 0.0) * period),
                                                      int(note.t - 60000 / bpm * (x - 0.5) * period),
                                                      size * scale,
                                                      10 * size * scale)
            scale_str += " S,16,{},{},{},{}\n".format(int(note.t - 60000 / bpm * (x - 0.5) * period),
                                                      int(note.t - 60000 / bpm * (x - 1.0) * period),
                                                      0,
                                                      size * scale)
        return scale_str
