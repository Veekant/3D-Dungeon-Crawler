'''
creates main menu
'''

from pyglet import *
import settings
import gameplay
import aboutPage
import ui
import utilities

# initialize vars
buttonList = []
gray = (128, 128, 128, 255)
buttonColors = [(255, 0, 0, 255), (225, 0, 0, 255), (195, 0, 0, 255)]

def reset():
    # creates buttons
    startButton = ui.button(settings.width//2, settings.height//2+(150*settings.uiScale), 
                            600, 100, "Start", 50, buttonColors, startGame)
    aboutButton = ui.button(settings.width//2, settings.height//2,
                            600, 100, "About", 50, buttonColors, openAbout)
    quitButton = ui.button(settings.width//2, settings.height//2-(150*settings.uiScale),
                           600, 100, 'Quit', 50, buttonColors, quitGame)
    buttonList.extend([startButton, aboutButton, quitButton])

def onSwitch():
    # disables cursor
    settings.window.set_exclusive_mouse(False)
    # plays main menu music
    musicPlayer = settings.musicPlayer
    utilities.stopSound(musicPlayer)
    musicPlayer.queue(settings.musicFiles[2])
    musicPlayer.play()
    musicPlayer.volume = 0.25
    musicPlayer.loop = True
    reset()

def onDraw():
    batch = graphics.Batch()
    # draws title
    titleLabel = text.Label("3D Dungeon Crawler", font_name='Century Gothic',
                          font_size=96, bold=True, color=gray,
                          x=settings.width//2, y=settings.height-(150*settings.uiScale),
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

def startGame():
    switchTo('gameplay')
    gameplay.onSwitch(True)

def openAbout():
    switchTo('about')
    aboutPage.onSwitch()

def quitGame():
    # stop music
    settings.musicPlayer.next_source()
    # close window
    settings.window.close()

def switchTo(state):
    # change state
    settings.state = state
    # reset buttons
    buttonList = []

