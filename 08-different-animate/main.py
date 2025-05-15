from manim import *
class Main(Scene):
    def construct(self):
        rt=RoundedRectangle(corner_radius=0.5,fill_opacity=0.2,color=BLUE,fill_color=BLUE)
        t=Triangle(fill_color=RED,fill_opacity=0.5)
        self.add(rt)
        self.wait(2)
        self.play(Transform(rt,t))
        self.wait(2)
