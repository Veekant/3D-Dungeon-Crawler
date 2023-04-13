'''
This file will handle the bulk of the world rendering
'''
from cmu_graphics import *
import math
import player

# raycasting algorithms from https://lodev.org/cgtutor/raycasting.html

def render(width, height, player, map):
    for x in range(0, width, 4):
        adjX = (2 * x / width) - 1
        rayDirX = player.dirX + adjX * player.planeX
        rayDirY = player.dirY + adjX * player.planeY
        dist, side = rayCast(rayDirX, rayDirY, player, map)
        drawVertLine(x, dist, side, height)

def rayCast(rayDirX, rayDirY, player, map):
    posX, posY = player.x, player.y
    mapX, mapY = int(posX), int(posY)
    deltaDistX = math.inf if rayDirX == 0 else abs(1 / rayDirX)
    deltaDistY = math.inf if rayDirY == 0 else abs(1 / rayDirY)
    '''
    if rayDirX >= 0:
        stepX = 1
        totalDistX = (mapX + 1 - posX) * deltaDistX
    else:
        stepX = -1
        totalDistX = (posX - mapX) * deltaDistX
    if rayDirY >= 0:
        stepY = 1
        totalDistY = (mapY + 1 - posY) * deltaDistY
    else:
        stepY = -1
        totalDistY = (posY - mapY) * deltaDistY
    '''
    stepX, stepY = sign(rayDirX), sign(rayDirY)
    totalDistX = stepX * (mapX - posX + (stepX+1)//2) * deltaDistX
    totalDistY = stepY * (mapY - posY + (stepY+1)//2) * deltaDistY
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
    dist = (totalDistX - deltaDistX) if side == 0 else (totalDistY - deltaDistY)
    return dist, side

def sign(num):
    if num == 0: return 1
    return int(num // abs(num))

def drawVertLine(x, dist, side, height):
    lineHeight = int(height/dist)
    top = max(-lineHeight/2 + height/2, 0)
    bottom = min(lineHeight/2 + height/2, height)
    drawLine(x, bottom, x, top, fill='blue', lineWidth=4)