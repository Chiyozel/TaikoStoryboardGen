from switchcase import switch
from yumi.osu.notes.notetype import NoteType
from yumi.osu.notes.hitsound import Hitsound
import random


def note_transform(n, transform_type, n_in, overlay):
    out = ""
    n_x = n.t - n_in
    n_type = NoteType(n.note_type)
    note_hs = Hitsound(n.hs)
    # 0: None / 1: Abekobe / 2: Confusion / 3: Flashlight / 4: Not Abekobe / 5: Hidden / 6: Hidden+ (Colors only)
    if note_hs.iskat():
        # 2 3 4 5 6
        for case in switch(transform_type):
            if case(0) and not overlay:
                out += " C,0,{},,100,160,255\n".format(n.t)
            if case(1) and not overlay:
                out += " C,0,{},,255,80,80\n".format(n.t)
            if case(2) and not overlay:
                n_x = int(n_x / 4)
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                out += " C,0,{},{},{},{},{},100,160,255\n".format(n_in + n_x, n.t - n_x, red, green, blue)
            if case(3) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},0,0,0,100,160,255\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(4) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},255,80,80,100,160,255\n".format(n_in + 4 * n_x, n.t - 2 * n_x)
            if case(5):
                n_x = int(n_x / 8)
                if not overlay:
                    out += " C,0,{},,100,160,255\n".format(n_in)
                out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(6) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},,100,160,255\n".format(n_in)
                out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(7) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},100,160,255,128,128,128\n".format(n_in + 4 * n_x, n.t - 2 * n_x)
    elif n_type.isslider():
        # 2 3 5 6
        for case in switch(transform_type):
            if case(0) and not overlay:
                out += " C,0,{},,255,200,0\n".format(n.t)
            if case(1) and not overlay:
                out += " C,0,{},,255,200,0\n".format(n.t)
            if case(2) and not overlay:
                n_x = int(n_x / 4)
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                out += " C,0,{},{},{},{},{},255,200,0\n".format(n_in + n_x, n.t - n_x, red, green, blue)
            if case(3) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},0,0,0,255,200,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(4) and not overlay:
                out += " C,0,{},,255,200,0\n".format(n.t)
            if case(5):
                n_x = int(n_x / 8)
                if not overlay:
                    out += " C,0,{},,255,200,0\n".format(n.t)
                out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(6) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},,255,200,0\n".format(n.t)
                out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(7) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},255,200,0,128,128,128\n".format(n_in + 4 * n_x, n.t - 2 * n_x)
    elif n_type.isspinner():
        # 2 3 5 6
        for case in switch(transform_type):
            if case(0) and not overlay:
                out += " C,0,{},,128,128,128\n".format(n.t)
            if case(1) and not overlay:
                out += " C,0,{},,128,128,128\n".format(n.t)
            if case(2) and not overlay:
                n_x = int(n_x / 4)
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                out += " C,0,{},{},{},{},{},128,128,128\n".format(n_in + n_x, n.t - n_x, red, green, blue)
            if case(3) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},0,0,0,128,128,128\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(4) and not overlay:
                out += " C,0,{},,128,128,128\n".format(n.t)
            if case(5):
                n_x = int(n_x / 8)
                if not overlay:
                    out += " C,0,{},,128,128,128\n".format(n.t)
                out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(6) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},,128,128,128\n".format(n_in)
                out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(7) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},100,160,255,128,128,128\n".format(n_in + 4 * n_x, n.t - 2 * n_x)
    else:
        # 2 3 4 5 6
        for case in switch(transform_type):
            if case(0) and not overlay:
                out += " C,0,{},,255,80,80\n".format(n.t)
            if case(1) and not overlay:
                out += " C,0,{},,100,160,255\n".format(n.t)
            if case(2) and not overlay:
                n_x = int(n_x / 4)
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                out += " C,0,{},{},{},{},{},255,80,80\n".format(n_in + n_x, n.t - n_x, red, green, blue)
            if case(3) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},0,0,0,255,80,80\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(4) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},100,160,255,255,80,80\n".format(n_in + 4 * n_x, n.t - 2 * n_x)
            if case(5):
                n_x = int(n_x / 8)
                if not overlay:
                    out += " C,0,{},,255,80,80\n".format(n_in)
                out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(6) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},,255,80,80\n".format(n_in)
                out += " F,0,{},{},1,0\n".format(n_in + 3 * n_x, n.t - 3 * n_x)
            if case(7) and not overlay:
                n_x = int(n_x / 8)
                out += " C,0,{},{},255,80,80,128,128,128\n".format(n_in + 4 * n_x, n.t - 2 * n_x)
    return out
