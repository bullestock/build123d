from build123d import *
from ocp_vscode import *

with BuildPart() as p:
    Box(100, 100, 10)
    plane = Plane(Axis.Z).rotated((50, 0, 0)).offset(-12)
    with BuildSketch(plane) as sk:
        with Locations(Location((0, 20, 0))):
            Circle(15)
    extrude(amount=25)
    with BuildSketch(plane) as sk:
        with Locations(Location((0, 20, -10))):
            Circle(10)
    extrude(amount=20, mode=Mode.SUBTRACT)

show(p)
