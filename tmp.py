"""
Bpython => manually solved part 2 of crossed Wires
"""
import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import shapely
from shapely.geometry import LineString, Point
from shapely.ops import nearest_points
from crossedWires import *

D1 = draw(W1, origin)
D2 = draw(W2, origin)

POINTS = intersectionPoints(W1, W2)
P = POINTS[0]


def LEN(D, P):
    D = copy.copy(D)
    DATA = [D.pop(0)]
    intersects = False
    while not intersects:
        DATA.append(D.pop(0))
        L = LineString(DATA)
        if L.intersects(Point(P)):
            intersects = True
    DATA[-1] = P
    L = LineString(DATA)
    return L.length


for P in POINTS:
    LEN(D1, P) + LEN(D2, P)
