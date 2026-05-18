from build123d import *
from ocp_vscode import *

width = 14
length = 70
height = 14
th = 2

with BuildPart() as p:
    with BuildSketch(Plane.XY):
        RectangleRounded(length, width, width/2 - 0.1)
    extrude(amount=th)
    with BuildSketch(Plane.XY):
        Rectangle(length, th)
    extrude(amount=height)
    e = p.edges().sort_by(Axis.Z)
    fillet([e[-1], e[-2], e[-4]], radius=1)

show(p)

export_step(p.part, 'machinetap-divider.step')
