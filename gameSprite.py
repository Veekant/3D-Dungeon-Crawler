'''
contains sprite and enemy classes
'''

import settings
import pathfinding
import utilities
import gameplay
import time

class sprite:

    def __init__(self, x, y, scale, vScale, textureID):
        self.x = x
        self.y = y
        self.scale = scale
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

    def __init__(self, x, y, scale, vScale, textureID):
        super().__init__(x, y, scale, vScale, textureID)
        self.attackTimer = time.time()
        self.pathfinding = False
        self.snarlTimer = time.time()
        self.health = settings.enemyHealth
        settings.enemyList.append(self)

    def update(self, dt):
        player = settings.player
        # handle movement
        self.moveToPlayer(player, dt)
        # handle attacking
        self.attack(player, dt)
        # handle sound
        self.playSnarl()

    def moveToPlayer(self, player, dt):
        # finds path to player
        pos = (self.x, self.y)
        cameraPos = (player.x + player.dirX, player.y+player.dirY)
        path = pathfinding.findPath(pos, cameraPos)
        # if path exists and player is close enough:
        if path != None and len(path)-1 <= settings.aggroDistance:
            self.pathfinding = True
            # move towards target
            target = (path[1][0] + 0.5, path[1][1] + 0.5) if len(path)>1 else cameraPos
            if self.distToPlayer() > settings.enemyAttackRange:
                self.moveToPoint(target, dt)
        else:
            self.pathfinding = False

    # moves in direction of point
    def moveToPoint(self, point, dt):
        # get location and dist vectors
        x, y = point[0], point[1]
        distX, distY = (x - self.x), (y - self.y)
        # normalize vector and scale
        dirX, dirY = utilities.normalizeVector((distX, distY))
        dx = settings.enemySpeed * dt * dirX
        dy = settings.enemySpeed * dt * dirY  
        self.moveAxis(dx, dy)

    # moves along axes
    def moveAxis(self, dx, dy):
        self.x += dx
        self.y += dy

    # attacks player if within range and cooldown not active
    def attack(self, player, dt):
        if self.distToPlayer() < settings.enemyAttackRange:
            if time.time() - self.attackTimer >= settings.enemyAttackCooldown: 
                player.attacked(self)
                self.attackTimer = time.time()
    
    # snarls at player if targeting and enough time has elapsed
    def playSnarl(self):
        currentTime = time.time()
        if self.pathfinding and currentTime-self.snarlTimer > settings.enemySnarlFrequency:
            settings.sfxFiles[1].play()
            self.snarlTimer = currentTime

    # handles being attacked
    def attacked(self, player):
        settings.sfxFiles[8].play()
        # takes damage
        self.health -= settings.damage
        # kill enemy if health at 0
        if self.health <= 0: self.die()

        # calculate knockback
        enemyDistVec = (self.x-player.x, self.y-player.y)
        normDistVec = utilities.normalizeVector(enemyDistVec)
        knockbackVec = utilities.vecMultiply(settings.enemyKnockback, normDistVec)
        gameplay.moveAxis(self, knockbackVec[0], knockbackVec[1])
    
    # kills enemy by removing from lists
    def die(self):
        settings.sfxFiles[2].play()
        settings.spriteList.remove(self)
        settings.enemyList.remove(self)