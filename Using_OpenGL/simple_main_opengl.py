# -*- coding: utf-8 -*-

# подключаем необходимые модули
from pyglet.gl import *

# будем вводить команды OpenGL в window
window = pyglet.window.Window()

# выводит треугольник
@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glColor3f(0.5,0,0)
    glVertex2f(0,0)
    glVertex2f(window.width,0)
    glVertex2f(window.width,window.height)
    glEnd()

pyglet.app.run()
