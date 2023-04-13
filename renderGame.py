'''
This file will handle the bulk of the world rendering
'''
from cmu_graphics import *
import math

# raycasting algorithms from https://lodev.org/cgtutor/raycasting.html
resolution = 8

def render(width, height, player, map):
    for x in range(0, width, resolution):
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
    stepX, stepY = sign(rayDirX), sign(rayDirY)
    totalDistX = stepX * (mapX - posX + (stepX == 1)) * deltaDistX
    totalDistY = stepY * (mapY - posY + (stepY == 1)) * deltaDistY
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
    if num < 0: return -1
    else: return 1

def drawVertLine(x, dist, side, height):
    lineHeight = int(height/dist)
    top = max(-lineHeight/2 + height/2, 0)
    bottom = min(lineHeight/2 + height/2, height)
    color = 'blue' if side==0 else 'lightblue'
    drawLine(x, bottom, x, top, fill=color, lineWidth=resolution)