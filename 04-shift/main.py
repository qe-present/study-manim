from manim import *
class Main(Scene):
    def construct(self):
        self.add(NumberPlane())
        t=Text("hello world",fill_color=BLUE).shift(RIGHT*3)
        rec=Square(side_length=3).shift(LEFT*3)
        self.play(Write(t))
        self.wait(1)
        self.play(Write(rec))
        self.wait(1)