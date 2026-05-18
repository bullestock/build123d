from build123d import *
from ocp_vscode import *

# Definire i punti
punto1 = (0, 0, 0.2)
punto2 = (100, 100, 0.2)

pseudoarc = Line(punto1, punto2)

# Calcolare la larghezza e l'altezza dello slot
width = 100  # Larghezza complessiva dello slot
height = 20  # Altezza dello slot (diametro dei cerchi alle estremità)
rotation = 30

# Creare la parte e lo sketch
with BuildPart() as slot:
    # Creare uno sketch sul piano XY
    with BuildSketch(Plane.XY) as s:
        SlotArc(pseudoarc, height)
    # Estrudere lo slot
    extrude(amount=20)

show(slot)

# Esportare la par0te come file STP
export_step(slot.part, "slot.step")
