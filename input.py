'''
might handle some input stuff here
'''

def rotate(player, direction):
    player.rotate(direction)

def move(player, map, dx, dy):
    player.move(dx, dy)
    mapX, mapY = int(player.x), int(player.y)
    if map[mapX][mapY] > 0:
        player.move(-dx, -dy)