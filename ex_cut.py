from build123d import *
from ocp_vscode import *

base_shapes = PolarLocations(15, 20) * Box(4, 4, 4)
holes = PolarLocations(17, 20) * Cylinder(1, 4)

#start_time = timeit.default_timer()
compound_shapes = Compound(base_shapes).cut(Compound(holes))
#print(f"Time: {timeit.default_timer() - start_time:0.3f}s")
