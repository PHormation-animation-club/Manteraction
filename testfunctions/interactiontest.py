#!!!do not change this file, it is used for testing the interaction of the test functions with the optimization algorithms!!!

#here is the place where to import. Put the import as less as possible here, because this file is imported by the optimization algorithms and should not import too much stuff. Only import what is necessary for the test functions to work.

class Interaction(InteractiveScene):
    def construct(self):
        #the dot which can be dragged by mouse,the initial position of the dot is (0,0)
        dot1 = Dot().become_draggable()
        
        #the dot which can be dragged by mouse,the initial position of the dot is (1,1)
        dot2 = Dot().shift(RIGHT+UP).become_draggable()

        dot3 = Dot().shift(LEFT+UP).become_draggable()
        