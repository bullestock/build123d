# %%
from build123d import *
from ocp_vscode import *

dial_radius = 5
flag_width = 20
flag_height = 5
flag_fillet_radius = 2
number_ring_width = 1

with BuildSketch() as base2:
    Circle(dial_radius)

    with Locations((flag_width / 2, -dial_radius + flag_height / 2, 0)):
         Rectangle(flag_width, flag_height)

    fillet(vertices().filter_by_position(Axis.X, dial_radius, dial_radius), flag_fillet_radius)
    fillet(
        vertices().filter_by_position(Axis.X, flag_width, flag_width),
        flag_fillet_radius,
    )
    outside_skt = base2.sketch
    offset(amount=-number_ring_width, kind=Kind.INTERSECTION, mode=Mode.SUBTRACT)

show(base2)