'''
creates menu when player wins
'''

from pyglet import *
import settings
import main_menu
import ui
import utilities

# initialize vars
buttonList = []
green = (0, 255, 0, 255)
buttonColors = [(255, 0, 0, 255), (225, 0, 0, 255), (195, 0, 0, 255)]

def reset():
    # create main menu button
    mainMenuButton = ui.button(settings.width//2, settings.height//2-(100*settings.uiScale),
                               600, 100, 'Main Menu', 50, buttonColors, returnToMainMenu)
    buttonList.append(mainMenuButton)

def onSwitch():
    # enable mouse
    settings.window.set_exclusive_mouse(False)
    # play win music
    musicPlayer = settings.musicPlayer
    utilities.stopSound(musicPlayer)
    musicPlayer.queue(settings.musicFiles[1])
    musicPlayer.play()
    reset()

def onDraw():
    batch = graphics.Batch()
    # display win text
    winLabel = text.Label("YOU WIN", font_name='Century Gothic',
                          font_size=72, bold=True, color=green,
                          x=settings.width//2, y=settings.height-(400*settings.uiScale),
                          anchor_x='center', anchor_y='center',
                          batch=batch)
    # draw buttons
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