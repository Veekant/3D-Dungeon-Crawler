'''
handles ui elements (buttons)
'''

from pyglet import *
import settings

# def colors
black = (0, 0, 0, 255)

# basic button class
class button:

    def __init__(self, centerX, centerY, width, height, text, textSize, colors, func):
        self.x = centerX
        self.y = centerY
        self.width = width
        self.height = height
        self.text = text
        self.textSize = textSize
        self.color = colors[0]
        self.hoverColor = colors[1]
        self.pressColor = colors[2]
        self.func = func

        self.hover = False
        self.press = False

    # methods for interactivity

    def pressed(self):
        self.press = True
        settings.sfxFiles[4].play()

    def released(self):
        self.press = False
        self.func()

    def hovered(self):
        if self.hover == False:
            settings.sfxFiles[3].play()
        self.hover = True
    
    def unHovered(self):
        self.hover = False

    def checkCursor(self, mouseX, mouseY):
        return (self.x-self.width//2 <= mouseX <= self.x+self.width//2 and
                self.y-self.height//2 <= mouseY <= self.y+self.height//2)
    
    def draw(self, batch):
        # gets color
        if self.press: color = self.pressColor
        elif self.hover: color = self.hoverColor
        else: color = self.color
        # draws rectangle
        rect = shapes.BorderedRectangle(self.x, self.y, self.width, self.height,
                                        border=2, color=color, border_color=black,
                                        batch=batch)
        rect.anchor_position = self.width//2, self.height//2
        # draws button text
        label = text.Label(self.text, font_name='Century Gothic',
                          font_size=self.textSize, bold=True,
                          x=self.x, y=self.y,
                          anchor_x='center', anchor_y='center',
                          batch=batch)
        return (rect, label)