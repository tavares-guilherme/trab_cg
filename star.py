import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import matrix


class Star:
    def __init__(self, offset, x_0, y_0, scale):
        self.offset = offset
        self.x_0 = x_0
        self.y_0 = y_0
        self.scale = scale
        self.vertices = self.setVertices()


    def setVertices(self):
        vertices = np.zeros(6, [("position", np.float32, 2)])
        vertices['position'] = [
                                    ( 0.2, 0.15), # vertice 0
                                    (-0.2, 0.15), # vertice 3
                                    ( 0.0,-0.30), # vertice 1
                                    ( 0.2,-0.15), # vertice 2
                                    (-0.2,-0.15), # vertice 4
                                    ( 0.0, 0.30), # vertice 5
                                ]
        return vertices
 
    def drawShape(self, loc_color, program, dgree):
        mat_transformation = matrix.getMatrix(self.scale, dgree, self.x_0, self.y_0)
        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transformation)

        # yellow stars
        rValue = 222.0 / 255.0
        gValue = 212.0 / 255.0
        bValue = 18.0 / 255.0

        glUniform4f(loc_color, rValue, gValue, bValue, 1.0) 
        glDrawArrays(GL_TRIANGLES, self.offset, 6)  