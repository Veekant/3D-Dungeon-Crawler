'''
this file contains basic functions that will be used across files
'''

def sign(num):
    if num < 0: return -1
    else: return 1

def zeroSign(num):
    if num > 0: return 1
    if num < 0: return -1
    return 0

def distance(x1, y1, x2, y2):
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

def normalizeVector(vec):
     vecX, vecY = vec[0], vec[1]
     dist = distance(0, 0, vecX, vecY)
     normVec = (vecX/dist, vecY/dist)
     return normVec

def dotProduct(vec1, vec2):
     return vec1[0] * vec2[0] + vec1[1] * vec2[1]