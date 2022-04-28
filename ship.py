import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

class Ship:
    def __init__(self, offset, x_0, y_0):
        self.offset = offset
        self.x_0 = x_0
        self.y_0 = y_0
        self.vertices = self.setVertices()

    def setVertices(self):
        step = 16
        radius = 0.05

        vertices = np.zeros(21, [("position", np.float32, 2)])
        vertices[0] = [ 0.1 + self.x_0,-0.2 + self.y_0]
        vertices[1] = [-0.1 + self.x_0,-0.2 + self.y_0]
        vertices[2] = [ 0.1 + self.x_0, 0.2 + self.y_0]
        vertices[3] = [-0.1 + self.x_0, 0.2 + self.y_0]
        vertices[4] = [ 0.0 + self.x_0, 0.4 + self.y_0]

        for i in range(step):
            angle = math.pi * (2 * i/step)
            x = math.cos(angle)*radius + self.x_0
            y = math.sin(angle)*radius + self.y_0 + 1.5 * radius

            vertices[i+5] = [x,y]

        
        return vertices

    def drawShape(self, loc_color):
        glUniform4f(loc_color, 225.0/255, 71.0/255, 71.0/255, 1.0)  
        glDrawArrays(GL_TRIANGLE_STRIP, self.offset, 4)    

        glUniform4f(loc_color, 0.5, 134.0/255, 59.0/255, 1.0)      
        glDrawArrays(GL_TRIANGLES, self.offset + 2, 3)

        glUniform4f(loc_color, 204, 204, 51, 1.0) 
        glDrawArrays(GL_TRIANGLE_FAN, self.offset + 5, 16)