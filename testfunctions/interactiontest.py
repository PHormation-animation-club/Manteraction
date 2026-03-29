#!!!do not change this file, it is used for testing the interaction of the test functions with the optimization algorithms!!!

#here is the place where to import. Put the import as less as possible here, because this file is imported by the optimization algorithms and should not import too much stuff. Only import what is necessary for the test functions to work.

class Interaction(InteractiveScene):
    def construct(self):
        #the dot which can be dragged by mouse,the initial position of the dot is (0,0)
        dot1 = Dot().become_draggable()
        
        #the dot which can be dragged by mouse,the initial position of the dot is (1,1)
        dot2 = Dot().shift(RIGHT+UP).become_draggable()

        #the dot which can be dragged by mouse, which is limited to a boundary. the boundary number can be a geometric shape or a function
        dot3 = Dot().become_draggable(x_boundary = [-1,1],y_boundary = [-1,1])
        #or restriction_function = f(x), where toe dot can only move in space f(x)<0
        #or restrict_shape = Cricle()
        