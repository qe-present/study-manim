from manim import *
class Main(Scene):
    def construct(self):
        rt=RoundedRectangle(corner_radius=0.5,fill_opacity=0.2,color=BLUE,fill_color=BLUE)
        # 类似于一个圆角矩形
        self.play(Write(rt))