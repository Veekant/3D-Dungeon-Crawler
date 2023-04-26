'''
menu when player dies
'''

from pyglet import *
import settings
import gameplay
import main_menu
import ui

buttonList = []
labelWidth = 10
blurColor = (0, 0, 0, 64)
blueColor2 = (0, 0, 0, 128)
gray = (128, 128, 128, 255)
red = (255, 0, 0, 255)
startColors = [(255, 0, 0, 255), (225, 0, 0, 255), (195, 0, 0, 255)]

def reset():
    mainMenuButton = ui.button(settings.width//2, settings.height//2-100, 600, 100, 'Main Menu', 50, startColors, returnToMainMenu)
    buttonList.append(mainMenuButton)

def onSwitch():
    settings.window.set_exclusive_mouse(False)
    settings.musicFiles[0].play()
    reset()

def update(dt):
    # cool animation
    global labelWidth
    if labelWidth < settings.width:
        labelWidth = min(labelWidth+250*dt, settings.width)

def onDraw():
    gameplay.onDraw()
    batch = graphics.Batch()
    blurScreen = shapes.Rectangle(0, 0, settings.width, settings.height,
                                  color=blurColor, batch=batch)
    blurLabel = shapes.Rectangle(settings.width//2, settings.height-400,
                                 labelWidth, 150,
                                 color=blurColor, batch=batch)
    blurLabel.anchor_position = labelWidth//2, 75
    deathLabel = text.Label("YOU DIED", font_name='Century Gothic',
                          font_size=72, bold=True, color=red,
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

def returnToMainMenu():
    switchTo('main_menu')
    main_menu.onSwitch()

def switchTo(state):
    settings.state = state
    buttonList = []