import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

class Ship:
    vertices = np.zeros(3, [("position", np.float32, 2)])
    vertices['position'] = [
                            ( 0.0, 0.0), # vertice 0
                            (+0.5,+0.5), # vertice 1
                            (+0.5, 0.0), # vertice 2
                            ]  

    def loadShape(self, program):
        buffer = glGenBuffers(1)

        # Make this buffer the default one
        glBindBuffer(GL_ARRAY_BUFFER, buffer)

        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_DYNAMIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, buffer)

        # Bind the position attribute
        # --------------------------------------
        stride = self.vertices.strides[0]
        offset = ctypes.c_void_p(0)

        loc = glGetAttribLocation(program, "position")
        glEnableVertexAttribArray(loc)

        glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)


    def drawShape(self):
        glDrawArrays(GL_TRIANGLES, 0, len(self.vertices))              
                            


