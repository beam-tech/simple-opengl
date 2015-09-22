# -*- coding: utf-8 -*-

import pyglet
# инициализация окна
window = pyglet.window.Window()

# инициализация Label для вывода текста
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width // 2,
                          y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')

# декоратор для событий
@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.app.run()

