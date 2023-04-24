'''
This file will handle the bulk of the world rendering

TO DO:
texture rendering (TP3)
floor/ceiling rendering (TP3)

'''
from cmu_graphics import *
from pyglet import *
import settings
import utilities
import math

# base raycasting algorithm from https://lodev.org/cgtutor/raycasting.html
# sprite raycasting algorithm from https://lodev.org/cgtutor/raycasting3.html

# initialize basic rendering vars (will move into settings later)
resolution = 4
maxViewDistance = 150
wallColors = [(112, 128, 144, 255), (119, 136, 153, 255)]
ceilingColor = (105, 105, 105, 255)
floorColor = (186, 140, 99, 255)

# main render function
def render():
    width, height = settings.width, settings.height
    player, map = settings.player, settings.map
    mainBatch = graphics.Batch()
    # draw floor and ceiling
    floor = shapes.Rectangle(0, 0, width, height//2, color=floorColor, batch=mainBatch)
    ceiling = shapes.Rectangle(0, height//2, width, height//2, color=ceilingColor, batch=mainBatch)
    zBuffer = []
    lineList = []
    # loop through pixel x-values on screen
    for x in range(0, width+1, resolution):
        # shift x-values so they go from -1 to 1
        adjX = (2 * x / width) - 1
        # determine ray direction
        rayDirX = player.dirX + adjX * player.planeX
        rayDirY = player.dirY + adjX * player.planeY
        # cast ray and draw line
        dist, side = rayCast(player.x, player.y, rayDirX, rayDirY, map, zBuffer)
        drawVertLine(x, dist, side, height, lineList, mainBatch)
    mainBatch.draw()
    
    drawSprites(width, height, player, zBuffer)

# function that handles casting 1 ray
def rayCast(posX, posY, dirX, dirY, map, buffer):
    # get map tile to check
    mapX, mapY = int(posX), int(posY)
    # get direction to check tiles in 
    stepX, stepY = utilities.sign(dirX), utilities.sign(dirY)
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
    # add dist to buffer
    buffer.extend([dist] * resolution)
    return dist, side

# helper function that returns sign
def sign(num):
    if num < 0: return -1
    else: return 1

# draw vertical line on screen
def drawVertLine(x, dist, side, height, lineList, batch):
    # calculate line of height
    lineHeight = height/dist if dist != 0 else math.inf
    # find top and bottom of line
    top = max(-lineHeight/2 + height/2, 0)
    bottom = min(lineHeight/2 + height/2, height)
    # get color
    color = wallColors[side]
    # draw line
    vertLine = shapes.Line(x, bottom, x, top, width=resolution, color=color, batch=batch)
    lineList.append(vertLine)

# draws all sprites to the screen
def drawSprites(width, height, player, buffer):
    # sort the sprite list by distance
    spriteList = sorted(settings.spriteList, reverse=True)
    # loop through all sprites
    for sprite in spriteList:
        # calculate distance to player
        spriteDistX, spriteDistY = (sprite.x - player.x), (sprite.y - player.y)
        # determine coords on camera using matrix
        coeff = 1 / (player.planeX*player.dirY - player.dirX*player.planeY)
        spriteCameraX = coeff * (spriteDistX*player.dirY - spriteDistY*player.dirX)
        spriteCameraY = coeff * (-spriteDistX*player.planeY + spriteDistY*player.planeX)
        # convert to screen coords
        spriteScreenX = (width/2) * (1 + spriteCameraX / spriteCameraY)

        # scale factor
        vertScaleScreen = -sprite.vertScale / spriteCameraY

        # calculate width and height of sprite
        spriteWidth = abs(width / spriteCameraY) / sprite.widthScale
        spriteLeft = max(-spriteWidth/2 + spriteScreenX, 0)
        spriteRight = min(spriteWidth/2 + spriteScreenX, width)

        spriteHeight = abs(height / spriteCameraY) / sprite.heightScale
        spriteBottom = max(-spriteHeight/2 + height/2 + vertScaleScreen, 0)
        spriteTop = min(spriteHeight/2 + height/2 + vertScaleScreen, height)

        drawSprite(sprite.texID, width, spriteCameraY, spriteLeft, spriteRight, spriteBottom, spriteTop, buffer)

# draw individual sprite
def drawSprite(spriteID, width, depth, left, right, bottom, top, buffer):
    spriteBatch = graphics.Batch()
    lineList = []
    # loop through x values
    for x in range(int(left), int(right)+1, resolution):
        # if in front of camera, draw line
        if (0 < depth <= buffer[x]):
            vertLine = shapes.Line(x, bottom, x, top, width=resolution, color=(0,255,0,255), batch=spriteBatch)
            lineList.append(vertLine)
    spriteBatch.draw()
