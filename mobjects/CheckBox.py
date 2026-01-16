from manim import *

class CheckBox(VGroup):
    """
    this mobject is used as one of the input source of Manteraction.
    method:
    __init__:
    initialize the checkbox

    check:
    checking the checkbox
    """
    def __init__(
        self,
        is_checked=False
        ,box_color=WHITE,
        box_size = 1,
        check_color=WHITE,
        corner_radius_factor = 0.2,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.is_checked = is_checked
        self.surrounding_edge  = RoundedRectangle(
            stroke_color=WHITE,
            corner_radius=corner_radius_factor*box_size,

            fill_color=box_color,
            height=box_size,
            width=box_size,
        )

        self.checkmark = VGroup(

            RoundedRectangle(
                corner_radius=(corner_radius_factor-0.05)*box_size,
                fill_color=check_color,
                height=box_size*0.9,
                width=box_size*0.9,
                fill_opacity=1
            ).set_fill(check_color),


        )
        """
                    Line(
                        start=DOWN,
                        end=LEFT,
                        stroke_width=box_size * 0.2,
                        stroke_color=BLACK,
                    ).set_z_index(0),
                    """

        self.add(self.surrounding_edge)
        if self.is_checked:
            self.add(self.checkmark)



    def check(self):
        if self.is_checked:
            yield
        else:
            self.checkmark.set_color(WHITE)
        self.is_checked = not self.is_checked
        return self