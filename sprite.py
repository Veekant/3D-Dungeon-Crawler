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
import utilities
import time

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
        return self.distToPlayer() == other.distToPlayer()
    
    def __lt__(self, other):
        if not isinstance(other, sprite): return False
        return self.distToPlayer() < other.distToPlayer()
    
    # gets distance to player
    def distToPlayer(self):
        player = settings.player
        return utilities.distance(self.x, self.y, player.x, player.y)

class enemy(sprite):

    def __init__(self, x, y, hScale, wScale, vScale, textureID):
        super().__init__(x, y, hScale, wScale, vScale, textureID)
        self.attackTimer = time.time()
        settings.enemyList.append(self)

    def update(self):
        player = settings.player
        self.moveToPlayer(player)
        self.attack(player)

    def moveToPlayer(self, player):
        pos = (self.x, self.y)
        cameraPos = (player.x + player.dirX, player.y+player.dirY)
        path = pathfinding.findPath(pos, cameraPos)
        if path != None and len(path)-1 <= settings.aggroDistance:
            target = (path[1][0] + 0.5, path[1][1] + 0.5) if len(path)>1 else cameraPos
            if self.distToPlayer() > settings.enemyAttackRange:
                self.moveToPoint(target)

    def moveToPoint(self, point):
        x, y = point[0], point[1]
        distX, distY = (x - self.x), (y - self.y)
        dx, dy = utilities.normalizeVector((distX, distY))
        self.moveAxis(dx, dy)

    def moveAxis(self, dx, dy):
        self.x += settings.enemySpeed * dx
        self.y += settings.enemySpeed * dy

    def attack(self, player):
        if self.distToPlayer() < settings.enemyAttackRange:
            if time.time() - self.attackTimer >= settings.enemyAttackCooldown: 
                player.attacked(self)
                self.attackTimer = time.time()