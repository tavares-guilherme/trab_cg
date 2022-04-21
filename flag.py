import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

class Flag:
    triangle = np.zeros(5, [("position", np.float32, 2)])
    triangle['position'] = [
                              ( 0.0, 0.4), # vertice 0
                              (+0.3,+0.3), # vertice 1
                              (+0.0, 0.2), # vertice 2
                            (0.0, 0.0), # vertice 0
                            (0.0, 0.2), # vertice 1
                        ]

    def loadShape(self, program):
        buffer = glGenBuffers(1)

        # Make this buffer the default one
        glBindBuffer(GL_ARRAY_BUFFER, buffer)

        glBufferData(GL_ARRAY_BUFFER, self.triangle.nbytes, self.triangle, GL_DYNAMIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, buffer)

        # Bind the position attribute
        # --------------------------------------
        stride = self.triangle.strides[0]
        offset = ctypes.c_void_p(0)

        loc = glGetAttribLocation(program, "position")
        glEnableVertexAttribArray(loc)

        glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)


    def drawShape(self):
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glDrawArrays(GL_LINES, 4, 5)
