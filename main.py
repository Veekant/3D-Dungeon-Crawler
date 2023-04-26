from pyglet import *
import settings
import load
import gameplay
import main_menu
import aboutPage
import pause
import death
import win
import traceback

image.Texture.default_min_filter = gl.GL_LINEAR
image.Texture.default_mag_filter = gl.GL_LINEAR

game_window = window.Window(fullscreen=True)
settings.window = game_window
keys = window.key.KeyStateHandler()
fps_display = window.FPSDisplay(window=game_window)
batch = graphics.Batch()

def onAppStart():
    settings.width, settings.height = game_window.get_size()
    game_window.set_exclusive_mouse(True)

    settings.map = load.loadMap("map2")
    settings.texFiles = load.loadTextures()
    settings.spriteFiles = load.loadSprites()
    settings.sfxFiles = load.loadSFX()
    settings.musicFiles = load.loadMusic()
    settings.state = 'main_menu'
    settings.musicPlayer = media.Player()
    main_menu.onSwitch()

@game_window.event
def on_draw():
    game_window.clear()
    if settings.state == 'main_menu':
        main_menu.onDraw()
    elif settings.state == 'about':
        aboutPage.onDraw()
    elif settings.state == 'gameplay': 
        gameplay.onDraw()
    elif settings.state == 'paused':
        pause.onDraw()
    elif settings.state == 'death':
        death.onDraw()
    elif settings.state == 'win':
        win.onDraw()
    fps_display.draw()

@game_window.event          
def on_key_press(symbol, modifiers):
    key = window.key.symbol_string(symbol)

    if key == 'ESCAPE':
        settings.musicPlayer.next_source()

    if settings.state == 'gameplay':
        gameplay.onKeyPress(key)
    elif settings.state == 'paused':
        pause.onKeyPress(key)

@game_window.event
def on_mouse_motion(x, y, dx, dy):
    if settings.state == 'main_menu':
        main_menu.onMouseMove(x, y)
    elif settings.state == 'about':
        aboutPage.onMouseMove(x, y)
    elif settings.state == 'gameplay':
        gameplay.onMouseMove(x, y, dx, dy)
    elif settings.state == 'paused':
        pause.onMouseMove(x, y)
    elif settings.state == 'death':
        death.onMouseMove(x, y)
    elif settings.state == 'win':
        win.onMouseMove(x, y)

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    if settings.state == 'main_menu':
        main_menu.onMousePress(x, y, button)
    elif settings.state == 'about':
        aboutPage.onMousePress(x, y, button)
    elif settings.state == 'gameplay':
        gameplay.onMousePress(x, y, button, modifiers)
    elif settings.state == 'paused':
        pause.onMousePress(x, y, button)
    elif settings.state == 'death':
        death.onMousePress(x, y, button)
    elif settings.state == 'win':
        win.onMousePress(x, y, button)

@game_window.event
def on_mouse_release(x, y, button, modifiers):
    if settings.state == 'main_menu':
        main_menu.onMouseRelease(x, y, button)
    elif settings.state == 'about':
        aboutPage.onMouseRelease(x, y, button)
    elif settings.state == 'gameplay':
        gameplay.onMouseRelease(x, y, button)
    elif settings.state == 'paused':
        pause.onMouseRelease(x, y, button)
    elif settings.state == 'death':
        death.onMouseRelease(x, y, button)
    elif settings.state == 'win':
        win.onMouseRelease(x, y, button)

def update(dt):
    game_window.push_handlers(keys)
    if settings.state == 'gameplay':
        gameplay.update(dt, keys)
    elif settings.state == 'death':
        death.update(dt)
clock.schedule_interval(update, 1/settings.fps)

def main():
    try:
        onAppStart()
        app.run()
    except:
        game_window.close()
        traceback.print_exc()

main()