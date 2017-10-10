from muma.utils import findsetting, isfloat
from muma.note_mods import BasicMod
import muma.note_mods.sbUtils
from muma.sbmods.transformations import note_transform as n_trans


class VisionCone(BasicMod):

    def __init__(self, notes, bpm, transformation):
        BasicMod.__init__(self, notes, bpm, transformation)

    def mod_setup(self):
        pass

    def note_to_sb(self, note):
        pass
