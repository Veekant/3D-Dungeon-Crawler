from cmu_graphics import *
import renderGame
import load
import player

def onAppStart(app):
    app.width, app.height = 1920, 1080
    app.stepsPerSecond = 60
    app.map = load.loadMap("map1")
    app.player = player.player((50, 50), 0, 90)

def redrawAll(app):
    drawCircle(app.player.x, app.player.y, 10)
    dirX, dirY = app.player.x + 35 * app.player.dirX, app.player.y + 35 * app.player.dirY
    drawLine(app.player.x, app.player.y, dirX, dirY)
    drawLine(dirX, dirY, dirX + 35 * app.player.planeX, dirY + 35 * app.player.planeY)
    drawLine(dirX, dirY, dirX - 35 * app.player.planeX, dirY - 35 * app.player.planeY)

    drawLine(app.player.x, app.player.y, dirX + 35 * app.player.planeX, dirY + 35 * app.player.planeY)
    drawLine(app.player.x, app.player.y, dirX - 35 * app.player.planeX, dirY - 35 * app.player.planeY)

def onStep(app):
    pass

def onMouseMove(app, mouseX, mouseY):
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onKeyPress(app, key):
    if key == 'escape': app.stop()

def onKeyHold(app, keys):
    if 'q' in keys: app.player.rotate(0.1)
    elif 'e' in keys: app.player.rotate(-0.1)
    elif 'w' in keys: app.player.move(0, -10)
    elif 'a' in keys: app.player.move(-10, 0)
    elif 's' in keys: app.player.move(0, 10)
    elif 'd' in keys: app.player.move(10, 0)


def main():
    runApp()

main()