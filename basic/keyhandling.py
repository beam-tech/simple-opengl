# -*- coding: utf-8 -*-

import pyglet
from pyglet.window import key    # события для символов
from pyglet.window import mouse  # события для символов
# инициализация окна
window = pyglet.window.Window()
#window.push_handlers(pyglet.window.event.WindowEventLogger())

# функция для обработки нажатия клавиш(декорируется)
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('AAA')
    elif symbol == key.LEFT:
        print('На лево')
    elif symbol == key.ENTER:
        print('Энтер')
    else:
        print('Не знаю, что за кнопка')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('Левая клавиша мыши')

@window.event
def on_draw():
    window.clear()

pyglet.app.run()