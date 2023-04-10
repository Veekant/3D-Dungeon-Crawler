'''
This file will handle the bulk of the world rendering
'''
from cmu_graphics import *
import math
import player

# raycasting algorithms from https://lodev.org/cgtutor/raycasting.html

def render(app, player, map):
    for x in range(0, app.width, 1):
        adjX = (2 * x / app.width) - 1
        rayX = player.dirX + adjX * player.planeX
        rayY = player.dirY + adjX * player.planeY
        dist = rayCast(rayX, rayY, player, map)

def rayCast(rayDirX, rayDirY, player, map):
    posX, posY = player.x, player.y
    mapX, mapY = int(posX), int(posY)

    pass