from typing import List
import numpy as np


class Wave:

    tolerance = 0.1

    def __init__(self, frequencies: List[float]):
        self.frequencies = sorted(frequencies)

    def visualize(self):
        pass

    @property
    def fundamental(self):
        return self.frequencies[0]

    def get_ratio(self, freq):
        irr_ratio = freq / self.fundamental

        def is_whole(f, eps):
            return abs(f - round(f)) < abs(eps)

        for denom in range(1, 21):
            print(denom, irr_ratio * denom)
            if is_whole(irr_ratio * denom, Wave.tolerance):
                return irr_ratio * denom, denom

        raise ValueError("not a valid ratio")

    # in cycles
    @property
    def period_multiple(self):
        denoms = [self.get_ratio(f)[1] for f in self.frequencies]
        return np.lcm.reduce(denoms)

    @property
    def frequency(self):
        return self.fundamental / self.period

    def __add__(self, other):
        return Wave(self.frequencies + other.frequencies)