# %%
from build123d import *
from ocp_vscode import *

conn_w = 5.9 + 0.05
conn_l = 8
conn_h = 6
block_h = 10
N = 3
cc = 8

with BuildPart() as o:
    # basic shape
    Box((N + 0.5)*cc, conn_l, block_h)#, align=Align.MIN)
    # fillet
    fillet(o.edges().filter_by(Axis.Z), radius=1)
    fillet(o.edges().sort_by(Axis.Z)[-1], radius=1)
    # holes
    with BuildSketch(o.faces().sort_by(Axis.Y)[-1]) as h:
        with Locations([ ((block_h - conn_h)/2 + 1, 0, 0) ]):
            Rectangle(conn_w, conn_h)
        with Locations([ ((block_h - conn_h)/2 + 1, cc, 0) ]):
            Rectangle(conn_w, conn_h)
        with Locations([ ((block_h - conn_h)/2 + 1, -cc, 0) ]):
            Rectangle(conn_w, conn_h)
    extrude(amount=-conn_l, mode=Mode.SUBTRACT)

show(o)    
export_step(o.part, "jstmaleholder.step")
