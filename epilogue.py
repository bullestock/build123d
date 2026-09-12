import sys
from pathlib import Path
from build123d import *
from ocp_vscode import *


parent_module = sys.modules['.'.join(__name__.split('.')[:-1]) or '__main__']

def epilogue(p):
    show(p, reset_camera=Camera.KEEP)

    export_step(p.part, f'{Path(parent_module.__file__).stem}.step')

def filletx(p, radius):
    fillet(p.edges().filter_by(Axis.X), radius=radius)
    
def fillety(p, radius):
    fillet(p.edges().filter_by(Axis.Y), radius=radius)
    
def filletz(p, radius):
    fillet(p.edges().filter_by(Axis.Z), radius=radius)
    
def first_x(p):
    return p.faces().sort_by(Axis.X).first
    
def last_x(p):
    return p.faces().sort_by(Axis.X).last

def first_y(p):
    return p.faces().sort_by(Axis.Y).first
    
def last_y(p):
    return p.faces().sort_by(Axis.Y).last

def first_z(p):
    return p.faces().sort_by(Axis.Z).first
    
def last_z(p):
    return p.faces().sort_by(Axis.Z).last

def z_edges(p):
    return p.edges().sort_by(Axis.Z)
    
