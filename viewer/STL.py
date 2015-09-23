# -*- coding: utf-8 -*-
import re

# класс реализующий парсинг данных из файла stl
class Reader:
    def __init__(self, fname):
        # имя файла
        self.file_name = fname
        
    

    # Возвращает список из треугольнико
    def parse_triangles(self):
        coords = list()                 # список для хранения коорд. вершин или нормали одного треугольника
        triangles = list()              # список для хранения треугольников
        cnt = 0
        try:
            with open(self.file_name, 'r') as lines:
                for line in lines:
                    match = re.search('vertex|facet normal|endfacet', line)
                    if match is not None:
                        if match.group() == 'facet normal':
                            coords = []                          # обнуляем список
                            normal = self.take_coord(line)
                            coords.append(normal)                # сохраняем координаты нормали
                        elif match.group() == 'vertex':
                            vertex = self.take_coord(line)
                            coords.append(vertex)                # сохраняем координаты вершины
                        elif match.group() == 'endfacet':
                            triangles.append(coords)             # сохраняем треугольник

        except (IOError):
            print('Не могу прочитать файл!')
        except (NameError):
            print('Не подключен модуль re!')
        else:
            return triangles


    # Возвращает список из координат.
    # строка line - строка из файла
    def take_coord(self,line):
        try:
            result = line.split()
            coord = [float(i) for i in result[-3:]]
            return coord
        except (NameError):
            print('Не подключен модуль re!')

# stl = Reader('space_invader.stl')
# triangles = stl.parse_triangles()
# for triangle in triangles:
#     print(triangle)
