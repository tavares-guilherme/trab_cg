import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np


class Star:

    vertices = np.zeros(6, [("position", np.float32, 2)])
    vertices['position'] = [
                                ( 0.2, 0.4), # vertice 0
                                ( 0.4, 0.8), # vertice 1
                                ( 0.6, 0.4), # vertice 2
                                ( 0.2, 0.7), # vertice 3
                                ( 0.6, 0.7), # vertice 4
                                ( 0.4, 0.3), # vertice 5
                            ]
    offset = 0
 
    def drawShape(self, loc_color):
        glDrawArrays(GL_TRIANGLES, 0+self.offset-1, 6)  