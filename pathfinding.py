'''
pathfinding algorithm and helper function implemented here

TO DO: None
'''

import settings
import math
import utilities

# A* algorithm from:
# https://www.youtube.com/watch?v=ySN5Wnu88nE
# https://www.youtube.com/watch?v=icZj67PTFhc (just the example part)

# convert position to center of current tile
def convertToNavCoords(pos):
    posX = int(pos[0])
    posY = int(pos[1])
    return (posX, posY)

# get set of all walkable tiles in map
def getMapGraph(map):
    cols, rows = len(map), len(map[0])
    graph = set()
    # loop through all tiles
    for col in range(cols):
        for row in range(rows):
            # add tile to set if walkable
            if map[col][row] == 0:
                graph.add((col, row))
    return graph

# get dict from set with a default val
def getGraphDict(graph, val):
    graphDict = dict()
    for node in graph:
        graphDict[node] = val
    return graphDict

# find key in set with lowest value according to dict
def getMinKey(s, d):
    # init vars
    minKey = None
    minKeyVal = math.inf
    # loop through elems in set
    for key in s:
        # if elem in dict and value is lowest, update vars
        if key in d and d[key] < minKeyVal:
            minKey = key
            minKeyVal = d[key]
    return minKey

# get set of neighbors to a tile
def getNeighborNodes(map, pos):
    cols, rows = len(map), len(map[0])
    currCol, currRow = pos[0], pos[1]
    neighborNodes = set()
    # loop through all directions
    for dCol in [-1, 0, 1]:
        for dRow in [-1, 0, 1]:
            neighborRow, neighborCol = currRow + dRow, currCol + dCol
            # make sure neighbor is within map and walkable
            if ((0 <= neighborRow < rows) and
                (0 <= neighborCol < cols) and
                (map[neighborCol][neighborRow] == 0)):
                # only add diagonals if it doesn't clip a corner
                if dRow != 0 and dCol != 0:
                    if map[neighborRow][currCol] == 0 and map[currRow][neighborCol] == 0:
                        neighborNodes.add((neighborCol, neighborRow))
                # prevent adding current tile
                elif dRow != 0 or dCol != 0:
                    neighborNodes.add((neighborCol, neighborRow))
    return neighborNodes

# gets path from end
def getPath(prevDict, endPos):
    # init vars
    path = [endPos]
    nextNode = prevDict.get(endPos, None)
    # loop through dict to find prev node and add to path
    while nextNode != None:
        path.append(nextNode)
        nextNode = prevDict.get(nextNode, None)
    # reverse the path so the end is at the end
    return list(reversed(path))

# basic distance function
def distance(posInitial, posFinal):
    return utilities.distance(posInitial[0], posInitial[1], posFinal[0], posFinal[1])

# heuristic function for A* algorithm
def heuristic(current, target):
    return distance(current, target)

# find path from start to end using A*
def findPath(start, end):
    map = settings.map
    start, end = convertToNavCoords(start), convertToNavCoords(end)
    mapGraph = getMapGraph(map)

    # initialize sets and dicts
    checkSet = {start}
    prevDict = getGraphDict(mapGraph, None)
    localScoreDict = getGraphDict(mapGraph, math.inf)
    globalScoreDict = getGraphDict(mapGraph, math.inf)

    # set values of start node
    localScoreDict[start] = 0
    globalScoreDict[start] = heuristic(start, end)

    # while there are nodes left to check
    while len(checkSet) > 0:
        # get closest node
        curr = getMinKey(checkSet, globalScoreDict)
        # return path if node at the end
        if curr == end:
            return getPath(prevDict, curr)
        # loop through neighbors
        for neighbor in getNeighborNodes(map, curr):
            localPathScore = localScoreDict[curr] + distance(curr, neighbor)
            # if current path is better than previous path, update values and add neighbor to be checked
            if localPathScore < localScoreDict[neighbor]:
                prevDict[neighbor] = curr
                localScoreDict[neighbor] = localPathScore
                globalScoreDict[neighbor] = localPathScore + heuristic(curr, end)
                checkSet.add(neighbor)
        # remove node, since checked
        checkSet.remove(curr)
    # if no paths, return None
    return None