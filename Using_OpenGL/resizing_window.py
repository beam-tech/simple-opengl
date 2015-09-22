# -*- coding: utf-8 -*-

# подключаем необходимые модули
from OpenGL.raw.GL.VERSION.GL_1_1 import glMatrixMode
from pyglet.gl import *

# будем вводить команды OpenGL в window
#window = pyglet.window.Window(config=config)
window = pyglet.window.Window(width=300, height=300, resizable=True)


vertices = [
        0, 0,
        200, 0,
        100,200
        ]
# преобразуем в OpenGL / ctypes массив:
vertices_gl = (GLfloat* len(vertices))(*vertices)
# Подобные конструкции массивов могут быть использованы для создания
# данных для буфера вершин объектов, данных текстуры, данных штриховки
# многоугольников и функций map.


# Включаем использование массива вершин
glEnableClientState(GL_VERTEX_ARRAY)

# Указываем, где взять массив координат:
# Первый параметр - сколько используется координат на одну вершину
# Второй параметр - определяем тип данных для каждой координаты вершины
# Третий парметр - определяет смещение между вершинами в массиве
# Если вершины идут одна за другой, то смещение 0
# Четвертый параметр - указатель на первую координату первой вершины в массиве
glVertexPointer(2, GL_FLOAT, 0, vertices_gl)


@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                # Сброс просмотра
    # Задаем усеченную пирамиду видимости.
    # Первый параметр - угол зрения в вертикальной плоскости;
    # Второй параметр - отношение ширины окна картинной плоскости к его высоте;
    # Третий и Четвертый параметр - расстояния от центра проецирования до передней и задней отсекающих плоскостей.
    gluPerspective(65, width / float(height), 1, 2)
    glMatrixMode(GL_MODELVIEW)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()                                    #  текущая матрица будет сделана единичной.

    # Рисуем данные массивов за один проход:
    # Первый параметр - какой тип примитивов использовать (треугольники, точки, линии и др.)
    # Второй параметр - начальный индекс в указанных массивах
    # Третий параметр - количество рисуемых объектов (в нашем случае это 2 вершины - 4 координат или размер vertises на 2)
    glDrawArrays(GL_TRIANGLES, 0, len(vertices) // 2)

pyglet.app.run()
