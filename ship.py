import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math
import matrix

class Ship:
    def __init__(self, offset, x_0, y_0):
        self.offset = offset
        self.x_0 = x_0
        self.y_0 = y_0
        self.vertices = self.setVertices()
        self.wColor = 1

    def setWColor(self, color):
        self.wColor = color

    def setVertices(self):
        step = 16
        radius = 0.05

        vertices = np.zeros(21, [("position", np.float32, 2)])
        # Retangulo
        vertices[0] = [ 0.1,-0.1]
        vertices[1] = [-0.1,-0.1]
        vertices[2] = [ 0.1, 0.1]
        vertices[3] = [-0.1, 0.1]
        # Ponta da nave
        vertices[4] = [ 0.0, 0.16]
        
        # Circulo
        for i in range(step):
            angle = math.pi * (2 * i/step)
            x = math.cos(angle)*radius
            y = math.sin(angle)*radius + 0.75 * radius

            vertices[i+5] = [x,y]

        
        return vertices

    def drawShape(self, loc_color, program, dg, tx, ty):
        mat_transformation = matrix.getMatrix(1, dg, self.x_0 + tx, self.y_0 + ty)
        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transformation)

        # red body
        rValueBody = 227.0 / 255.0
        gValueBody = 23.0 / 255.0
        bValueBody = 70.0 / 255.0
        glUniform4f(loc_color, rValueBody, gValueBody, bValueBody, 1.0)  
        glDrawArrays(GL_TRIANGLE_STRIP, self.offset, 4)

         # green top
        rValueTop = 115.0 / 255.0
        gValueTop = 222.0 / 255.0
        bValueTop = 33.0 / 255.0
        glUniform4f(loc_color, rValueTop, gValueTop, bValueTop, 1.0)   
        glDrawArrays(GL_TRIANGLES, self.offset + 2, 3)

        # white window
        if(self.wColor == 1):
            ValueWindow = 1
        else:
            ValueWindow = 118.0 / 255.0
        
        glUniform4f(loc_color, ValueWindow, ValueWindow, ValueWindow, 1.0) 
        glDrawArrays(GL_TRIANGLE_FAN, self.offset + 5, 16)