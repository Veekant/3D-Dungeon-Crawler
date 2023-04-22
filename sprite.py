'''
will work on npc(enemies and friendly) stuff here

TO DO:
flesh out npc studff
add health, damage stuff
pathfinding
conversations
'''
import settings
import pathfinding

class sprite:

    def __init__(self, x, y, hScale, wScale, vScale, textureID):
        self.x = x
        self.y = y
        self.heightScale = hScale
        self.widthScale = wScale
        self.vertScale = vScale
        self.texID = textureID
        settings.spriteList.append(self)
    
    def __str__(self):
        return f"ID:{self.texID}, pos:({self.x},{self.y}))"

    # methods for sorting
    def __eq__(self, other):
        if not isinstance(other, sprite): return False
        return self.distToPlayer == other.distToPlayer
    
    def __lt__(self, other):
        if not isinstance(other, sprite): return False
        return self.distToPlayer < other.distToPlayer
    
    # gets distance to player
    def distToPlayer(self):
        player = settings.player
        return ((self.x-player.x)**2 + (self.y-player.y)**2)**0.5

class character(sprite):

    def __init__(self, x, y, hScale, wScale, vScale, textureID):
        super().__init__(x, y, hScale, wScale, vScale, textureID)
        settings.enemyList.append(self)

    def moveToPoint(self, point):
        x, y = point[0], point[1]
        dx, dy = character.sign(x - self.x), character.sign(y - self.y)
        self.move(dx, dy)

    def move(self, dx, dy):
        if dx == 0 or dy == 0:
            self.x += dx * 0.01
            self.y += dy * 0.01
        else:
            self.x += dx * (0.01 / 2**0.5)
            self.y += dy * (0.01 / 2**0.5)

    def update(self):
        if self.distToPlayer() < 10:
            player = settings.player
            pos = (self.x, self.y)
            playerPos = (player.x, player.y)
            path = pathfinding.findPath(pos, playerPos)
            if path != None:
                target = (path[1][0] + 0.5, path[1][1] + 0.5) if len(path)>1 else playerPos
                self.moveToPoint(target)
    
    @staticmethod
    def sign(num):
        if num > 0: return 1
        if num < 0: return -1
        return 0
