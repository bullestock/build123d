from build123d import *
from ocp_vscode import *

outer_dia = 10
hole_dia = 1.55
thickness = 4.5
slot_dia = 2

bottom = (Align.CENTER, Align.CENTER, Align.MIN)

with BuildPart() as p:
    Cylinder(outer_dia/2, thickness)
    fillet(p.edges().sort_by(Axis.Z)[0], radius=0.25)
    #with Locations([(0, 0, 1.75)]):
    Torus(outer_dia/2, slot_dia/2, mode=Mode.SUBTRACT)
    Cylinder(hole_dia/2, 10, 
             mode=Mode.SUBTRACT)
show(p)

export_step(p.part, 'pulley-small10.step')
