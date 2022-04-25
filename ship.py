import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

class Ship1:
    vertices = np.zeros(5, [("position", np.float32, 2)])
    vertices['position'] = [
                            (-0.5, -0.5),  
                            (-0.5, 0.5), 
                            (+0.5,-0.5), 
                            ( 0.5, 0.5),
                            ( 0.75, 0.0), 
                            ]  
    offset = 0

    def drawShape(self, loc_color):
        glUniform4f(loc_color, 225.0/255, 71.0/255, 71.0/255, 1.0)  
        glDrawArrays(GL_TRIANGLE_STRIP, self.offset-1, 4)    
        glUniform4f(loc_color, 0.5, 134.0/255, 59.0/255, 1.0)      
        glDrawArrays(GL_TRIANGLES, self.offset-1 + 2, 3)       

class Ship2:
    vertices = np.zeros(4, [("position", np.float32, 2)])
    vertices['position'] = [
                            (-0.3, 0.4),  
                            (0.3, 0.4), 
                            (0.3,-0.4), 
                            (-0.3,-0.4), 
                            ]  
    offset = 0

    def drawShape(self, loc_color):
        glUniform4f(loc_color, 20.0/255, 71.0/255, 71.0/255, 1.0)  
        glDrawArrays(GL_TRIANGLE_FAN, self.offset-1, 4)          
                            


