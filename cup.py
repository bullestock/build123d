from build123d import *
from ocp_vscode import *

with BuildPart() as p:
    Sphere(10, 0)
    offset(amount=-1)

show(p)

export_step(p.part, 'cup.step')
