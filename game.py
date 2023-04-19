import math

class hitBox:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class Game:
    def __init__(self, coin, stars, planet, ship):
        
        self.gameState = 1
        self.coin = coin
        self.stars = stars
        self.planet = planet
        self.ship = ship

    def __checkColision(sef, ob1, ob2):

        # Get full distance
        dist = math.sqrt((ob1.x - ob2.x)*(ob1.x - ob2.x) + (ob1.y-ob2.y)*(ob1.y-ob2.y))
        
        if(dist <= (ob1.radius + ob2.radius)):
            return True
        else:
            return False

    def setShipPosition(self, x, y):
        self.ship.x = -0.5+x
        self.ship.y =  0.5+y
    
    def gameFlow(self):
        
        if(self.gameState == 0):
            self.gameState = 1

        for i in range(len(self.stars)):
            if(self.__checkColision(self.ship, self.stars[0])):
                self.gameState = 0
                return self.gameState
        
        #Check coin
        if(self.__checkColision(self.ship, self.coin)):
            self.gameState = 2
            print("priqito")
            return self.gameState


    
        
