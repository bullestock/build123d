from build123d import *
from ocp_vscode import *
import time

set_port(3939)

fileName = 'noun-pig.svg'
svgFile = import_svg(fileName)

#Find min/max for all elements
for idx,ele in enumerate(svgFile):
    bbox = ele.bounding_box()
    if idx == 0:
        xMin = bbox.min.X
        xMax = bbox.max.X
        yMin = bbox.min.Y
        yMax = bbox.max.Y
    else:
        xMin = bbox.min.X if bbox.min.X < xMin else xMin        
        xMax = bbox.max.X if bbox.max.X > xMax else xMax
        yMin = bbox.min.Y if bbox.min.Y < yMin else yMin
        yMax = bbox.max.Y if bbox.max.Y > yMax else yMax

print(f'xMin: {xMin} - xMax: {xMax} - yMin:{yMin} - yMax:{yMax}')

'''
Calculate centers from min/max and lengths
'''
lengthX = (xMax - xMin)
centerX = (lengthX/2) + xMin
lengthY = (yMax - yMin)
centerY = (lengthY/2) + yMin

print(f'Center X: {centerX} - Center Y: {centerY}')


'''
Build "plate" to put SVG on. Plate shall be the same
size as the SVG and be centered on the SVG
'''
with BuildPart() as svgPart:
    #Start by creating base to work on. This shall be the "neck" + "pyriamid"
    with BuildSketch() as base_sk:
        #Move to center of svg
        with Locations((centerX, centerY)):
            Rectangle(lengthX, lengthY, align=(Align.CENTER, Align.CENTER))
    extrude(amount=-400)

    #Extrude SVG
    extrude(svgFile, amount=5)

    #Select bottom of "neck/pyramid", offset to create wall, and cut pyriamid
    #with BuildSketch() as neck_sk:


show(svgPart)