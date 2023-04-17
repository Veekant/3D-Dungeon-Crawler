'''
This file will handle the bulk of the world rendering

TO DO:
sprite rendering (TP1/2)
texture rendering (TP3)
floor/ceiling rendering (TP3)

'''
from cmu_graphics import *
import math

# raycasting algorithms from https://lodev.org/cgtutor/raycasting.html

# initialize basic rendering vars (will move into settings later)
resolution = 8
maxViewDistance = 150
wallColors = ['slateGray', 'lightSlateGray']
ceilingColor = 'dimGray'
floorColor = rgb(186, 140, 99)

# basic render function
def render(width, height, player, map):
    # draw floor and ceiling
    drawRect(0, 0, width, height//2, fill=ceilingColor)
    drawRect(0, height//2, width, height, fill=floorColor)
    # loop through pixel x-values on screen
    for x in range(0, width+1, resolution):
        # shift x-values so they go from -1 to 1
        adjX = (2 * x / width) - 1
        # determine ray direction
        rayDirX = player.dirX + adjX * player.planeX
        rayDirY = player.dirY + adjX * player.planeY
        # cast ray and draw line
        dist, side = rayCast(player.x, player.y, rayDirX, rayDirY, map)
        drawVertLine(x, dist, side, height)

# function that handles casting 1 ray
def rayCast(posX, posY, dirX, dirY, map):
    # get map tile to check
    mapX, mapY = int(posX), int(posY)
    # get direction to check tiles in 
    stepX, stepY = sign(dirX), sign(dirY)
    # get distance between successive x and y intersections
    deltaDistX = math.inf if dirX == 0 else abs(1 / dirX)
    deltaDistY = math.inf if dirY == 0 else abs(1 / dirY)
    # initialize total distance vars as distance to first x and y intersections
    totalDistX = stepX * (mapX - posX + (stepX == 1)) * deltaDistX
    totalDistY = stepY * (mapY - posY + (stepY == 1)) * deltaDistY
    # initialize side hit and hit condition
    side = 0
    hit = False
    # while wall not hit
    while (not hit):
        # increment shorter distance
        if totalDistX >= totalDistY:
            mapY += stepY
            totalDistY += deltaDistY
            side = 1
        else:
            mapX += stepX
            totalDistX += deltaDistX
            side = 0
        # if wall is hit, exit loop
        if map[mapX][mapY] > 0:
            hit = True
    # calculate perp wall distance (removes fisheye)
    dist = (totalDistX - deltaDistX) if side == 0 else (totalDistY - deltaDistY)
    return dist, side

# helper function that returns sign
def sign(num):
    if num < 0: return -1
    else: return 1

# draw vertical line on screen
def drawVertLine(x, dist, side, height):
    # calculate line of height
    lineHeight = int(height/dist) if dist != 0 else math.inf
    # find top and bottom of line
    top = max(-lineHeight/2 + height/2, 0)
    bottom = min(lineHeight/2 + height/2, height)
    # get color
    color = wallColors[side]
    # draw line
    drawLine(x, top, x, bottom, fill=color, lineWidth=resolution)