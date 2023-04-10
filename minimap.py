'''
minimap implementation
'''

from cmu_graphics import *

# a lot of the following code is taken from CS Academy
# specifically, the Tetris assignment

class minimap:

    def __init__(self, map, player, left, top, width, height):
        self.map = map
        self.rows, self.cols = len(map), len(map[0])
        self.player = player
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.borderWidth = 1

    def __str__(self):
        return f"map at ({self.left, self.top} with {self.rows} rows and {self.cols} cols)"
    
    def getTileSize(self):
        tileWidth = self.width / self.cols
        tileHeight = self.height / self.rows
        return (tileWidth, tileHeight)
    
    def getTileCorner(self, row, col):
        tileWidth, tileHeight = self.getTileSize()
        tileLeft = self.left + col * tileWidth
        tileTop = self.top + row * tileHeight
        return (tileLeft, tileTop)
    
    def getPlayerPos(self):
        tileWidth, tileHeight = self.getTileSize()
        playerX = self.left + self.player.x * tileWidth
        playerY = self.top + self.player.y * tileHeight
        return (playerX, playerY)
    
    def drawBorder(self):
        drawRect(self.left, self.top, self.width, self.height,
           fill=None, border='black',
           borderWidth=2*self.borderWidth)
        
    def drawTile(self, row, col, color):
        tileLeft, tileTop = self.getTileCorner(row, col)
        tileWidth, tileHeight = self.getTileSize()
        drawRect(tileLeft, tileTop, tileWidth, tileHeight,
             fill=color, border='black',
             borderWidth=self.borderWidth)
        
    def drawPlayer(self):
        scale = 0.05 * self.width
        posX, posY = self.getPlayerPos()
        dirPlaneX, dirPlaneY = posX + scale * self.player.dirX, posY + scale * self.player.dirY
        planeLX, planeLY = dirPlaneX - scale * self.player.planeX, dirPlaneY - scale * self.player.planeY
        planeRX, planeRY = dirPlaneX + scale * self.player.planeX, dirPlaneY + scale * self.player.planeY

        drawCircle(posX, posY, 0.5*scale)

        drawLine(posX, posY, dirPlaneX, dirPlaneY)

        drawLine(dirPlaneX, dirPlaneY, planeLX, planeLY)
        drawLine(dirPlaneX, dirPlaneY, planeRX, planeRY)

        drawLine(posX, posY, planeLX, planeLY)
        drawLine(posX, posY, planeRX, planeRY)
        
    def drawMap(self):
        for row in range(self.rows):
            for col in range(self.cols):
                color = 'blue' if self.map[row][col] == 1 else 'white'
                self.drawTile(row, col, color)
        self.drawPlayer()