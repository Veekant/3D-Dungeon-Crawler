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

    def __init__(self, x, y, textureID):
        self.x = x
        self.y = y
        self.texID = textureID
        settings.spriteList.append(self)
    
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

    def __init__(self, x, y, textureID):
        super().__init__(x, y, textureID)