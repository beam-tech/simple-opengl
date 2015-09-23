# -*- coding: utf-8 -*-

# подключаем необходимые модули
from pyglet.gl import *

window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    print 'The window was resized to %dx%d' % (width, height)
