import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

import ship, star, coin, flag


# Janela
def initWindow():
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(700, 700, "Trabalho 1 CG", None, None)
    glfw.make_context_current(window)

    return window

def vertexShader3D():
    vertex_code = """
            attribute vec2 position;
            void main(){
                gl_Position = vec4(position,0.0,1.0);
            }
            """
    
    vertex = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex, vertex_code)
    
    glCompileShader(vertex)
    if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex).decode()
        print(error)
        raise RuntimeError("Erro de compilacao do Vertex Shader")

    return vertex

def fragmentShader():
    fragment_code = """
            uniform vec4 color;
            void main(){
                gl_FragColor = color;
            }
            """

    fragment = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment, fragment_code)

    glCompileShader(fragment)
    if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(fragment).decode()
        print(error)
        raise RuntimeError("Erro de compilacao do Fragment Shader")

    return fragment

def programCreate():
    program  = glCreateProgram()
    
    vertex = vertexShader3D()
    glAttachShader(program, vertex)
    
    fragment = fragmentShader()
    glAttachShader(program, fragment)

    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Linking error')

    glUseProgram(program)

    return program

window = initWindow()
program = programCreate()


count = 0
vertices = np.zeros(84, [("position", np.float32, 2)])

# Get the Coin points
myCoin = coin.Coin();myCoin.findPoints()
myCoin.offset = count;count += myCoin.vertices.size; 
for i in range(myCoin.vertices.size):
    vertices[i+myCoin.offset] = myCoin.vertices[i]

# Get the Star points
myStar = star.Star()
myStar.offset = count;count += myStar.vertices.size; 
for i in range(myStar.vertices.size):
    vertices[i+myStar.offset-1] = myStar.vertices[i]

# Get the Flag points
myFlag = flag.Flag()
myFlag.offset = count;count += myFlag.vertices.size; 
vertices = np.append(vertices, myFlag.vertices)
for i in range(myFlag.vertices.size):
   vertices[i+myFlag.offset-1] = myFlag.vertices[i]

# Get Ship1 points
myShip1 = ship.Ship1()
myShip1.offset = count;count += myShip1.vertices.size; 
vertices = np.append(vertices, myShip1.vertices)
for i in range(myShip1.vertices.size):
   vertices[i+myShip1.offset-1] = myShip1.vertices[i]


# Get Ship2 points
myShip2 = ship.Ship2()
myShip2.offset = count;count += myShip2.vertices.size; 
vertices = np.append(vertices, myShip2.vertices)
for i in range(myShip2.vertices.size):
   vertices[i+myShip2.offset-1] = myShip2.vertices[i]


buffer = glGenBuffers(1)

# Make this buffer the default one
glBindBuffer(GL_ARRAY_BUFFER, buffer)

glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
glBindBuffer(GL_ARRAY_BUFFER, buffer)

# Bind the position attribute
# --------------------------------------
stride = vertices.strides[0]
offset = ctypes.c_void_p(0)

loc = glGetAttribLocation(program, "position")
glEnableVertexAttribArray(loc)

glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)

loc_color = glGetUniformLocation(program, "color")

glfw.show_window(window)

# para as cores RGB
rValue= 66.0 / 255.0
gValue= 135.0 / 255.0
bValue= 245.0 / 255.0

while not glfw.window_should_close(window):

    # funcao interna do glfw para gerenciar eventos de mouse, teclado, etc
    glfw.poll_events()
    
    # limpa a cor de fundo da janela e preenche com outra no sistema RGBA
    glClear(GL_COLOR_BUFFER_BIT)     
    glClearColor(rValue, gValue, bValue, 1.0)
    
    myCoin.drawShape(loc_color)
    myStar.drawShape(loc_color)
    myFlag.drawShape()
    myShip1.drawShape(loc_color)
    myShip2.drawShape(loc_color)

    # gerencia troca de dados entre janela e o OpenGL
    glfw.swap_buffers(window)

glfw.terminate()