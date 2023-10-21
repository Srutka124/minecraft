from direct.showbase.ShowBase import ShowBase
from hero import Hero
from mapmanager import MapManager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapManager()
        self.land.loadMap("map.txt")
        self.hero = Hero((0,0,1), self.land)
        
        

game = Game()

game.run()
