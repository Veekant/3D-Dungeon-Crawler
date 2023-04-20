'''
minimap implementation

TO DO:
draw enemies and npcs to map (TP2)
'''

from cmu_graphics import *
import settings

# code inspired by CS Academy (Tetris) but with a few adjustments

class minimap:

    def __init__(self, map, left, top, width, height):
        self.map = map
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

    def drawPlayer(self):
        player = settings.player
        scale = 0.5 * self.tileWidth
        posX, posY = self.convertToBoardCoords(player.x, player.y)
        dirPlaneX, dirPlaneY = posX + scale * player.dirX, posY + scale * player.dirY

        drawCircle(posX, posY, 0.5*scale)
        drawLine(posX, posY, dirPlaneX, dirPlaneY)

        '''
        planeLX, planeLY = dirPlaneX - scale * player.planeY, dirPlaneY - scale * player.planeX
        planeRX, planeRY = dirPlaneX + scale * player.planeY, dirPlaneY + scale * player.planeX
        drawLine(dirPlaneX, dirPlaneY, planeLX, planeLY)
        drawLine(dirPlaneX, dirPlaneY, planeRX, planeRY)
        drawLine(posX, posY, planeLX, planeLY)
        drawLine(posX, posY, planeRX, planeRY)
        '''

    def drawSprites(self):
        spriteList = settings.spriteList
        for sprite in spriteList:
            spriteX, spriteY = self.convertToBoardCoords(sprite.x, sprite.y)
            drawCircle(spriteX, spriteY, 0.15*self.tileWidth, fill='red')
        
    def drawMap(self):
        for col in range(self.cols):
            for row in range(self.rows):
                color = 'blue' if self.map[col][row] == 1 else 'white'
                self.drawTile(row, col, color)
        self.drawPlayer()
        self.drawSprites()