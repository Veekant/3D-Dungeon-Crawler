from pyglet import *
import settings
import load
import player
import hud
import gameSprite
import renderGame
import input
import math
import time

image.Texture.default_min_filter = gl.GL_LINEAR
image.Texture.default_mag_filter = gl.GL_LINEAR

game_window = window.Window(fullscreen=True)
keys = window.key.KeyStateHandler()
fps_display = window.FPSDisplay(window=game_window)
batch = graphics.Batch()

def onAppStart():
    settings.width, settings.height = game_window.get_size()
    game_window.set_exclusive_mouse(True)

    settings.map = load.loadMap("map2")
    settings.texFiles = load.loadTextures()
    settings.spriteFiles = load.loadSprites()
    settings.player = player.player(1.5, 1.5, math.pi)
    settings.minimap = hud.minimap(settings.width-200, 0, 200, 200)
    settings.statusBars = hud.statusBars(0, 0, 300, 200, 75, 12)
    testEnemy = gameSprite.enemy(3.5, 4.5, 3, 3, 400, 5)

@game_window.event
def on_draw():
    game_window.clear()
    renderGame.render()
    settings.minimap.draw()
    settings.statusBars.drawBars()
    fps_display.draw()

@game_window.event
def on_key_press(symbol, modifiers):
    key = window.key.symbol_string(symbol)
    input.onKeyPress(game_window, key)

@game_window.event
def on_mouse_motion(x, y, dx, dy):
    input.onMouseMove(x, y, dx, dy)

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    input.onMousePress(x, y, button, modifiers)

def update(dt):
    game_window.push_handlers(keys)
    input.onKeyHold(keys, dt)
    for enemy in settings.enemyList:
        enemy.update(dt)
clock.schedule_interval(update, 1/settings.fps)

def main():
    onAppStart()
    app.run()

main()