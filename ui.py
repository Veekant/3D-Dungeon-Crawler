'''
will have some basic ui here
(might be just buttons tbh)
'''

from pyglet import *
import settings
import utilities

class button:

    def __init__(self, left, bottom, width, height, colors, func):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
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
        self.hover = False
        self.press = False
        self.func()

    def hovered(self):
        self.hover = True
        self.press = False

    

    
