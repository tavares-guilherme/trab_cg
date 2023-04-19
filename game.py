import math

class hitBox:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class Game:
    def __init__(self, coin, stars, planet, ship, ufo):
        
        self.gameState = 1
        self.coin = coin
        self.stars = stars
        self.planet = planet
        self.ship = ship
        self.ufo = ufo

    def __checkColision(sef, ob1, ob2):

        # Get distance between two points
        dist = math.sqrt((ob1.x - ob2.x)*(ob1.x - ob2.x) + (ob1.y-ob2.y)*(ob1.y-ob2.y))
        
        # Checks colision using the "hitbot" radius
        if(dist <= (ob1.radius + ob2.radius)):
            return True
        else:
            return False

    def setShipPosition(self, x, y):
        self.ship.x = -0.5+x
        self.ship.y =  0.5+y
    
    def updateUfoRange(self, operation):
        if(operation == 1):
            self.ufo.radius += 0.025
        else:
            self.ufo.radius -= 0.025
    
    def gameFlow(self):
        
        if(self.gameState == 0):
            self.gameState = 1
            return self.gameState

        # Stars
        for i in range(len(self.stars)):
            if(self.__checkColision(self.ship, self.stars[i])):
                self.gameState = 0
                print("Colidiu!")
                return self.gameState
        
        if(self.__checkColision(self.ship, self.ufo)):
            self.gameState = 0
            print("Colidiu")
            return self.gameState

        # Coin
        if(self.__checkColision(self.ship, self.coin)):
            self.gameState = 2
            return self.gameState
        
        if(self.__checkColision(self.ship, self.planet)):
            if(self.gameState == 1):
                self.gameState = 0
            else:
                self.gameState = 3
            return self.gameState


    
        
