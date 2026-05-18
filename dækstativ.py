from build123d import *
from ocp_vscode import *

id = 36
od = 140
rod_d = 10 #!
th = 10
cyl_h = 
with BuildPart() as p:
    Sphere(10, 0)
    offset(amount=-1)

show(p)

export_step(p.part, 'cup.step')
