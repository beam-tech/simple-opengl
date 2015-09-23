
from pyglet.window import key

from pyglet.gl import *
import pyglet
import STL

try:
    # Try and create a window with multisampling (antialiasing)
    config = Config(sample_buffers=1, samples=4, 
                    depth_size=16, double_buffer=True,)
    window = pyglet.window.Window(600, 600, resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    # Fall back to no multisampling for old hardware
    window = pyglet.window.Window(resizable=True)


@window.event
def on_key_press(symbol, modifiers):
    global rx, ry,rz
    if symbol == key.LEFT:
        rx =+ 5
    if symbol == key.RIGHT:
        rx -= 5
    if symbol == key.UP:
        rz += 5


@window.event
def on_resize(width, height):
    # Override the default on_resize handler to create a 3D projection
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(60., width / float(height), 0, 100.)
    glOrtho(-50, 50, -50, 50, -50, 50)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

def update(dt):
    global rx, ry, rz
    rx += dt * 30
    ry += dt * 80
    rz += dt * 1
    rx %= 360
    ry %= 360
    rz %= 360
pyglet.clock.schedule(update)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -4)
    glRotatef(rz, 0, 0, 1)
    glRotatef(ry, 0, 1, 0)
    glRotatef(rx, 1, 0, 0)
    draw()

def setup():
    # One-time GL setup
    glClearColor(1, 1, 1, 1)
    glColor3f(0, 1, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)

    # Uncomment this line for a wireframe view
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Simple light setup.  On Windows GL_LIGHT0 is enabled by default,
    # but this is not the case on Linux or Mac, so remember to always 
    # include it.
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    # Define a simple function to create ctypes arrays of floats:
    def vec(*args):
        return (GLfloat * len(args))(*args)

    glLightfv(GL_LIGHT0, GL_POSITION, vec(.5, .5, 1, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, vec(.5, .5, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
    glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, .5, 0))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(.5, .5, .5, 1))
    glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0.5, 0, 0.8, 1))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)

#class Torus(object):
    #def __init__(self):
        # Create the vertex and normal arrays.
        
        

        # Create ctypes arrays of the lists
        # vertices = (GLfloat * len(vertices))(*vertices)
        # normals = (GLfloat * len(normals))(*normals)

        # # Create a list of triangle indices.
        

        # indices = []
        # for i in range(100):
        #     for j in range(100 - 1):
        #         indices.extend([p, p + 100, p + 100 + 1])
        #         indices.extend([p,  p + 100 + 1, p + 1])
        
        # indices = (GLuint * len(indices))(*indices)

        # Compile a display list
        #self.list = glGenLists(1)
        #glNewList(self.list, GL_COMPILE)

        #glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        #glEnableClientState(GL_VERTEX_ARRAY)
        #glEnableClientState(GL_NORMAL_ARRAY)
        #glVertexPointer(3, GL_FLOAT, 0, vertices)
        #glNormalPointer(GL_FLOAT, 0, normals)
        #glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
        #glPopClientAttrib()

        #glEndList()

    #def draw(self):
        #glCallList(self.list)

def draw():
    stl = STL.Reader("space_invader.stl")
    triangles = stl.parse_triangles()
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        glNormal3f(*triangle[0])
        glVertex3f(*triangle[1])
        glVertex3f(*triangle[2])
        glVertex3f(*triangle[3])
    glEnd()


setup()
rx = ry = rz = 0
pyglet.app.run()