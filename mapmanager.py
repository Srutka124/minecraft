



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
    def findBlock(self,pos):
        self.map.findAllMatches("=at="+str(pos))
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



    