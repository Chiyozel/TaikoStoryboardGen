from yumi.utils import findsetting


def createbase():
    out = ""

    # Main Black Bar
    out += "Sprite,Background,Centre,\"SB/black_bar.png\",320,240\n"
    out += " F,0,0,500000,1\n"
    out += " M,0,0,500000,320,{}\n".format(findsetting("Receptor_Y"))

    # Receptor
    out += "Sprite,Foreground,Centre,\"SB/point.png\",320,240\n"
    out += " S,0,0,500000,0.4\n"
    out += " F,0,0,500000,1\n"
    out += " M,0,0,500000,{},{}\n".format(findsetting("Receptor_X"), findsetting("Receptor_Y"))

    # Taiko Left Portion
    out += "Sprite,Foreground,Centre,\"SB/taiko_left.png\",320,240\n"
    out += " M,0,0,500000,{},{}\n".format(int(findsetting("CounterCentreLeft")) - 60, findsetting("Receptor_Y"))
    out += " F,0,0,50000,1\n"

    # No idea what else to add.

    return out
