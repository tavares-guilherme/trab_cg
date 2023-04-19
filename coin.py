import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math
import matrix

class Coin:
    def __init__(self, offset, x_0, y_0, scale):
        self.offset = offset
        self.x_0 = x_0
        self.y_0 = y_0
        self.scale = scale
        self.vertices = self.setVertices()
        self.show = True
        

    def setShow(self, s):
        self.show = s

    def setVertices(self):
        vertices = np.zeros(64, [("position", np.float32, 2)])

        angle = 0.0
        radius = 0.05*self.scale

        for count in range(64):
            if (count == 32):   radius = 0.02
            
            angle += 2*3.14/32
            
            x = math.cos(angle)*radius
            y = math.sin(angle)*radius

            vertices[count] = [x,y]
    
        return vertices


    def drawShape(self, loc_color, program):
        
        # Realiza uma operação de escala para 0, se não puder ser dividida
        if(self.show):
            size = 1
        else:
            size = 0

        mat_transformation = matrix.getMatrix(size*1, 0, self.x_0, self.y_0)
        loc = glGetUniformLocation(program, "mat_transformation")
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transformation)

        # silver coin
        rValue = 118.0 / 255.0
        gValue = 133.0 / 255.0
        bValue = 107.0 / 255.0

        glUniform4f(loc_color, rValue, gValue, bValue, 1.0) 
        glDrawArrays(GL_TRIANGLE_FAN, 0, 32)    

        glUniform4f(loc_color, 1, 1, 1, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 32, 31)         
                            


