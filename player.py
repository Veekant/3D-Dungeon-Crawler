'''
contains player class and a few methods

TO DO:
add combat features (TP1/2)
'''

from math import *
from cmu_graphics import *
import settings


# rotation matrix from https://en.wikipedia.org/wiki/Rotation_matrix

class player:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y

        self.dirX = -1
        self.dirY = 0

        self.planeX = 0
        self.planeY = -0.66
    

        '''
        self.dirX = cos(dir)
        self.dirY = sin(dir)

        # use fov from settings to calculate camera vectors
        fov = settings.fov
        a = tan(radians(fov / 2))
        self.planeX = a * self.dirY
        self.planeY = -a * self.dirX
        '''

    def __str__(self):
        return (f"Player at ({self.x},{self.y}) " +
                f"facing ({self.dirX},{self.dirY}) " +
                f"with camera ({self.planeX},{self.planeY})")

    def rotate(self, theta):
        # store old variables
        oldDirX, oldDirY = self.dirX, self.dirY
        oldPlaneX, oldPlaneY = self.planeX, self.planeY

        # multiply by rotation matrix
        self.dirX = oldDirX * cos(theta) - oldDirY * sin(theta)
        self.dirY = oldDirX * sin(theta) + oldDirY * cos(theta)
        self.planeX = oldPlaneX * cos(theta) - oldPlaneY * sin(theta)
        self.planeY = oldPlaneX * sin(theta) + oldPlaneY * cos(theta)

    # move player in direction
    def move(self, dx, dy):
        # use custom rotation matrix
        moveX = dx * self.dirY + dy * self.dirX
        moveY = -dx * self.dirX + dy * self.dirY 
        # update vars
        self.x += moveX
        self.y += moveY
    
    # move player along axes
    def moveAxis(self, dx, dy):
        self.x += dx
        self.y += dy