from cmu_graphics import *
import renderGame
import load
import player
import minimap
import math
import input
import time

def onAppStart(app):
    app.width, app.height = 1280, 720
    app.stepsPerSecond = 60
    app.map = load.loadMap("map1")
    app.player = player.player((1.5, 1.5), math.pi, 65)
    app.minimap = minimap.minimap(app.map, app.player, app.width-200, app.height-200, 200, 200)
    app.mouseY = None

def redrawAll(app):
    startTime = time.time()
    renderGame.render(app.width, app.height, app.player, app.map)
    # app.minimap.drawMap()
    endTime = time.time()
    print(endTime - startTime)
def onStep(app):
    # print(app.player)
    pass

def onMouseMove(app, mouseX, mouseY):
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onKeyPress(app, key):
    if key == 'escape': app.stop()

def onKeyHold(app, keys):
    if 'q' in keys: input.rotate(app.player, 0.05)
    elif 'e' in keys: input.rotate(app.player, -0.05)

    elif 'w' in keys: input.move(app.player, app.map, 0, -1/30)
    elif 'a' in keys: input.move(app.player, app.map, 1/30, 0)
    elif 's' in keys: input.move(app.player, app.map, 0, 1/30)
    elif 'd' in keys: input.move(app.player, app.map, -1/30, 0)


def main():
    runApp()

main()