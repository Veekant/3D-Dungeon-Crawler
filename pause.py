'''
pause menu
'''

from pyglet import *
import settings
import gameplay
import main_menu
import ui

# initialize vars
buttonList = []
blurColor = (230, 230, 230, 128)
gray = (128, 128, 128, 255)
startColors = [(255, 0, 0, 255), (225, 0, 0, 255), (195, 0, 0, 255)]

def reset():
    # create buttons
    unpauseButton = ui.button(settings.width//2, settings.height//2,
                              600, 100, "Unpause", 50, startColors, unpauseGame)
    mainMenuButton = ui.button(settings.width//2, settings.height//2-(150*settings.uiScale),
                               600, 100, 'Main Menu', 50, startColors, returnToMainMenu)
    buttonList.extend([unpauseButton, mainMenuButton])

def onSwitch():
    # enable mouse
    settings.window.set_exclusive_mouse(False)
    # play pause sound
    settings.sfxFiles[5].play()
    # pause current music
    settings.musicPlayer.pause()
    reset()

def onKeyPress(key):
    # unpause game if pause key pressed
    if key == 'P':
        unpauseGame()

def onDraw():
    # draws game behind menu
    gameplay.onDraw()
    batch = graphics.Batch()
    # "blurs" the background
    blurScreen = shapes.Rectangle(0, 0, settings.width, settings.height,
                                  color=blurColor, batch=batch)
    # draws pause text
    pauseLabel = text.Label("Paused", font_name='Century Gothic',
                          font_size=72, bold=True, color=gray,
                          x=settings.width//2, y=settings.height-(400*settings.uiScale),
                          anchor_x='center', anchor_y='center',
                          batch=batch)
    # draws buttons
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

def unpauseGame():
    switchTo('gameplay')
    # play unpause music
    settings.sfxFiles[6].play()
    gameplay.onSwitch(False)

def returnToMainMenu():
    switchTo('main_menu')
    main_menu.onSwitch()

def switchTo(state):
    # change state
    settings.state = state
    # reset buttons
    buttonList = []
    # resume music
    settings.musicPlayer.play()