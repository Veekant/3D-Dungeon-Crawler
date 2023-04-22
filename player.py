'''
contains player class and a few methods

TO DO:
add combat features (TP1/2)
'''

from math import *
from cmu_graphics import *
import settings
import input


# rotation matrix from https://en.wikipedia.org/wiki/Rotation_matrix

class player:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y

        self.dirX = cos(dir)
        self.dirY = sin(dir)

        # use fov from settings to calculate camera vectors
        fov = settings.fov
        a = tan(radians(fov / 2))
        self.planeX = -a * self.dirY
        self.planeY = a * self.dirX

        # combat stuff
        self.health = settings.maxHealth
        self.stamina = settings.maxStamina
        self.special = settings.maxSpecial
        self.blocking = False

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

    def attacked(self, enemy):
        if self.blocking and self.stamina > settings.enemyStaminaCost:
            self.stamina -= settings.enemyStaminaCost
        else:
            self.health -= settings.enemyDamage

        if self.health <= 0: settings.gameOver = True
        if self.stamina <= 0: self.blocking = False

        enemyDistVec = (self.x - enemy.x, self.y - enemy.y)
        enemyDist = distance(enemy.x, enemy.y, self.x, self.y)
        normDistVec = (enemyDistVec[0] / enemyDist, enemyDistVec[0] / enemyDist)
        knockbackVec = (normDistVec[0] * settings.knockback, normDistVec[1] * settings.knockback)
        input.move(knockbackVec[0], knockbackVec[1])
    
    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2-x1)**2 + (y2-y1)**2)**0.5 