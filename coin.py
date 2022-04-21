from itertools import count
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

class Coin:

    
    def _init_(self, vertices = np.zeros(32, [("position", np.float32, 2)])):
        count = 0
        angle = 0.0
        radius = 0.1

        for i in range(32):
            angle += 2*3.14/32 
            x = math.cos(angle)*radius
            y = math.sin(angle)*radius
            self._vertices[count] = [x,y]

       

    

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
        print(self.vertices)
        glDrawArrays(GL_TRIANGLE_FAN, 0, len(self.vertices))              
                            


