'''
contains player class and a few methods

TO DO:
add combat features (TP1/2)
'''

from math import *
from cmu_graphics import *
import settings
import utilities
import gameplay
import time


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
        self.attacking = False
        self.attackTimer = time.time()

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

    # attack enemy
    def attack(self, enemy):
        # if cooldown over, attach enemy and reset cooldown
        if time.time()-self.attackTimer > settings.attackCooldown:
            enemy.attacked(self)
            self.attackTimer = time.time()

    # respond to getting attacked
    def attacked(self, enemy):
        self.health -= settings.enemyDamage

        # if health below zero, game over
        if self.health <= 0:
            settings.sfxFiles[9].play()
            settings.gameOver = True
        else:
            settings.sfxFiles[10].play()

        # calculate knockback from attack
        enemyDistVec = (self.x-enemy.x, self.y-enemy.y)
        normDistVec = utilities.normalizeVector(enemyDistVec)
        knockbackVec = utilities.vecMultiply(settings.knockback, normDistVec)
        gameplay.moveAxis(self, knockbackVec[0], knockbackVec[1])