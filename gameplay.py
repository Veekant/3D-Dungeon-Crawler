'''
might handle some input stuff here
'''

from pyglet import *
import settings
import pause
import death
import win
import player
import hud
import gameSprite
import renderGame
import utilities
import math
import time

footstepSoundTimer = 0

def onSwitch(resetGame):
    settings.window.set_exclusive_mouse(True)

    musicPlayer = settings.musicPlayer
    musicPlayer.queue(settings.musicFiles[3])
    musicPlayer.play()
    musicPlayer.volume = 0.6
    musicPlayer.loop = True

    if resetGame: reset()

def reset():
    settings.enemyList = []
    settings.spriteList = []
    settings.player = player.player(4, 22, -math.pi/2)
    settings.minimap = hud.minimap(settings.width-200, 0, 200, 200)
    settings.statusBars = hud.statusBars(0, 0, 300, 200, 75, 12)
    spawnEnemies()

def spawnEnemies():
    zombie1 = gameSprite.enemy(4, 16, 4, 400, 6)
    zombie2 = gameSprite.enemy(6, 3, 4, 400, 6)
    zombie3 = gameSprite.enemy(11, 20, 4, 400, 6)
    zombie4 = gameSprite.enemy(15, 20, 4, 400, 6)

    skeleton1 = gameSprite.enemy(9, 12, 2, 400, 5)
    skeleton2 = gameSprite.enemy(8, 20, 2, 400, 5)
    skeleton3 = gameSprite.enemy(3, 14, 2, 400, 5)

    druid1 = gameSprite.enemy(11, 14, 2, 400, 2)

def onKeyPress(key):
    if key == 'P':
        pauseGame()
    elif key == 'M':
        die()

def onKeyHold(keys, dt):
    dir = [0, 0]
    if keys[window.key.W]: dir[1] = 1
    elif keys[window.key.S]: dir[1] = -1
    if keys[window.key.A]: dir[0] = 1
    elif keys[window.key.D]: dir[0] = -1

    if dir != [0, 0]:
        # get dir vector and scale for velocity
        normDir = utilities.normalizeVector(dir)
        dr = settings.speed * dt
        dir = utilities.vecMultiply(dr, normDir)
        move(dir[0], dir[1])

def onMouseMove(mouseX, mouseY, dx, dy):
    dTheta = settings.sensitivity * math.atan2(dx/settings.width, 1)
    rotate(dTheta)

def onMousePress(mouseX, mouseY, button, modifiers):
    if button == window.mouse.LEFT:
        settings.player.attacking = True
        swordSound = settings.sfxFiles[7].play()
        swordSound.volume = 0.5
        attack()

def onMouseRelease(mouseX, mouseY, button):
    if button == window.mouse.LEFT and settings.player.attacking:
        settings.player.attacking = False

def onDraw():
    renderGame.render()
    hud.draw()

def update(dt, keys):
    onKeyHold(keys, dt)
    for enemy in settings.enemyList:
        enemy.update(dt)
    if settings.gameOver:
        die()
    if len(settings.enemyList) == 0:
        winGame()

# call player rotate method
def rotate(direction):
    player = settings.player
    player.rotate(direction)

# move player and check for collisions
def move(hor, vert):
    player = settings.player
    map = settings.map
    # edge case (for later)
    if hor == 0 and vert == 0: return
    # move player and check if position is legal
    player.move(hor, vert)
    if collisionValid(player):
        playFootstepSound()
        return
    # if illegal, return to original position
    player.move(-hor, -vert)

    # get direction components along axes
    dx = hor * player.dirX + vert * player.dirX
    dy = hor * player.dirY + vert * player.dirY
    moveAxis(player, dx, dy)

def moveAxis(entity, dx, dy):
    map = settings.map
    # check first axis
    entity.moveAxis(dx, 0)
    if collisionValid(entity): return
    # if failed, undo and try second axis
    entity.moveAxis(-dx, dy)
    if collisionValid(entity): return
    # if failed again, give up and cry probably
    entity.moveAxis(0, -dy)

def collisionValid(entity):
    map = settings.map
    player = settings.player
    # check map tile
    if map[int(entity.x)][int(entity.y)] > 0: return False
    # check each sprite and player
    for sprite in settings.spriteList:
        distToSprite = utilities.distance(player.x, player.y, sprite.x, sprite.y)
        if distToSprite < settings.maxSpriteDist: return False
    return True

def playFootstepSound():
    global footstepSoundTimer
    currentTime = time.time()
    if currentTime-footstepSoundTimer > settings.footstepInterval:
        settings.sfxFiles[0].play()
        footstepSoundTimer = currentTime
    
def attack():
    player = settings.player
    # loop through all enemies
    for enemy in settings.enemyList:
        # check if close enough
        if utilities.distance(player.x, player.y, enemy.x, enemy.y) < settings.attackRange:
            distVec = utilities.normalizeVector((enemy.x-player.x, enemy.y-player.y))
            dirVec = (player.dirX, player.dirY)
            # check if roughly facing the right direction
            dp = utilities.dotProduct(distVec, dirVec)
            theta = math.degrees(math.acos(dp))
            if theta < settings.attackAngularRange:
                player.attack(enemy)

def switchTo(state):
    settings.state = state
    settings.musicPlayer.next_source()

def pauseGame():
    switchTo('paused')
    pause.onSwitch()

def die():
    switchTo('death')
    death.onSwitch()

def winGame():
    switchTo('win')
    win.onSwitch()
