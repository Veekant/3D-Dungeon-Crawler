'''
might handle some input stuff here
'''
import math

# call player rotate method
def rotate(player, direction):
    player.rotate(direction)

# move player and check for collisions
def move(player, map, dx, dy):
    # edge case (for later)
    if dx == 0 and dy == 0: return
    # move player and check if position is legal
    player.move(dx, dy)
    mapX, mapY = int(player.x), int(player.y)
    if map[mapX][mapY] == 0: return
    # if illegal, return to original position
    player.move(-dx, -dy)