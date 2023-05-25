'''
basic functions used across files
'''

# sign function used in raycasting
def sign(num):
    if num < 0: return -1
    else: return 1

# normal sign function
def zeroSign(num):
    if num > 0: return 1
    if num < 0: return -1
    return 0

# Euclidean distance
def distance(x1, y1, x2, y2):
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

# gets a unit vector in same direction
def normalizeVector(vec):
     vecX, vecY = vec[0], vec[1]
     dist = distance(0, 0, vecX, vecY)
     normVec = (vecX/dist, vecY/dist)
     return normVec

# multiplies a vector by a scalar
def vecMultiply(scalar, vec):
     return (vec[0] * scalar, vec[1]*scalar)

# takes the dot product of two vectors
def dotProduct(vec1, vec2):
     return vec1[0] * vec2[0] + vec1[1] * vec2[1]

# stops sounds from playing
def stopSound(player):
     while player.playing:
          player.next_source()