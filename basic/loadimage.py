# -*- coding: utf-8 -*-
import pyglet
# инициализация окна
window = pyglet.window.Window()
# загружаем картинку
image = pyglet.resource.image('car.png')


@window.event
def on_draw():
    window.clear()
    # выводит картинку по середине
    # координаты картинки (x, y), начало координат - левый нижний край окна
    image.blit(window.width // 2 - image.width // 2,    # x
               window.height // 2 - image.height // 2)  # y

pyglet.app.run()
