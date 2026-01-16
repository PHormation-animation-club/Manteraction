from manim import *
from CheckBox import CheckBox
class test(Scene):
    def construct(self):
        cb = CheckBox(is_checked=True)
        self.add(cb)
        self.wait(1)

        self.wait(1)

        self.wait(1)
        self.interactive_embed()
