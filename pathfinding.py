'''
pathfinding algorithm and helper function implemented here

TO DO:
Implement helper functions to get map and stuff
Implement A Star Algorithm
'''

import settings
import math

def getMapGraph():
    map = settings.map
    rows, cols = len(map), len(map[0])
    graph = set()
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == 0:
                graph.add((row, col))
    return graph

def getNeighborNodes(row, col):
    neighborNodes = set()
    print("want cry now")