from manim import *
class Main(Scene):
    def construct(self):
        t=Text("Hello World!")
        self.play(Write(t))


