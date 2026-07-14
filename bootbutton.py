# %%
from build123d import *
from ocp_vscode import *
from epilogue import *

th = 4
sr = 18

with BuildPart() as p:
    # body
    with BuildSketch():
        RectangleRounded(6, th, 1)
    extrude(amount=15)
    # button
    with BuildSketch():
        with Locations((0, 0)):
            RectangleRounded(9, 15, 1)
    extrude(amount=th)
    # depression
    with BuildSketch(p.faces().sort_by(Axis.Z).last):
        RectangleRounded(3.75, 1.75, 0.5)
    extrude(amount=-0.75, mode=Mode.SUBTRACT)
    #with Locations((0, 0, -17.5)):
    #        Sphere(radius=sr, mode=Mode.SUBTRACT)
    fillet(p.edges().sort_by(Axis.Z)[0], radius=2)
    

epilogue(p)
