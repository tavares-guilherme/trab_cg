import numpy as np
import math

def getMatrix(size, theta, t_x, t_y):
    return np.array([ size * math.cos(theta),    size * (-1) * math.sin(theta),  0.0,    t_x, 
                      size * math.sin(theta),    size * math.cos(theta),         0.0,    t_y, 
                      0.0,                       0.0,                            1.0,    0.0, 
                      0.0,                       0.0,                            0.0,    1.0],
                    np.float32)