from build123d import *
from ocp_vscode import *

width = 14
length_i = 68.2
length_o = 68+4
height = 12+3.5
th = 2

with BuildPart() as p:
    with BuildSketch(Plane.XY):
        Rectangle(length_o, width)
    extrude(amount=height)
    edges = [1, -1]
    fillet([p.edges().filter_by(Axis.X)[i] for i in edges], 1)
    with BuildSketch(p.faces().filter_by(Axis.X).first):
        with Locations((0, -height/2 + 5)):
            Circle(radius=3/2)
    extrude(amount=-200, mode=Mode.SUBTRACT)
    with BuildSketch(Plane.XY.offset(th)):
        Rectangle(length_i, width)
    extrude(amount=height, mode=Mode.SUBTRACT)

show(p)

export_step(p.part, 'machinetap-holder.step')
