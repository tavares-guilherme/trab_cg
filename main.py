import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

import ship, star, coin, planet, ufo, game


# Janela
def initWindow():
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(700, 700, "Trabalho 1 CG", None, None)
    glfw.make_context_current(window)

    return window

def vertexShader():
    vertex_code = """
        attribute vec2 position;
        uniform mat4 mat_transformation;
        void main(){
            gl_Position = mat_transformation * vec4(position,0.0,1.0);
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
    
    vertex = vertexShader()
    glAttachShader(program, vertex)
    
    fragment = fragmentShader()
    glAttachShader(program, fragment)

    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Linking error')

    glUseProgram(program)

    return program

def setVertices(myCoin, uStar, rStar, ldStar, cStar, myPlanet, myShip, myUFO, offset_tot):
    vertices = np.zeros(offset_tot, [("position", np.float32, 2)])

    for i in range(myCoin.vertices.size):
        vertices[i + myCoin.offset] = myCoin.vertices[i]
        
    for i in range(uStar.vertices.size):
        vertices[i + uStar.offset] = uStar.vertices[i]

    for i in range(rStar.vertices.size):
        vertices[i + rStar.offset] = rStar.vertices[i]

    for i in range(ldStar.vertices.size):
        vertices[i + ldStar.offset] = ldStar.vertices[i]

    for i in range(cStar.vertices.size):
        vertices[i + cStar.offset] = cStar.vertices[i]

    for i in range(myPlanet.vertices.size):
        vertices[i + myPlanet.offset] = myPlanet.vertices[i]

    for i in range(myShip.vertices.size):
        vertices[i + myShip.offset] = myShip.vertices[i]

    for i in range(myUFO.vertices.size):
        vertices[i + myUFO.offset] = myUFO.vertices[i]

    buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    return vertices

def key_event(window,key,scancode,action,mods):
    global s_ufo, dg_planet, tx_ship, ty_ship, dg_ship, newGame

    if key == 265:      #cima
        ty_ship += 0.01
        dg_ship = 0 * math.pi
        newGame.setShipPosition(tx_ship, ty_ship)       
    
    if key == 264:      # baixo
        ty_ship -= 0.01
        dg_ship = 1 * math.pi
        newGame.setShipPosition(tx_ship, ty_ship)  

    if key == 263:      #esquerda
        tx_ship -= 0.01
        dg_ship = 0.5 * math.pi
        newGame.setShipPosition(tx_ship, ty_ship)  

    if key == 262:      #direita
        tx_ship += 0.01
        dg_ship = 1.5 * math.pi
        newGame.setShipPosition(tx_ship, ty_ship)  

    if key ==  32: dg_planet += 0.05  # espaço

    if key ==  65:
        s_ufo += 0.05     # A
        newGame.updateUfoRange(1)
    if key ==  90: 
        s_ufo -= 0.05     # Z
        newGame.updateUfoRange(2)

# Inicia os objetos

# Coin
myCoin = coin.Coin(0, 0.7, -0.7, 1)
offset_at = myCoin.vertices.size
objCoin = game.hitBox(0.7, -0.7, 0.05)

stars = []
# Estrela de baixo
uStar = star.Star(offset_at, 0.15, 0.7, 0.5)
offset_at += uStar.vertices.size
stars.append(game.hitBox(0.15, 0.7, 0.1))

# Estrela da direita
rStar = star.Star(offset_at, 0.6, -0.2, 0.5)
offset_at += rStar.vertices.size
stars.append(game.hitBox(0.6, -0.2, 0.1))

# Estrela da esquerda
ldStar = star.Star(offset_at, -0.6, -0.6, 0.5)
offset_at += ldStar.vertices.size
stars.append(game.hitBox(-0.6, -0.6, 0.1))

# Estrela do centro
cStar = star.Star(offset_at, -0.2, -0., 0.5)
offset_at += cStar.vertices.size
stars.append(game.hitBox(-0.2, 0, 0.1))

myPlanet = planet.Planet(offset_at, 0.7, 0.6)
offset_at += myPlanet.vertices.size
objPlanet = game.hitBox(0.7, 0.6, 0.14)

myShip = ship.Ship(offset_at, -0.5, 0.5)
offset_at += myShip.vertices.size
objShip = game.hitBox(-0.5, 0.5, 0.07)

myUFO = ufo.UFO(offset_at, 0, -0.7)
offset_at += myUFO.vertices.size
objUFO = game.hitBox(0, -0.7, 0.12)

newGame = game.Game(objCoin, stars, objPlanet, objShip, objUFO) 

window = initWindow()
program = programCreate()

vertices = setVertices(myCoin, myPlanet, uStar, rStar, ldStar, cStar, myShip, myUFO, offset_at)
stride = vertices.strides[0]
offset = ctypes.c_void_p(0)


loc = glGetAttribLocation(program, "position")
glEnableVertexAttribArray(loc)
glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)

loc_color = glGetUniformLocation(program, "color")

glfw.show_window(window)

# para as cores RGB
rValue= 0.0 / 255.0
gValue= 0.0 / 255.0
bValue= 0.0 / 255.0

glfw.set_key_callback(window,key_event)

s_ufo = 1.8
dg_planet = 0
tx_ship = 0
ty_ship = 0
dg_ship = 0
dg_star = 0

while not glfw.window_should_close(window):
    
    # funcao interna do glfw para gerenciar eventos de mouse, teclado, etc
    glfw.poll_events()
    gameState = newGame.gameFlow()
    
    # Reseta a posicao da nave se colidir
    if(gameState == 0):
        ty_ship = 0
        tx_ship = 0
        bValue = 0
        rValue = 0
        myCoin.setShow(1)
        myShip.setWColor(1)
    if(gameState == 2):
        myCoin.setShow(0)
        bValue = 1
        myShip.setWColor(2)
    if(gameState == 3): 
        myShip.setWColor(1)
        rValue = 2
        print("Fim de jogo!")

    # limpa a cor de fundo da janela e preenche com outra no sistema RGBA
    glClear(GL_COLOR_BUFFER_BIT)     
    glClearColor(rValue, gValue, bValue, 1.0)

    myCoin.drawShape(loc_color, program)
    myPlanet.drawShape(loc_color, program, dg_planet)
    myUFO.drawShape(loc_color, program, s_ufo)
    myShip.drawShape(loc_color, program, dg_ship, tx_ship, ty_ship)
    uStar.drawShape(loc_color, program, dg_star)
    rStar.drawShape(loc_color, program, dg_star)
    ldStar.drawShape(loc_color, program, -dg_star)
    cStar.drawShape(loc_color, program, dg_star)
    dg_star += 0.001
    
    # gerencia troca de dados entre janela e o OpenGL
    glfw.swap_buffers(window)

glfw.terminate()