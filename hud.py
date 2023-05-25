'''
minimap implementation

TO DO:
draw enemies and npcs to map (TP2)
'''

from pyglet import *
import settings

black = (0, 0, 0, 255)
red = (255, 0, 0, 255)
green = (0, 255, 0, 255)
blue = (0, 0, 255, 255)
yellow = (255, 255, 0)
white = (255, 255, 255, 255)

# minimap inspired by CS Academy (Tetris) but with a few adjustments
class minimap:

    def __init__(self, left, bottom, width, height):
        map = settings.map
        self.rows, self.cols = len(map), len(map[0])
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
        self.tileWidth = self.width / self.cols
        self.tileHeight = self.height / self.rows
        self.borderWidth = 1

    def __str__(self):
        return f"map at ({self.left, self.bottom} with {self.rows} rows and {self.cols} cols)"
    
    def getTileCorner(self, col, row):
        tileLeft = self.left + col * self.tileWidth
        tileBottom = self.bottom + (self.rows-row-1) * self.tileHeight
        return (tileLeft, tileBottom)
    
    # convert game coords to minimap coords
    def convertToBoardCoords(self, posX, posY):
        boardX = self.left + posX * self.tileWidth
        boardY = self.bottom + (self.rows-posY) * self.tileHeight
        return (boardX, boardY)
    
    def drawBorder(self, batch):
        border = shapes.BorderedRectangle(self.left, self.bottom, self.width, self.height, 
                                          border=2*self.borderWidth, color=white, 
                                          border_color=black, batch=batch)
        border.opacity = 0
        return border
        
    def drawTile(self, batch, col, row, color):
        tileLeft, tileBottom = self.getTileCorner(col, row)
        tile = shapes.BorderedRectangle(tileLeft, tileBottom, self.tileWidth, self.tileHeight, 
                                          border=self.borderWidth, color=color, 
                                          border_color=black, batch=batch)
        return tile
        
    # draws player on minimap
    def drawPlayer(self, batch):
        player = settings.player
        scale = 0.5 * self.tileWidth
        posX, posY = self.convertToBoardCoords(player.x, player.y)
        dirX, dirY = posX + 2*scale * player.dirX, posY - 2*scale * player.dirY
        posLX, posLY = posX - scale * player.planeX, posY + scale * player.planeY
        posRX, posRY = posX + scale * player.planeX, posY - scale * player.planeY
        playerIndicator = shapes.Triangle(dirX, dirY, posLX, posLY, posRX, posRY,
                                          color=black, batch=batch)
        return playerIndicator

    # draws every enemy as a red circle on the map
    def drawEnemies(self, batch):
        enemyDotList = []
        enemyList = settings.enemyList
        for sprite in enemyList:
            spriteX, spriteY = self.convertToBoardCoords(sprite.x, sprite.y)
            enemyDot = shapes.Circle(spriteX, spriteY, 0.15*self.tileWidth, 
                                     color=red, batch=batch)
            enemyDotList.append(enemyDot)
        return enemyDotList
        
    def drawMap(self, batch):
        map = settings.map
        border = self.drawBorder(batch)
        tileList = []
        for col in range(self.cols):
            for row in range(self.rows):
                color = blue if map[col][row] > 0 else white
                tile = self.drawTile(batch, col, row, color)
                tileList.append(tile)
        return border, tileList

    def draw(self, batch):
        border, tileList = self.drawMap(batch)
        playerIndicator = self.drawPlayer(batch)
        enemyDotList = self.drawEnemies(batch)
        return (border, tileList, playerIndicator, enemyDotList)

class statusBars:

    def __init__(self, left, bottom, width, height, barWidth, textSize):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
        self.barWidth = barWidth
        self.textSize = textSize
        self.colors = [red, green, yellow]
        self.labels = ['HP', 'ST', 'SP']

    def __str__(self):
        return f"status bars at ({self.left, self.top}) with bar width {self.barWidth}"
    
    # draw individual bar
    def drawBar(self, batch, pos, val, maxVal):
        # get left of bar
        if pos == 0: left = 2 + self.left
        elif pos == 1: left = self.left + self.width/2 - self.barWidth/2
        else: left = self.left + self.width - self.barWidth - 2
        # get bar heights
        maxBarHeight = self.height-self.textSize
        barHeight = (val/maxVal)*maxBarHeight
        # bruh
        label = text.Label(self.labels[pos], font_name='Times New Roman',
                          font_size=self.textSize, bold=True,
                          x=left+self.barWidth//2, y=self.bottom+2,
                          anchor_x='center', anchor_y='bottom',
                          batch=batch)
        bar = shapes.Rectangle(left, self.bottom+2, self.barWidth, barHeight,
                               color=self.colors[pos], batch=batch)
        barOutline = shapes.BorderedRectangle(left, self.bottom+2, self.barWidth, maxBarHeight,
                                              border=2, color=white, border_color=black,
                                              batch=batch)
        barOutline.opacity = 0
        return (label, barOutline, bar)

    # draw all three bars
    def drawBars(self, batch):
        barList = []
        # draw background
        background = shapes.BorderedRectangle(self.left, self.bottom, self.width, self.height,
                                              border=2, color=white, border_color=black,
                                              batch=batch)
        # get bar values
        player = settings.player
        barVals = [player.health, player.stamina, player.special]
        maxBarVals = [settings.maxHealth, settings.maxStamina, settings.maxSpecial]
        # draw each bar
        for i in range(3):
            bar = self.drawBar(batch, i, barVals[i], maxBarVals[i])
            barList.append(bar)
        return barList

def drawSword(batch, attacking):
    # draw cool sword thing
    swordImg = settings.spriteFiles[7]
    swordImg.anchor_x, swordImg.anchor_y = swordImg.width//2, 0
    if attacking:
        posX = settings.width // 3
        posY = -90
        rotation = -50
        scale = 0.9
    else:
        posX = 3 * settings.width // 4
        posY = -100
        rotation = 10
        scale = 1.2
    swordSprite = sprite.Sprite(swordImg, posX, posY, batch=batch)
    swordSprite.scale = scale
    swordSprite.rotation = rotation
    return swordSprite

def draw():
    hudBatch = graphics.Batch()
    sword = drawSword(hudBatch, settings.player.attacking)
    (border, tileList, playerIndicator, enemyDotList) = settings.minimap.draw(hudBatch)
    bars = settings.statusBars.drawBars(hudBatch)
    hudBatch.draw()

