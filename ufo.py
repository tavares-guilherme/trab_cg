import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import matrix
import math

class UFO:
    def __init__(self, offset, x_0, y_0):
        self.offset = offset
        self.x_0 = x_0
        self.y_0 = y_0

        self.vertices = self.setVertices()
        

    def setVertices(self):
        radius = 0.05
        step = 16

        vertices = np.zeros(22, [("position", np.float32, 2)])
        
        vertices[0] = [0.15,  0.02]
        vertices[1] = [0.10, -0.02]
        vertices[2] = [0.05, -0.05]

        vertices[3] = [-0.15,  0.02]
        vertices[4] = [-0.10, -0.02]
        vertices[5] = [-0.05, -0.05]


        for i in range(step):
            angle = math.pi * (2 * i/step)
            x = math.cos(angle)*radius
            y = math.sin(angle)*radius + 0.02

            vertices[i+6] = [x,y]

        return vertices


    def drawShape(self, loc_color, program, size):
        mat_transformation = matrix.getMatrix(size, 0, self.x_0, self.y_0)
        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transformation)

        glUniform4f(loc_color, 0, 200, 0, 1.0)  
        glDrawArrays(GL_TRIANGLE_FAN, self.offset + 6, 16)

        glUniform4f(loc_color, 1, 1, 1, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, self.offset, 6)
                            


