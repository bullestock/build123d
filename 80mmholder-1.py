# %%
from build123d import *
from ocp_vscode import *
from epilogue import *

tube_dia = 80
th = 10
width = 30
standoff = 25

with BuildPart() as p:
    with BuildSketch():
        Circle(radius=tube_dia/2 + th, arc_size=180, align=None)
    extrude(amount=width)
    with BuildSketch():
        Circle(radius=tube_dia/2, arc_size=180, align=None)
    extrude(amount=width, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XZ):
        with Locations((0, width/2)):
            with GridLocations(tube_dia+th, 1, 2, 1):
                Rectangle(th, width)
    extrude(amount=tube_dia/2+standoff)
    fillet(p.edges().sort_by(Axis.Z)[2], radius=2)
    fillet(p.edges().sort_by(Axis.Z)[-3], radius=2)
    with BuildSketch(Plane.YZ.offset(-tube_dia/2-th)):
        with Locations((-(standoff+tube_dia/2-10), width/2)):
            Circle(radius = 5.5/2)
    extrude(amount=tube_dia+2*th, mode=Mode.SUBTRACT)

epilogue(p)
