from ctypes import c_void_p
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import matrix
import math

class Planet():
    def __init__(self, offset, x_0, y_0):
        self.offset = offset
        self.x_0 = x_0
        self.y_0 = y_0
        self.vertices = self.setVertices()
    
    def setVertices(self):
        step = 16
        radius = 0.15

        vertices = np.zeros(21, [("position", np.float32, 2)])

        vertices[0] = [0.0, 1.4*radius]
        vertices[2] = [0.6 * radius, 1.6*radius]
        vertices[1] = [0.0, 1.8*radius]
        vertices[3] = [0.0, 0.0]
        vertices[4] = [0.0, 1.5*radius]

        for i in range(step):
            angle = math.pi * (2 * i/step)
            x = math.cos(angle)*radius
            y = math.sin(angle)*radius

            vertices[i+5] = [x,y]
        
        return vertices



    def drawShape(self, loc_color, program, dg):
        mat_transformation = matrix.getMatrix(1, dg, self.x_0, self.y_0)
        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transformation)

        # red flag
        rValueFlag = 227.0 / 255.0
        gValueFlag = 23.0 / 255.0
        bValueFlag = 70.0 / 255.0

        # orange planet
        rValuePlanet = 135.0 / 255.0
        gValuePlanet = 68.0 / 255.0
        bValuePlanet = 9.0 / 255.0

        glUniform4f(loc_color, rValueFlag, gValueFlag, bValueFlag, 1.0) 
        glDrawArrays(GL_TRIANGLES, self.offset, 3)
        glDrawArrays(GL_LINES, self.offset+3, 2)

        glUniform4f(loc_color, rValuePlanet, gValuePlanet, bValuePlanet, 1.0) 
        glDrawArrays(GL_TRIANGLE_FAN, self.offset+5, 16)    