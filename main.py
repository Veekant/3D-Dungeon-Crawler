from cmu_graphics import *
from pyglet import *
import settings
import load
import player
import hud
import sprite
import renderGame
import input
import math
import time

'''
def onAppStart(app):
    app.width, app.height = settings.width, settings.height
    app.stepsPerSecond = settings.fps
    settings.map = load.loadMap("map1")
    settings.player = player.player(1.5, 1.5, math.pi)
    settings.minimap = hud.minimap(app.width-200, app.height-200, 200, 200)
    settings.statusBars = hud.statusBars(0, app.height-200, 300, 200, 75, 12)
    testEnemy = sprite.enemy(3.5, 4.5, 3, 3, 250, None)

def redrawAll(app):
    startTime = time.time()
    renderGame.render()
    settings.minimap.drawMap()
    settings.statusBars.drawBars()
    endTime = time.time()
    fps = int(1 / (endTime - startTime))
    drawLabel(fps, 20, 20, size=12)
    # temp victory condition
    if len(settings.enemyList) == 0:
        drawLabel("YOU WIN (for now)", app.width//2, app.height//2, size=50)

def onStep(app):
    # update each enemy
    for enemy in settings.enemyList:
        enemy.update()
    # temp game over state
    if settings.gameOver: app.stop()

def onMouseMove(app, mouseX, mouseY):
    pass

def onMousePress(app, mouseX, mouseY):
    input.attack()

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
'''

game_window = window.Window(fullscreen=True)
keys = window.key.KeyStateHandler()
fps_display = window.FPSDisplay(window=game_window)
batch = graphics.Batch()

def onAppStart():
    settings.width, settings.height = game_window.get_size()
    game_window.set_exclusive_mouse(True)

    settings.map = load.loadMap("map1")
    settings.player = player.player(1.5, 1.5, math.pi)
    settings.minimap = hud.minimap(settings.width-200, settings.height-200, 200, 200)
    settings.statusBars = hud.statusBars(0, settings.height-200, 300, 200, 75, 12)
    testEnemy = sprite.enemy(3.5, 4.5, 3, 3, 250, None)

@game_window.event
def on_draw():
    game_window.clear()
    renderGame.render()
    fps_display.draw()

@game_window.event
def on_key_press(symbol, modifiers):
    key = window.key.symbol_string(symbol)
    input.onKeyPress(game_window, key)

@game_window.event
def on_mouse_motion(x, y, dx, dy):
    print(dx, dy)
    input.onMouseMove(x, y, dx, dy)

def update(dt):
    game_window.push_handlers(keys)
    input.onKeyHold(keys, dt)
clock.schedule_interval(update, 1/60)

def main():
    onAppStart()
    app.run()

main()