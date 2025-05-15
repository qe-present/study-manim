from manim import *
class Main(Scene):
    def construct(self):
        s=Square(side_length=3.0,fill_opacity=0.7,color=RED)
        self.play(Write(s))
        self.wait(1)
