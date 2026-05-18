from build123d import *
from ocp_vscode import *

width = 

length, thickness, fontsz, fontht = 25, 25.0, 10, 1.5

with BuildPart() as block:
    Box(length, width, thickness)
    fillet(block.edges().filter_by(Axis.Y), radius=2)
    txtf = block.faces().sort_by(Axis.X)[-1]
    with BuildSketch(txtf) as block_sk2:
        Text(str(width), font_size=fontsz, font_style=FontStyle.BOLD, align=(Align.CENTER, Align.CENTER))
    extrude(amount=-fontht, mode=Mode.SUBTRACT)
    
show(block)

export_step(block.part, f'block{width}.step')
