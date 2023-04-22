'''
minimap implementation

TO DO:
draw enemies and npcs to map (TP2)
'''

from cmu_graphics import *
import settings

# minimap inspired by CS Academy (Tetris) but with a few adjustments

class minimap:

    def __init__(self, left, top, width, height):
        map = settings.map
        self.rows, self.cols = len(map), len(map[0])
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.tileWidth = self.width / self.cols
        self.tileHeight = self.height / self.rows
        self.borderWidth = 1

    def __str__(self):
        return f"map at ({self.left, self.top} with {self.rows} rows and {self.cols} cols)"
    
    def getTileCorner(self, row, col):
        tileLeft = self.left + col * self.tileWidth
        tileTop = self.top + row * self.tileHeight
        return (tileLeft, tileTop)
    
    # convert game coords to minimap coords
    def convertToBoardCoords(self, posX, posY):
        boardX = self.left + posX * self.tileWidth
        boardY = self.top + posY * self.tileHeight
        return (boardX, boardY)
    
    def drawBorder(self):
        drawRect(self.left, self.top, self.width, self.height,
           fill=None, border='black',
           borderWidth=2*self.borderWidth)
        
    def drawTile(self, row, col, color):
        tileLeft, tileTop = self.getTileCorner(row, col)
        drawRect(tileLeft, tileTop, self.tileWidth, self.tileHeight,
             fill=color, border='black',
             borderWidth=self.borderWidth)
        
    # draws player on minimap
    def drawPlayer(self):
        player = settings.player
        scale = 0.5 * self.tileWidth
        posX, posY = self.convertToBoardCoords(player.x, player.y)
        dirPlaneX, dirPlaneY = posX + scale * player.dirX, posY + scale * player.dirY

        drawCircle(posX, posY, 0.4*scale)
        drawLine(posX, posY, dirPlaneX, dirPlaneY)

        planeLX, planeLY = dirPlaneX - scale * player.planeX, dirPlaneY - scale * player.planeY
        planeRX, planeRY = dirPlaneX + scale * player.planeX, dirPlaneY + scale * player.planeY
        drawLine(dirPlaneX, dirPlaneY, planeLX, planeLY)
        drawLine(dirPlaneX, dirPlaneY, planeRX, planeRY)
        drawLine(posX, posY, planeLX, planeLY)
        drawLine(posX, posY, planeRX, planeRY)

    # draws every enemy as a red circle on the map
    def drawEnemies(self):
        enemyList = settings.enemyList
        for sprite in enemyList:
            spriteX, spriteY = self.convertToBoardCoords(sprite.x, sprite.y)
            drawCircle(spriteX, spriteY, 0.15*self.tileWidth, fill='red')
        
    def drawMap(self):
        map = settings.map
        for col in range(self.cols):
            for row in range(self.rows):
                color = 'blue' if map[col][row] == 1 else 'white'
                self.drawTile(row, col, color)
        self.drawPlayer()
        self.drawEnemies()

class statusBars:

    def __init__(self, left, top, width, height, barWidth, textSize):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.barWidth = barWidth
        self.textSize = textSize
        self.colors = ['red', 'green', 'yellow']
        self.labels = ['HP', 'ST', 'SP']

    def __str__(self):
        return f"status bars at ({self.left, self.top}) with bar width {self.barWidth}"
    
    # draw individual bar
    def drawBar(self, pos, val, maxVal):
        # get left of bar
        if pos == 0: left = self.left
        elif pos == 1: left = self.left + self.width/2 - self.barWidth/2
        else: left = self.left + self.width - self.barWidth
        # get bar heights
        maxBarHeight = self.height-self.textSize
        barHeight = (val/maxVal)*maxBarHeight
        # get top of bar
        maxBarTop = self.top+self.textSize
        barTop = maxBarTop + (maxBarHeight-barHeight)
        # draw status bar
        drawLabel(self.labels[pos], left+self.barWidth/2, self.top+self.textSize/2, size=self.textSize)
        drawRect(left, maxBarTop, self.barWidth, maxBarHeight, fill=None, borderWidth=1)
        drawRect(left, barTop, self.barWidth, barHeight, fill=self.colors[pos], borderWidth=0)

    # draw all three bars
    def drawBars(self):
        # draw background
        drawRect(self.left, self.top, self.width, self.height, fill='white')
        # get bar values
        player = settings.player
        barVals = [player.health, player.stamina, player.special]
        maxBarVals = [settings.maxHealth, settings.maxStamina, settings.maxSpecial]
        # draw each bar
        for i in range(3):
            self.drawBar(i, barVals[i], maxBarVals[i])

