from math import *
from cmu_graphics import *

# rotation formula from https://lodev.org/cgtutor/raycasting.html

class player:
    speed = 5
    lookSpeed = 1

    def __init__(self, location, dir, fov):
        self.x = location[0]
        self.y = location[1]

        self.dirX = cos(dir)
        self.dirY = sin(dir)

        a = tan(radians(fov / 2))
        self.planeX = -a * self.dirY
        self.planeY = a * self.dirX

    def __str__(self):
        return (f"Player at ({self.x},{self.y}) " +
                f"facing ({self.dirX},{self.dirY}) " +
                f"with camera ({self.planeX},{self.planeY})")

    def rotate(self, theta):
        oldDirX, oldDirY = self.dirX, self.dirY
        oldPlaneX, oldPlaneY = self.planeX, self.planeY

        self.dirX = oldDirX * cos(theta) - oldDirY * sin(theta)
        self.dirY = oldDirX * sin(theta) + oldDirY * cos(theta)

        self.planeX = oldPlaneX * cos(theta) - oldPlaneY * sin(theta)
        self.planeY = oldPlaneX * sin(theta) + oldPlaneY * cos(theta)

    def move(self, dx, dy):
        moveX = -dx * self.dirY - dy * self.dirX
        moveY = dx * self.dirX - dy * self.dirY
        self.x += moveX
        self.y += moveY