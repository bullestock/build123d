from build123d import *
from ocp_vscode import *

h = 10
id = 15
od = 27

sh = 8
id1 = 19.5
od1 = 22.5

b_crush = 1

with BuildPart() as outer:
    with BuildSketch():
        Circle(radius=od/2)
    extrude(amount=h)
    with BuildSketch():
        Circle(radius=id/2)
    extrude(amount=h, mode=Mode.SUBTRACT)
    fillet(outer.edges().sort_by(Axis.Z)[0], radius=1)
    fillet(outer.edges().sort_by(Axis.Z)[-1], radius=1)
    fillet(outer.edges().sort_by(Axis.Z)[9], radius=2)
           
with BuildPart() as inner:
    with BuildSketch():
        Circle(radius=od1/2)
    extrude(amount=sh)
    with BuildSketch():
        Circle(radius=id1/2)
    extrude(amount=sh, mode=Mode.SUBTRACT)
    # inner ribs
    with BuildSketch():
        with PolarLocations(radius=id1/2 - 0.75, count=10, start_angle=360/20):
            Circle(b_crush)
    extrude(amount=sh, mode=Mode.SUBTRACT)
    # outer ribs
    with BuildSketch():
        with PolarLocations(radius=od1/2 + 0.75, count=10):
            Circle(b_crush)
    extrude(amount=sh, mode=Mode.SUBTRACT)


p = outer.part - inner.part

show(p, reset_camera=Camera.KEEP)

export_step(p, 'protector.step')
