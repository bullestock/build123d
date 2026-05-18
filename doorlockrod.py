from pathlib import Path
from build123d import *
from ocp_vscode import *

h = 45
w = 6

b_crush = 1

with BuildPart() as p:
    with BuildSketch():
        Rectangle(w, w)
    extrude(amount=h)
    with BuildSketch():
        Rectangle(w, 1)
    extrude(amount=3, mode=Mode.SUBTRACT)
           
show(p, reset_camera=Camera.KEEP)

export_step(p.part, f'{Path(__file__).stem}.step')

