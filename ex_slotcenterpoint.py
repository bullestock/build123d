from build123d import *
from ocp_vscode import *

# Definire i punti
punto1 = (0, 0, 0.2)
punto2 = (100, 100, 0.2)

# Calcolare la larghezza e l'altezza dello slot
width = 100  # Larghezza complessiva dello slot
height = 20  # Altezza dello slot (diametro dei cerchi alle estremità)
rotation = 30
l1 = Line((-100, 0), (100, 0))
l2 = Line((0, -100), (0, 100))
# Creare la parte e lo sketch
with BuildPart() as slot:

    # Creare uno sketch sul piano XY
    with BuildSketch(Plane.XY) as sketch:
        SlotCenterPoint(
            center=(
                (punto2[0] - punto1[0]) / 2,
                (punto2[1] - punto1[1]) / 2,
                0),
            point=punto2,
            height=height,
            rotation=rotation
        )
    # Estrudere lo slot
    extrude(amount=2, mode=Mode.ADD)
# Esportare la par0te come file STP
export_step(slot.part, "slot.step")
show(slot)
