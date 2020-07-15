from manimlib.imports import *

class SineWave(Scene):
    def get_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: np.sin((x+dx)) + np.sin((x-dx)),
            x_min=-10,x_max=10
        )

    def construct(self):
        sine_function=self.get_sine_wave()
        d_theta=ValueTracker(0)
        def update_wave(func):
            breakpoint()
            func.become(
                self.get_sine_wave(dx=d_theta.get_value())
            )
            return func
        sine_function.add_updater(update_wave)
        # sine_function = always_redraw(sine_function)
        self.play(ShowCreation(sine_function))
        breakpoint()
        self.play(d_theta.increment_value,(2*PI),rate_func=linear)
        self.wait()
