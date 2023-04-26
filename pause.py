'''
pause menu
'''

from pyglet import *
import settings
import gameplay
import main_menu
import ui

buttonList = []
blurColor = (230, 230, 230, 128)
gray = (128, 128, 128, 255)
startColors = [(255, 0, 0, 255), (225, 0, 0, 255), (195, 0, 0, 255)]

def reset():
    unpauseButton = ui.button(settings.width//2, settings.height//2, 600, 100, "Unpause", 50, startColors, unpauseGame)
    mainMenuButton = ui.button(settings.width//2, settings.height//2-150, 600, 100, 'Main Menu', 50, startColors, returnToMainMenu)
    buttonList.extend([unpauseButton, mainMenuButton])

def onSwitch():
    settings.window.set_exclusive_mouse(False)
    reset()

def update(dt):
    pass

def onKeyPress(key):
    if key == 'P':
        unpauseGame()

def onDraw():
    gameplay.onDraw()
    batch = graphics.Batch()
    blurScreen = shapes.Rectangle(0, 0, settings.width, settings.height,
                                  color=blurColor, batch=batch)
    pauseLabel = text.Label("Paused", font_name='Century Gothic',
                          font_size=72, bold=True, color=gray,
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
        if button.checkCursor(mouseX, mouseY):
            button.released()

def unpauseGame():
    switchTo('gameplay')
    gameplay.onSwitch(False)

def returnToMainMenu():
    switchTo('main_menu')
    main_menu.onSwitch()

def switchTo(state):
    settings.state = state
    buttonList = []