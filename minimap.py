'''
minimap implementation

TO DO:
draw enemies and npcs to map (TP2)
'''

from cmu_graphics import *

# code inspired by CS Academy (Tetris) but with a few adjustments

class minimap:

    def __init__(self, map, player, left, top, width, height):
        self.map = map
        self.rows, self.cols = len(map), len(map[0])
        self.player = player
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
    
    def getPlayerPos(self):
        playerX = self.left + self.player.x * self.tileWidth
        playerY = self.top + self.player.y * self.tileHeight
        return (playerX, playerY)
    
    def drawBorder(self):
        drawRect(self.left, self.top, self.width, self.height,
           fill=None, border='black',
           borderWidth=2*self.borderWidth)
        
    def drawTile(self, row, col, color):
        tileLeft, tileTop = self.getTileCorner(row, col)
        drawRect(tileLeft, tileTop, self.tileWidth, self.tileHeight,
             fill=color, border='black',
             borderWidth=self.borderWidth)

    def drawPlayer(self):
        scale = 0.5 * self.tileWidth
        posX, posY = self.getPlayerPos()
        dirPlaneX, dirPlaneY = posX + scale * self.player.dirX, posY + scale * self.player.dirY
        planeLX, planeLY = dirPlaneX - scale * self.player.planeY, dirPlaneY - scale * self.player.planeX
        planeRX, planeRY = dirPlaneX + scale * self.player.planeY, dirPlaneY + scale * self.player.planeX

        drawCircle(posX, posY, 0.5*scale)

        drawLine(posX, posY, dirPlaneX, dirPlaneY)
        '''
        drawLine(dirPlaneX, dirPlaneY, planeLX, planeLY)
        drawLine(dirPlaneX, dirPlaneY, planeRX, planeRY)
        drawLine(posX, posY, planeLX, planeLY)
        drawLine(posX, posY, planeRX, planeRY)
        '''
        
    def drawMap(self):
        for col in range(self.cols):
            for row in range(self.rows):
                color = 'blue' if self.map[col][row] == 1 else 'white'
                self.drawTile(row, col, color)
        self.drawPlayer()