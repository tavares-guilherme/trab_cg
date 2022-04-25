from ctypes import c_void_p
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
from matplotlib.ft2font import VERTICAL
import numpy as np

class Flag:
    vertices = np.zeros(5, [("position", np.float32, 2)])
    offset = 0
    vertices['position'] = [
                            (0.0, 0.4), # vertice 0
                            (+0.3,+0.3), # vertice 1
                            (+0.0, 0.2), # vertice 2
                            (0.0, 0.0), # vertice 0
                            (0.0, 0.2), # vertice 1
                        ]


    def drawShape(self):
        glDrawArrays(GL_TRIANGLES, 0+self.offset-1, 4)
        glDrawArrays(GL_LINES, self.offset+2, 2)



