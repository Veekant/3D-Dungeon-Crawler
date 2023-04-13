'''
This file will handle the bulk of the world rendering
'''
from cmu_graphics import *
import math
import player

# raycasting algorithms from https://lodev.org/cgtutor/raycasting.html

def render(width, height, player, map):
    for x in range(0, width, 1):
        adjX = (2 * x / width) - 1
        rayDirX = player.dirX + adjX * player.planeX
        rayDirY = player.dirY + adjX * player.planeY
        dist, side = rayCast(rayDirX, rayDirY, player, map)
        drawVertLine(dist, side, height)

def rayCast(rayDirX, rayDirY, player, map):
    posX, posY = player.x, player.y
    mapX, mapY = int(posX), int(posY)
    stepX, stepY = sign(rayDirX), sign(rayDirY)
    deltaDistX = math.inf if rayDirX == 0 else (1 / rayDirX)
    deltaDistY = math.inf if rayDirY == 0 else (1 / rayDirY)
    totalDistX = stepX * (posX - mapX - (stepX-1)//2) * deltaDistX
    totalDistY = stepY * (posY - mapY - (stepY-1)//2) * deltaDistY
    side = 0
    hit = False
    while (not hit):
        if totalDistX > totalDistY:
            mapY += stepY
            totalDistY += deltaDistY
            side = 1
        else:
            mapX += stepX
            totalDistX += deltaDistX
            side = 0
        
        if map[mapX][mapY] > 0:
            hit = True
    distance = (totalDistX - deltaDistX) if side == 0 else (totalDistY - deltaDistY)
    return distance, side

def sign(num):
    if num == 0: return 1
    return num // abs(num)