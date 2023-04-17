'''
might handle some input stuff here
'''
import math

# call player rotate method
def rotate(player, direction):
    player.rotate(direction)

# move player and check for collisions
def move(player, map, hor, vert):
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
    # check first axis
    player.moveAxis(dx, 0)
    if map[int(player.x)][int(player.y)] == 0: return
    # if failed, undo and try second axis
    player.moveAxis(-dx, dy)
    if map[int(player.x)][int(player.y)] == 0: return
    # if failed again, give up and cry probably
    player.moveAxis(0, -dy)
