from build123d import *
from ocp_vscode import *

#shapes = Pos(X=10) * GridLocations(5, 3, 2, 2) * Circle(1)

with BuildSketch() as skt:
    with Locations(Pos(X=10)):
        with GridLocations(5, 3, 2, 2):
            Circle(1)

show(skt)
