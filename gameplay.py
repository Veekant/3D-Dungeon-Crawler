'''
might handle some input stuff here
'''

from pyglet import *
import settings
import pause
import death
import player
import hud
import gameSprite
import renderGame
import utilities
import math

def onSwitch(resetGame):
    settings.window.set_exclusive_mouse(True)
    if resetGame: reset()

def reset():
    settings.player = player.player(1.5, 1.5, math.pi)
    settings.minimap = hud.minimap(settings.width-200, 0, 200, 200)
    settings.statusBars = hud.statusBars(0, 0, 300, 200, 75, 12)
    testEnemy = gameSprite.enemy(3.5, 4.5, 4, 400, 6)

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
        normDir = utilities.normalizeVector(dir)
        dr = settings.speed * dt
        dir = utilities.vecMultiply(dr, normDir)
        move(dir[0], dir[1])

def onMouseMove(mouseX, mouseY, dx, dy):
    dTheta = settings.sensitivity * math.atan2(dx/settings.width, 1)
    rotate(dTheta)

def onMousePress(mouseX, mouseY, button, modifiers):
    if button == window.mouse.LEFT:
        attack()

def onDraw():
    renderGame.render()
    settings.minimap.draw()
    settings.statusBars.drawBars()

def update(dt, keys):
    onKeyHold(keys, dt)
    for enemy in settings.enemyList:
        enemy.update(dt)
    if settings.player.health <= 0:
        die()

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
    if map[int(player.x)][int(player.y)] == 0: return
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
    if map[int(entity.x)][int(entity.y)] == 0: return
    # if failed, undo and try second axis
    entity.moveAxis(-dx, dy)
    if map[int(entity.x)][int(entity.y)] == 0: return
    # if failed again, give up and cry probably
    entity.moveAxis(0, -dy)

def attack():
    player = settings.player
    # loop through all enemies
    for enemy in settings.enemyList:
        # check if close enough
        if utilities.distance(player.x, player.y, enemy.x, enemy.y) < settings.attackRange:
            distVec = (enemy.x-player.x, enemy.y-player.y)
            dirVec = (player.dirX, player.dirY)
            # check if roughly facing the right direction
            if utilities.dotProduct(distVec, dirVec) > 0:
                player.attack(enemy)

def switchTo(state):
    settings.state = state

def pauseGame():
    switchTo('paused')
    pause.onSwitch()

def die():
    switchTo('death')
    death.onSwitch()
