from manim import *
from utils.functions import round_to_piece


class Slider(VGroup):
    """
    this Mobject is used as a input source of Manteraction.
    it can accept a continuous and discrete equal-difference value between 0 and 1.
    """
    def __init__(
            self,
            start=LEFT*0.5,
            end= RIGHT*0.5,
            value=0,
            slide_colour=WHITE,
            slide_size = 0.2,
            groove_width = 0.1
    ):
        self.value=value
        if groove_width>slide_size:
            raise ValueError("I'm sorry about this nonsense restriction, but groove_width must be smaller than slide_size, or it will looks ugly :)")
        super().__init__()
        base_line = Line(start,end)
        slide = Circle(
            radius=slide_size/2
        ).set_fill(slide_colour).move_to(
            base_line.get_start()*self.value+
            base_line.get_end()*(1-self.value)
        )
        self.add(base_line,slide)

    def set_value(self,value):
        self.value=value
        return self




class discrete_slider(Slider):
    def __init__(self,start=LEFT*0.5, end=RIGHT*0.5, value=0,piece_num=100,slide_colour=WHITE):
        self.piece_num = piece_num
        super().__init__(
            start=start,
            end=end,
            value=round_to_piece(value,piece_num),
            slide_colour=slide_colour
        )
    def set_value(self,value):
        super().set_value(
            round_to_piece(value, self.piece_num)
        )
















