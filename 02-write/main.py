from manim import *
class Main(Scene):
    def construct(self):
        text= Text("Hello, Manim!",color=DARK_BLUE,weight=BOLD,font_size=100)
        self.play(Write(text))
        self.wait(3)
        self.play(Unwrite(text))
        self.wait(1)

