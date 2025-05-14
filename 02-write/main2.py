from manim import *
class Main2(Scene):
    def construct(self):
        text = Text("Hello world", t2c={'o': YELLOW}, disable_ligatures=True)
        self.add(text)