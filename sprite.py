'''
will work on npc(enemies and friendly) stuff here

TO DO:
flesh out npc studff
add health, damage stuff
pathfinding
conversations
'''
import settings

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