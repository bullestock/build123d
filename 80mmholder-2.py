# %%
from build123d import *
from ocp_vscode import *
from epilogue import *

tube_dia = 80
th = 10
width = 30
standoff = 25

with BuildPart() as p:
    # base
    with BuildSketch():
        with Locations((-tube_dia/2, -tube_dia/2-standoff)):
            Rectangle(tube_dia, tube_dia/2+standoff-10, align=Align.MIN)
    extrude(amount=width)
    # tube cutout
    with BuildSketch():
        Circle(radius=tube_dia/2, align=None)
    extrude(amount=width, mode=Mode.SUBTRACT)
    # screw hole
    with Locations(p.faces().sort_by(Axis.Y)[-1].offset(-40)):
        with Locations((-tube_dia/2, 0)):
            CounterSinkHole(5/2, 8/2)
    # insert holes
    with BuildSketch(Plane.YZ.offset(tube_dia/2)):
        with Locations((-(standoff+tube_dia/2-10), width/2)):
            Circle(radius=7.1/2)
    extrude(amount=-10, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.YZ.offset(-tube_dia/2)):
        with Locations((-(standoff+tube_dia/2-10), width/2)):
            Circle(radius=7.1/2)
    extrude(amount=10, mode=Mode.SUBTRACT)
    # seam cutout
    with BuildSketch(Plane.XZ.offset(25)):
        with Locations((0, 15)):
            Rectangle(100, 10, rotation=35)
    extrude(amount=20, mode=Mode.SUBTRACT)


epilogue(p)
