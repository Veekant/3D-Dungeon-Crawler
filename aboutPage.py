'''
quick tutorial menu
'''

from pyglet import *
import settings
import main_menu
import ui

# initialize vars
buttonList = []
gray = (128, 128, 128, 255)
buttonColors = [(255, 0, 0, 255), (225, 0, 0, 255), (195, 0, 0, 255)]

def reset():
    # create main menu button
    mainMenuButton = ui.button(settings.width//2, settings.height//2-(400*settings.uiScale),
                               600, 100, 'Main Menu', 50, buttonColors, returnToMainMenu)
    buttonList.append(mainMenuButton)

def onSwitch():
    # make cursor visible
    settings.window.set_exclusive_mouse(False)
    reset()

def onDraw():
    batch = graphics.Batch()
    # draw instruction labels
    label1 = text.Label('Use the mouse to look around.', font_name='Century Gothic',
                          font_size=30, color=gray,
                          x=settings.width//2, y=settings.height//2 + (150*settings.uiScale),
                          anchor_x='center', anchor_y='center',
                          batch=batch)
    label2 = text.Label('Use WASD to move.', font_name='Century Gothic',
                          font_size=30, color=gray,
                          x=settings.width//2, y=settings.height//2 + (110*settings.uiScale),
                          anchor_x='center', anchor_y='center',
                          batch=batch)
    label3 = text.Label('Click to attack.', font_name='Century Gothic',
                          font_size=30, color=gray,
                          x=settings.width//2, y=settings.height//2 + (70*settings.uiScale),
                          anchor_x='center', anchor_y='center',
                          batch=batch)
    label4 = text.Label('Defeat all enemies to win.', font_name='Century Gothic',
                          font_size=30, color=gray,
                          x=settings.width//2, y=settings.height//2 + (30*settings.uiScale),
                          anchor_x='center', anchor_y='center',
                          batch=batch)
    label5 = text.Label('Good luck!', font_name='Century Gothic',
                          font_size=30, color=gray,
                          x=settings.width//2, y=settings.height//2 - (50*settings.uiScale),
                          anchor_x='center', anchor_y='center',
                          batch=batch)
    
    # draw all buttons on screen
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