'''
menu when player dies
'''

from pyglet import *
import settings
import gameplay
import main_menu
import ui
import utilities

# initialize vars
buttonList = []
labelWidth = 10
blurColor = (0, 0, 0, 64)
blurColor2 = (0, 0, 0, 128)
red = (255, 0, 0, 255)
buttonColors = [(255, 0, 0, 255), (225, 0, 0, 255), (195, 0, 0, 255)]

def reset():
    # create main menu button
    mainMenuButton = ui.button(settings.width//2, settings.height//2-(100*settings.uiScale),
                               600, 100, 'Main Menu', 50, buttonColors, returnToMainMenu)
    buttonList.append(mainMenuButton)
    # reset label size
    global labelWidth
    labelWidth = 10

def onSwitch():
    # enable cursor
    settings.window.set_exclusive_mouse(False)
    # play death music
    musicPlayer = settings.musicPlayer
    utilities.stopSound(musicPlayer)
    musicPlayer.queue(settings.musicFiles[0])
    musicPlayer.play()
    reset()

def update(dt):
    # cool animation (increases width of label)
    global labelWidth
    if labelWidth < settings.width:
        labelWidth = min(labelWidth+250*dt, settings.width)

def onDraw():
    gameplay.onDraw()
    batch = graphics.Batch()
    # "blurs" background
    blurScreen = shapes.Rectangle(0, 0, settings.width, settings.height,
                                  color=blurColor, batch=batch)
    # cool label for animation
    blurLabel = shapes.Rectangle(settings.width//2, settings.height-(400*settings.uiScale),
                                 labelWidth, 150,
                                 color=blurColor2, batch=batch)
    blurLabel.anchor_position = labelWidth//2, 75
    # death message
    deathLabel = text.Label("YOU DIED", font_name='Century Gothic',
                          font_size=72, bold=True, color=red,
                          x=settings.width//2, y=settings.height-(400*settings.uiScale),
                          anchor_x='center', anchor_y='center',
                          batch=batch)
    # draws each button
    buttonDrawables = []
    for button in buttonList:
        buttonDrawables.append(button.draw(batch))
    batch.draw()

def onMouseMove(mouseX, mouseY):
    # for each button
    for button in buttonList:
        # if cursor on button, hover
        if button.checkCursor(mouseX, mouseY):
            button.hovered()
        # if cursor elsewhere, unhover
        else:
            button.unHovered()

def onMousePress(mouseX, mouseY, button):
    # for each button
    for button in buttonList:
        # if press location in button, press button
        if button.checkCursor(mouseX, mouseY):
            button.pressed()

def onMouseRelease(mouseX, mouseY, button):
    # for each button
    for button in buttonList:
        # if currently pressed, release it
        if button.pressed:
            button.released()

def returnToMainMenu():
    switchTo('main_menu')
    main_menu.onSwitch()

def switchTo(state):
    # change state
    settings.state = state
    # reset buttons
    buttonList = []