'''
might handle some input stuff here
'''

from pyglet import *
import settings
import utilities
import math

def onKeyPress(window, key):
    if key == 'ESCAPE': window.close()

def onKeyHold(keys):
    if keys[window.key.Q]: rotate(-0.05)
    elif keys[window.key.E]: rotate(0.05)

    if keys[window.key.W]: move(0, 1/30)
    elif keys[window.key.A]: move(1/30, 0)
    elif keys[window.key.S]: move(0, -1/30)
    elif keys[window.key.D]: move(-1/30, 0)

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
