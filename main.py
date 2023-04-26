from pyglet import *
import settings
import load
import player
import hud
import gameSprite
import renderGame
import gameplay
import main_menu
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

    settings.map = load.loadMap("map1")
    settings.texFiles = load.loadTextures()
    settings.spriteFiles = load.loadSprites()
    settings.state = 'main_menu'

@game_window.event
def on_draw():
    game_window.clear()
    if settings.state == 'gameplay': 
        gameplay.onDraw()
    fps_display.draw()

@game_window.event
def on_key_press(symbol, modifiers):
    key = window.key.symbol_string(symbol)
    if settings.state == 'gameplay':
        gameplay.onKeyPress(game_window, key)

@game_window.event
def on_mouse_motion(x, y, dx, dy):
    if settings.state == 'gameplay':
        gameplay.onMouseMove(x, y, dx, dy)

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    if settings.state == 'gameplay':
        gameplay.onMousePress(x, y, button, modifiers)

def update(dt):
    game_window.push_handlers(keys)
    if settings.state == 'gameplay':
        gameplay.update(dt, keys)
clock.schedule_interval(update, 1/settings.fps)

def main():
    onAppStart()
    app.run()

main()