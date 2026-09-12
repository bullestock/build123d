from build123d import *
from ocp_vscode import *
from epilogue import *

from vb_defs import *

with BuildPart() as p:
    # basic shape
    with BuildSketch():
        Rectangle(box_w, box_l)
    extrude(amount=box_h)
    filletz(p, 5)
    filletx(p, 2)
    # make shell
    offset(amount=-th, mode=Mode.SUBTRACT)
    # button holes
    with BuildSketch(last_z(p)):
        with Locations((-box_w/4, -10)):
            with GridLocations(1, 0.5*25.4, 1, 3):
                Circle(radius=6.5/2)
    extrude(amount=-th, mode=Mode.SUBTRACT)
    # switch hole
    with BuildSketch(last_z(p)):
        with Locations((box_w/4, -box_l/4)):
            Rectangle(sw_w, sw_l)
    extrude(amount=-th, mode=Mode.SUBTRACT)
    split(bisect_by=Plane.XY.offset(box_h-top_h), keep=Keep.TOP)
    #split(bisect_by=Plane.XY.offset(box_h-top_h), keep=Keep.BOTTOM)
    # ears
    with BuildSketch(last_z(p).offset(-th)):
            with GridLocations(1, box_l-2*th-insert_h, 1, 2):
                Rectangle(box_w-4*th, insert_h)
    extrude(amount=-1.75*top_h)
    # holes
    with BuildSketch(Plane.XZ.offset(-box_l/2)):
        with Locations((0, box_h - top_h*1.5)):
            with GridLocations(box_w/2, 1, 2, 1):
                Circle(radius=insert_r-0.1)
    extrude(amount=box_l, mode=Mode.SUBTRACT)
    
epilogue(p)
