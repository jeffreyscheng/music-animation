from typing import List
import numpy as np
from manimlib.imports import *
import math


class Wave:

    tolerance = 0.1

    def __init__(self, frequencies: List[float]):
        self.frequencies = sorted(frequencies)

    def frequency_to_standing_wave_fn(self, freq):
        def f(x, t):
            return math.sin(freq * x + t) + math.sin(freq * x - t)
        return f

    def get_wave_scene(self):
        class WaveScene(Scene):
            def construct(self2):
                axes = Axes()
                _t = ValueTracker()
                for freq in self.frequencies:
                    def get_f(): return axes.get_graph(lambda x: self.frequency_to_standing_wave_fn(freq)(x, _t.get_value()))
                    func = always_redraw(get_f)
                    self2.add(func)
                self2.play(_t.set_value, 10, run_time=10, rate_func=linear)
        return WaveScene

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


# TODO: only displays the highest frequency wave.
octave = Wave([1, 1, 10, 1])
octave_scene = octave.get_wave_scene()
SCENES_IN_ORDER = [octave_scene]
