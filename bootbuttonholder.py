# %%
from build123d import *
from ocp_vscode import *
from epilogue import *

w = 20

with BuildPart() as p:
    # body
    with BuildSketch():
        RectangleRounded(w, 15, 1)
    extrude(amount=5)
    with BuildSketch():
        with Locations((0, 3)):
            with GridLocations(10.34, 1, 2, 1):
                RectangleRounded(6.2, 4.2, 0.9)
    extrude(amount=30, mode=Mode.SUBTRACT)
    with BuildSketch(p.faces().sort_by(Axis.Z).last):
        with Locations((0, -3.875)):
            RectangleRounded(w, 6, 1)
    extrude(amount=10)
    #fillet(p.edges().sort_by(Axis.Z)[0], radius=1)
    with BuildSketch(p.faces().sort_by(Axis.Z).last):
        with GridLocations(10, 1, 2, 1):
            Circle(radius=2)
    extrude(amount=-30, mode=Mode.SUBTRACT)

epilogue(p)
