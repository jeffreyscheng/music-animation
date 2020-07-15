from manimlib.imports import *
import math

class SineWave(Scene):
    def construct(self):
        axes = Axes()
        def f(x, t):
            #function that you want to draw
           return math.sin(x + t) + math.sin(x - t)

        _t = ValueTracker()
        def get_f(): return axes.get_graph(lambda x: f(x, _t.get_value()))

        func = always_redraw(get_f)
        self.add(func)

        self.play(_t.set_value, 10, run_time = 10, rate_func = linear)
