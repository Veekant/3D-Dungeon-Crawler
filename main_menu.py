'''
main menu logic here
'''

from pyglet import *
import settings
import gameplay
import ui

buttonList = []
gray = (128, 128, 128, 255)
startColors = [(255, 0, 0, 255), (225, 0, 0, 255), (195, 0, 0, 255)]

def reset():
    startButton = ui.button(settings.width//2, settings.height//2+100, 600, 100, "Start", 50, startColors, startGame)
    quitButton = ui.button(settings.width//2, settings.height//2-100, 600, 100, 'Quit', 50, startColors, quitGame)
    buttonList.extend([startButton, quitButton])

def onSwitch():
    settings.window.set_exclusive_mouse(False)
    reset()

def update(dt):
    pass

def onDraw():
    batch = graphics.Batch()
    titleLabel = text.Label("3D Dungeon Crawler", font_name='Century Gothic',
                          font_size=96, bold=True, color=gray,
                          x=settings.width//2, y=settings.height-150,
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

def startGame():
    switchTo('gameplay')
    gameplay.onSwitch(True)

def quitGame():
    settings.window.close()

def switchTo(state):
    settings.state = state
    buttonList = []
