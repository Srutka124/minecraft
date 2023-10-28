
import pickle

map
class MapManager:
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (0.2 , 0.2 , 0.35 , 1)

        self.addNew()
        
    def addNew(self):
        """створення основу для новоЇ карти
        """
        self.land = render.attachNewNode('Land')
    def addBlock(self,position):
        
        cube = loader.loadModel(self.model)
        cube_texture = loader.loadTexture(self.texture)


        cube.setTexture(cube_texture)
        cube.setPos(position)
        
        cube.setColor(self.color)
        cube.reparentTo(self.land)
        cube.setTag('at' , str(position))
    def delBlock(self, position):
        blocks = self.findBlock(position)
        for block in blocks:
           block.removeNode()
        
    def delBlockFrom (self, pos):
        x,y,z = self.findHightestEmpy(pos)
        pos = x , y , z-1
        blocks = self.findBlock(pos)
        for block in blocks :
            block.removeNode
    def buildBlock(self,pos):
        x , y , z = pos
        new_pos  = self.findHightestEmpy(pos)
        if new_pos[2] <= z+1 :
            self.addBlock(new_pos)
        else:
            self.map.buildBlock(pos)

    def loadMap(self, filename):
         """зчитування карти """
         with open(filename) as file :
            y = 0 
            for line in file :
                x = 0
                line = line.split(" ") 
                for number in line : 
                    if(number != "\n"):
                        for z in range(int(number)+1):
                            self.addBlock((x,y,z))
                        x +=1
                y+= 1
    def saveMap(self):
        blocks = self.land.getChildren()
        with open('map.dat',"wb") as file:
            pickle.dump(len(blocks) , file)
            for block in blocks :
                x , y , z = block.getPos()
                pos = (int(x) , int(y) ,int(z))
                pickle.dump(pos , file)
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def loadLend(self):
        self.clear()
        with open("map.dat" , "rb")as file:
            lenght = pickle.load(file)


            for i in range(lenght):
                pos = pickle.load(file)
                self.addBlock(pos, 'block')


    def findBlock(self,pos):
        return self.land.findAllMatches("=at="+str(pos))
    def isEmpty(self,pos):
        blocks = self.findBlock(pos)
        if blocks:
            return False
        else:
            return True
        
    def findHightestEmpy(self,pos):
        x, y , z = pos
        z =1 
        while not self.isEmpty((x,y,z)):
            z =+ 1

            return (x,y,z)



    