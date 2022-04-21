# ship - gui
# star - mat
# coin - 
# final_flag - jun
# wall - mat



import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import ship
import star
#import coin
import flag

glfw.init()

# Janela
glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
window = glfw.create_window(1000, 500, "Trabalho 1 CG", None, None)
glfw.make_context_current(window)

# Define eventos do teclado
def key_event(window,button,action,mods):
    print('[key event] button=',button)
    print('[key event] action=',action)
    print('[key event] mods=',mods)
    print('-------')
glfw.set_key_callback(window, key_event)




# ======= GLSL ===== 

vertex_code = """
        attribute vec2 position;
        void main(){
            gl_Position = vec4(position,0.0,1.0);
        }
        """

fragment_code = """
        void main(){
            gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
        }
        """

# Request a program and shader slots from GPU
program  = glCreateProgram()
vertex   = glCreateShader(GL_VERTEX_SHADER)
fragment = glCreateShader(GL_FRAGMENT_SHADER)

# Set shaders source
glShaderSource(vertex, vertex_code)
glShaderSource(fragment, fragment_code)

# Compile shaders
glCompileShader(vertex)
if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(vertex).decode()
    print(error)
    raise RuntimeError("Erro de compilacao do Vertex Shader")

glCompileShader(fragment)
if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
    error = glGetShaderInfoLog(fragment).decode()
    print(error)
    raise RuntimeError("Erro de compilacao do Fragment Shader")

# Attach shader objects to the program
glAttachShader(program, vertex)
glAttachShader(program, fragment)

# Build program
glLinkProgram(program)
if not glGetProgramiv(program, GL_LINK_STATUS):
    print(glGetProgramInfoLog(program))
    raise RuntimeError('Linking error')
    
# Make program the default program
glUseProgram(program)

#myShip = ship.Ship()
#myShip.loadShape(program)

#myCoin = coin.Coin()
#myCoin.loadShape(program)

myStar = star.Star()
myStar.loadShape(program)

myFlag = flag.Flag()
myFlag.loadShape(program)



# ======= GLSL ===== 

glfw.show_window(window)

while not glfw.window_should_close(window):

    # funcao interna do glfw para gerenciar eventos de mouse, teclado, etc
    glfw.poll_events()

    # para as cores RGB
    rValue= 66.0 / 255.0
    gValue= 135.0 / 255.0
    bValue= 245.0 / 255.0

    # limpa a cor de fundo da janela e preenche com outra no sistema RGBA
    glClear(GL_COLOR_BUFFER_BIT)     
    glClearColor(rValue, gValue, bValue, 1.0)



    #myShip.drawShape()
    myStar.drawShape()
    myFlag.drawShape()

    # gerencia troca de dados entre janela e o OpenGL
    glfw.swap_buffers(window)

glfw.terminate()