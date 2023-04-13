from cmu_graphics import *
import renderGame
import load
import player
import minimap

def onAppStart(app):
    app.width, app.height = 1920, 1080
    app.stepsPerSecond = 30
    app.map = load.loadMap("map1")
    app.player = player.player((1.5, 1.5), 0, 90)
    app.minimap = minimap.minimap(app.map, app.player, app.width-300, app.height-300, 300, 300)

def redrawAll(app):
    renderGame.render(app.width, app.height, app.player, app.map)
    app.minimap.drawMap()

def onStep(app):
    pass

def onMouseMove(app, mouseX, mouseY):
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onKeyPress(app, key):
    if key == 'escape': app.stop()

def onKeyHold(app, keys):
    if 'q' in keys: app.player.rotate(-0.1)
    elif 'e' in keys: app.player.rotate(0.1)
    elif 'w' in keys: app.player.move(0, -1/15)
    elif 'a' in keys: app.player.move(-1/15, 0)
    elif 's' in keys: app.player.move(0, 1/15)
    elif 'd' in keys: app.player.move(1/15, 0)


def main():
    runApp()

main()