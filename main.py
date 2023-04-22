from cmu_graphics import *
import settings
import load
import player
import minimap
import sprite
import renderGame
import input
import math
import time

def onAppStart(app):
    app.width, app.height = settings.width, settings.height
    app.stepsPerSecond = settings.fps
    settings.map = load.loadMap("map1")
    settings.player = player.player(1.5, 1.5, math.pi)
    settings.minimap = minimap.minimap(app.width-200, app.height-200, 200, 200)
    testEnemy = sprite.enemy(3.5, 4.5, 3, 3, 250, None)

def redrawAll(app):
    startTime = time.time()
    renderGame.render()
    settings.minimap.drawMap()
    endTime = time.time()
    fps = int(1 / (endTime - startTime))
    drawLabel(fps, 20, 20, size=12)

def onStep(app):
    # print(app.player)
    for enemy in settings.enemyList:
        enemy.update()
    pass

def onMouseMove(app, mouseX, mouseY):
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onKeyPress(app, key):
    if key == 'escape': app.stop()

def onKeyHold(app, keys):
    if 'q' in keys: input.rotate(-0.05)
    elif 'e' in keys: input.rotate(0.05)

    if 'w' in keys: input.move(0, 1/30)
    elif 'a' in keys: input.move(1/30, 0)
    elif 's' in keys: input.move(0, -1/30)
    elif 'd' in keys: input.move(-1/30, 0)

def main():
    runApp()

main()