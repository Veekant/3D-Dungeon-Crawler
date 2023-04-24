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
    testEnemy = sprite.enemy(3.5, 4.5, 3, 3, 400, None)

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
    input.onMouseMove(x, y, dx, dy)

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    input.onMousePress(x, y, button, modifiers)

def update(dt):
    game_window.push_handlers(keys)
    input.onKeyHold(keys, dt)
clock.schedule_interval(update, 1/60)

def main():
    onAppStart()
    app.run()

main()