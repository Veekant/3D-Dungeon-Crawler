'''
This file will handle the bulk of the world rendering

TO DO:
texture rendering (TP3)
floor/ceiling rendering (TP3)

'''
from pyglet import *
import settings
import utilities
import math

# base raycasting algorithm from https://lodev.org/cgtutor/raycasting.html
# sprite raycasting algorithm from https://lodev.org/cgtutor/raycasting3.html

# initialize basic rendering vars (will move into settings later)
resolution = 6
maxViewDistance = 150
wallColors = [(112, 128, 144, 255), (119, 136, 153, 255)]
ceilingColor = (60, 70, 75, 255)
floorColor = (133, 94, 66, 255)

# main render function
def render():
    width, height = settings.width, settings.height
    player, map = settings.player, settings.map

    mainBatch = graphics.Batch()
    bg = graphics.Group(order=0)
    walls = graphics.Group(order=1)
    sprites = graphics.Group(order=2)

    # draw floor and ceiling
    floor = shapes.Rectangle(0, 0, width, height//2, color=floorColor, batch=mainBatch, group=bg)
    ceiling = shapes.Rectangle(0, height//2, width, height//2, color=ceilingColor, batch=mainBatch, group=bg)
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
        dist, side, wallVal, wallX = rayCast(player.x, player.y, rayDirX, rayDirY, map, zBuffer)
        line = drawVertLine(mainBatch, walls, x, height, dist, side, wallVal, wallX, rayDirX, rayDirY)
        lineList.append(line)
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
    if side == 0: wallX = (posY + dist * dirY) % 1
    else: wallX = (posX + dist * dirX) % 1
    
    return dist, side, map[mapX][mapY], wallX

# helper function that returns sign
def sign(num):
    if num < 0: return -1
    else: return 1

# draw vertical line on screen
def drawVertLine(batch, group, x, height, dist, side, wallVal, wallX, rayDirX, rayDirY):
    # calculate line of height
    lineHeight = height/dist if dist != 0 else math.inf
    # find top and bottom of line
    bottom = max(-lineHeight/2 + height/2, 0)
    top = min(lineHeight/2 + height/2, height)
    # draw line
    texImg = settings.texFiles[wallVal-1]
    texX = int(wallX * texImg.width)
    if(side == 0 and rayDirX > 0): texX = texImg.width - texX - 1
    if(side == 1 and rayDirY < 0): texX = texImg.width - texX - 1

    # get image slice, scale, and draw
    scale = lineHeight / texImg.height
    minWidth = 1 if dist <= 4 else 2
    lineImgWidth = max(resolution/scale, minWidth)
    texStart = (bottom + lineHeight/2 - height/2) * (1/scale)
    lineImg = texImg.get_region(texX, texStart, lineImgWidth, texImg.height)
    lineSprite = sprite.Sprite(lineImg, x, bottom, subpixel=True, batch=batch, group=group)
    lineSprite.scale = scale
    # vertLine = shapes.Line(x, bottom, x, top, width=resolution, color=color, batch=batch)
    return lineSprite

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

        spriteImg = settings.spriteFiles[sprite.texID]

        # calculate width and height of sprite
        spriteWidth = abs(width / spriteCameraY) / sprite.scale
        spriteLeft = max(-spriteWidth/2 + spriteScreenX, 0)
        spriteRight = min(spriteWidth/2 + spriteScreenX, width)

        spriteHeight = spriteWidth * (spriteImg.height/spriteImg.width)
        spriteBottom = max(-spriteHeight/2 + height/2 + vertScaleScreen, 0)
        spriteTop = min(spriteHeight/2 + height/2 + vertScaleScreen, height)

        drawSprite(spriteImg, spriteCameraY, spriteLeft, spriteRight, 
                       spriteBottom, spriteTop, spriteWidth, spriteScreenX, buffer)

# draw individual sprite
def drawSprite(img, depth, left, right, bottom, top, width, center, buffer):
    spriteBatch = graphics.Batch()
    scale = img.height/(top-bottom)
    stripeStartIndex = 0
    stripeList = []
    # loop through x values
    for x in range(int(left), int(right), resolution):
        # if in front of camera, draw line
        if (0 < depth <= buffer[x]):
            # get image slice, scale, and draw
            texX = (x + width/2 - center) * (img.width/width)
            imgStripeWidth = max(int(scale * resolution), 1)
            stripeImg = img.get_region(texX, 0, imgStripeWidth, img.height)
            stripeSprite = sprite.Sprite(stripeImg, x, bottom, batch=spriteBatch)
            stripeSprite.scale = 1/scale
            stripeList.append(stripeSprite)
        stripeStartIndex += 1
    spriteBatch.draw()
