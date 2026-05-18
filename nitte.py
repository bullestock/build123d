from build123d import *
from ocp_vscode import *

id = 9.75
od1 = 11.2
od2 = 13
h1 = 1.4

with BuildPart() as p:
    with BuildSketch():
        Circle(od1/2)
    extrude(amount=h1)
    with BuildSketch():
        Circle(id/2)
    extrude(amount=h1, mode=Mode.SUBTRACT)

show(p)

export_step(p.part, 'nitte.step')
