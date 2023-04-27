'''
creates menu when player wins
'''

from pyglet import *
import settings
import main_menu
import ui

buttonList = []
green = (0, 255, 0, 255)
buttonColors = [(255, 0, 0, 255), (225, 0, 0, 255), (195, 0, 0, 255)]

def reset():
    mainMenuButton = ui.button(settings.width//2, settings.height//2-100, 600, 100, 'Main Menu', 50, buttonColors, returnToMainMenu)
    buttonList.append(mainMenuButton)

def onSwitch():
    settings.window.set_exclusive_mouse(False)
    settings.musicFiles[1].play()
    reset()

def onDraw():
    batch = graphics.Batch()
    winLabel = text.Label("YOU WIN", font_name='Century Gothic',
                          font_size=72, bold=True, color=green,
                          x=settings.width//2, y=settings.height-400,
                          anchor_x='center', anchor_y='center',
                          batch=batch)
    buttonDrawables = []
    for button in buttonList:
        buttonDrawables.append(button.draw(batch))
    batch.draw()

def onMouseMove(mouseX, mouseY):
    for button in buttonList:
        if button.checkCursor(mouseX, mouseY):
            button.hovered()
        else:
            button.unHovered()

def onMousePress(mouseX, mouseY, button):
    for button in buttonList:
        if button.checkCursor(mouseX, mouseY):
            button.pressed()

def onMouseRelease(mouseX, mouseY, button):
    for button in buttonList:
        if button.pressed:
            button.released()

def returnToMainMenu():
    switchTo('main_menu')
    main_menu.onSwitch()

def switchTo(state):
    settings.state = state
    buttonList = []