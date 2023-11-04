from direct.showbase.ShowBase import ShowBase
from hero import Hero
from mapmanager import MapManager
from direct.gui.OnscreenText import OnscreenText

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapManager()
        self.land.loadMap("map.txt")
        self.hero = Hero((0,0,1), self.land)
        textObject = OnscreenText(text='save', pos=(1, 0.7), scale=0.07)
        

game = Game()

game.run()
