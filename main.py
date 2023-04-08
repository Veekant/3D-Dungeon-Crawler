from cmu_graphics import *
import renderGame
import load

def onAppStart(app):
    app.width, app.height = 1920, 1080
    app.stepsPerSecond = 60
    app.map = load.loadMap("map1")
    app.playerX, app.playerY = 1, 1
    app.playerTheta = 0

def redrawAll(app):
    renderGame.render()

def onStep(app):
    pass

def onMouseMove(app, mouseX, mouseY):
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onKeyPress(app, key):
    if key == 'escape': app.stop()
    print(key)

def main():
    runApp()

main()