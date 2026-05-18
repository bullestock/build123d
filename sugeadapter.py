# %%
from build123d import *
from ocp_vscode import *
from epilogue import *

tube_dia = 80
slit_w = 2
slit_depth = 15
th = 5
overall_len = 25

ring_dia_o = 73
ring_dia_i = 66.5

with BuildPart() as slit:
    with BuildSketch():
        Circle(radius=(tube_dia+slit_w)/2)
    extrude(amount=slit_depth)
    with BuildSketch():
        Circle(radius=(tube_dia+slit_w)/2+1,
               arc_size=45,
               align=None)
    extrude(amount=slit_depth)
    with BuildSketch():
        Circle(radius=(tube_dia-slit_w)/2)
    extrude(amount=slit_depth, mode=Mode.SUBTRACT)

with BuildPart() as p:
    with BuildSketch():
        Circle(radius=tube_dia/2 + th)
    extrude(amount=overall_len)
    fillet(p.edges().sort_by(Axis.Z)[0], radius=2)
    fillet(p.edges().sort_by(Axis.Z)[-1], radius=5)
    with BuildSketch(p.faces().sort_by(Axis.Z).last):
        Circle(radius=ring_dia_o/2)
    extrude(amount=-10, mode=Mode.SUBTRACT)
    with BuildSketch(p.faces().sort_by(Axis.Z).last):
        Circle(radius=ring_dia_i/2)
    extrude(amount=-overall_len, mode=Mode.SUBTRACT)
    #filletz(p, 1)
    #fillet(p.faces().filter_by(Axis.Z), radius=0.1)

p.part -= slit.part

#fillet(p.edges().filter_by(Axis.X), radius=radius)
#show(p)

epilogue(p)
