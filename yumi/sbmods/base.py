from yumi.utils import findsetting, isfloat


def createbase():
    out = ""
    scale = float(findsetting("ScaleFactor")) if isfloat(findsetting("ScaleFactor")) else 1

    # Main Black Bar
    out += "Sprite,Background,Centre,\"{}.png\",320,240\n".format("taiko-bar-right" if findsetting("UseSkinElements") else "SB/black_bar")
    out += " F,0,0,500000,1\n"
    out += " M,0,0,500000,320,{}\n".format(findsetting("Receptor_Y"))
    out += " V,0,0,500000,1,{}\n".format(0.4 * scale)

    # Receptor
    out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format("approachcircle" if findsetting("UseSkinElements") else "SB/point")
    out += " S,0,0,500000,{}\n".format(0.4 * scale)
    out += " F,0,0,500000,1\n"
    out += " M,0,0,500000,{},{}\n".format(findsetting("Receptor_X"), findsetting("Receptor_Y"))

    # Taiko Left Portion
    out += "Sprite,Foreground,Centre,\"{}.png\",320,240\n".format("taiko-bar-left" if findsetting("UseSkinElements") else "SB/taiko_left")
    out += " M,0,0,500000,{},{}\n".format(int(findsetting("CounterCentreLeft")) - 60, findsetting("Receptor_Y"))
    out += " F,0,0,50000,1\n"
    out += " S,0,0,500000,{}\n".format(0.4 * scale)

    # No idea what else to add.

    return out
