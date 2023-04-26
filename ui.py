'''
will have some basic ui here
(might be just buttons tbh)
'''

from pyglet import *
import settings
import utilities

black = (0, 0, 0, 255)
red = (255, 0, 0, 255)
green = (0, 255, 0, 255)
blue = (0, 0, 255, 255)
yellow = (255, 255, 0)
white = (255, 255, 255, 255)

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
    
    def pressed(self):
        self.hover = False
        self.press = True

    def released(self):
        self.hover = True
        self.press = False
        self.func()

    def hovered(self):
        self.hover = True
        self.press = False

    def unHovered(self):
        self.hover = False
        self.press = False

    def checkCursor(self, mouseX, mouseY):
        return (self.x-self.width//2 <= mouseX <= self.x+self.width//2 and
                self.y-self.height//2 <= mouseY <= self.y+self.height//2)
    
    def draw(self, batch):
        if self.press: color = self.pressColor
        elif self.hover: color = self.hoverColor
        else: color = self.color
        rect = shapes.BorderedRectangle(self.x, self.y, self.width, self.height,
                                        border=2, color=color, border_color=black,
                                        batch=batch)
        rect.anchor_position = self.width//2, self.height//2
        label = text.Label(self.text, font_name='Century Gothic',
                          font_size=self.textSize, bold=True,
                          x=self.x, y=self.y,
                          anchor_x='center', anchor_y='center',
                          batch=batch)
        return (rect, label)


    

    
