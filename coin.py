import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

class Coin:
    offset = 0
    
    vertices = np.zeros(64, [("position", np.float32, 2)])
    
    def findPoints(self):
        angle = 0.0
        radius = 0.05

        for count in range(64):
            if(count == 32):
                radius = 0.02
            angle += 2*3.14/32 
            x = math.cos(angle)*radius
            y = math.sin(angle)*radius
            self.vertices[count] = [x,y]
    


    def drawShape(self, loc_color):
       
        glUniform4f(loc_color, 204, 204, 51, 1.0) 
        glDrawArrays(GL_TRIANGLE_FAN, 0, 32)     
        glUniform4f(loc_color, 0, 200, 0, 1.0)  
        glDrawArrays(GL_TRIANGLE_FAN, 32, 31)         
                            


