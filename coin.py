import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

class Coin:
    def __init__(self, offset, x_0, y_0, scale):
        self.offset = offset
        self.x_0 = x_0
        self.y_0 = y_0
        self.scale = scale
        self.vertices = self.setVertices()
        

    def setVertices(self):
        vertices = np.zeros(64, [("position", np.float32, 2)])

        angle = 0.0
        radius = 0.05*self.scale

        for count in range(64):
            if (count == 32):   radius = 0.02
            
            angle += 2*3.14/32
            
            x = math.cos(angle)*radius + self.x_0
            y = math.sin(angle)*radius + self.y_0

            vertices[count] = [x,y]
    
        return vertices


    def drawShape(self, loc_color):
        glUniform4f(loc_color, 204, 204, 51, 1.0) 
        glDrawArrays(GL_TRIANGLE_FAN, 0, 32)    

        glUniform4f(loc_color, 0, 200, 0, 1.0)  
        glDrawArrays(GL_TRIANGLE_FAN, 32, 31)         
                            


