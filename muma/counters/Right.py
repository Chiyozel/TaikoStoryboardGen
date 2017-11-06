from muma.utils import findsetting
from muma.counters.Counter import Counter


class RightCounter(Counter):
    def counter_x(self):
        return int(findsetting("CounterCentreLeft")) if self.is_reverse else int(findsetting("CounterCentreRight"))
