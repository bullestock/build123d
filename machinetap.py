from build123d import *
from ocp_vscode import *

holes = (
    (0, 9.5),
    (18, 8.5),
    (33, 6.5),
    (48, 6)
)

holes2 = (
    (0, 4.8),
    (15, 5),
    (30, 4),
    (45, 3)
)

width = 14
length = 68
height = 30#25

with BuildPart() as p:
    with BuildSketch(Plane.XY):
        #RectangleRounded(length, width, 2)
        Rectangle(length, width)
    extrude(amount=height)
    edges = [1, -1]
    fillet([p.edges().filter_by(Axis.X)[i] for i in edges], width/2-0.01)
    fillet([p.edges().filter_by(Axis.Z)[i] for i in edges], 1)
    with BuildSketch(Plane.XY):
        x = -length/2 + (length - holes[-1][0])/2
        for h in holes:
            with Locations((x + h[0], 0)):
                Circle(radius=h[1]/2)
    extrude(amount=height-5, mode=Mode.SUBTRACT)
    with BuildSketch(p.faces().filter_by(Axis.X).last):
        with Locations((0, height/2 - 5)):
            Circle(radius=3/2)
    extrude(amount=2)
    with BuildSketch(p.faces().filter_by(Axis.X).first):
        with Locations((0, -height/2 + 5)):
            Circle(radius=3/2)
    extrude(amount=2)

show(p)

export_step(p.part, 'machinetap.step')
