from muma.counters.Counter import Counter
from muma.utils import findsetting


class LeftCounter(Counter):
    def counter_x(self):
        return int(findsetting("CounterCentreRight")) if self.is_reverse else int(findsetting("CounterCentreLeft"))
