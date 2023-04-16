'''
This file will handle the bulk of the world rendering
'''
from cmu_graphics import *
import math

# raycasting algorithms from https://lodev.org/cgtutor/raycasting.html
resolution = 10
wallColors = ['slateGray', 'lightSlateGray']
ceilingColor = 'dimGray'
floorColor = rgb(186, 140, 99)

def render(width, height, player, map):
    drawRect(0, 0, width, height//2, fill=ceilingColor)
    drawRect(0, height//2, width, height, fill=floorColor)
    for x in range(0, width+1, resolution):
        adjX = (2 * x / width) - 1
        rayDirX = player.dirX + adjX * player.planeX
        rayDirY = player.dirY + adjX * player.planeY
        dist, side = rayCast(player.x, player.y, rayDirX, rayDirY, map)
        drawVertLine(x, dist, side, height)

def rayCast(posX, posY, dirX, dirY, map):
    mapX, mapY = int(posX), int(posY)
    deltaDistX = math.inf if dirX == 0 else abs(1 / dirX)
    deltaDistY = math.inf if dirY == 0 else abs(1 / dirY)
    stepX, stepY = sign(dirX), sign(dirY)
    totalDistX = stepX * (mapX - posX + (stepX == 1)) * deltaDistX
    totalDistY = stepY * (mapY - posY + (stepY == 1)) * deltaDistY
    side = 0
    hit = False
    while (not hit):
        if totalDistX >= totalDistY:
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
    lineHeight = int(height/dist) if dist != 0 else height
    top = max(-lineHeight/2 + height/2, 0)
    bottom = min(lineHeight/2 + height/2, height)
    color = wallColors[side]
    drawLine(x, top, x, bottom, fill=color, lineWidth=resolution)