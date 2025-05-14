from manim import *
class Main(Scene):
    def construct(self):
        s=Square(side_length=4.0)
        self.play(Write(s))
