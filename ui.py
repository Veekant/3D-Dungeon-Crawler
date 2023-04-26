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

    def __init__(self, left, bottom, width, height, text, colors, func):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
        self.text = text
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

    def checkCursor(self, mouseX, mouseY):
        return (self.left <= mouseX <= self.left+self.width and
                self.bottom <= mouseY <= self.bottom+self.height)
    
    def draw(self, batch):
        if self.press: color = self.pressColor
        elif self.hover: color = self.hoverColor
        else: color = self.color
        rect = shapes.BorderedRectangle(self.left, self.bottom, self.width, self.height,
                                        border=2, color=color, border_color=black,
                                        batch=batch)
        centerX, centerY = self.left+self.width//2, self.bottom+self.height//2
        label = text.Label(self.text, font_name='Times New Roman',
                          font_size=12, bold=True,
                          x=centerX, y=centerY,
                          anchor_x='center', anchor_y='center',
                          batch=batch)
        return (rect, label)


    

    
